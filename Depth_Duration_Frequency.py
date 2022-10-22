#==============================================================================
# Calculates return level depths in two ways: (1) empirically from annual maxima 
# in CLIGEN timeseries, and (2) statistically by fitting the annual maxima to the 
# GEV distribution. Location and scale parameters for the GEV equation are fitted,
# and the shape parameter is assummed to be -0.114. Bootstrapping is done to
# determine location and scale fitting uncertainties at 95% confidence. 
# The Filliben statistic is used as a measure of GEV goodness-of-fit.
# The Filliben statistic is found by plotting GEV versus empirical values on a 
# Q-Q plot using the Cunnane plotting position in this case. Two text file 
# outputs are generated for each station: one for empirical data and one for 
# GEV-fitted data. Units for return level depths and location and scale 
# parameters are in mm.
#==============================================================================

from scipy.stats import genextreme
from scipy import optimize
from scipy import stats
import numpy as np
import math
import os
import pandas as pd
import warnings
warnings.filterwarnings( 'error' )

#==============================================================================
# Manually enter directory paths below
#==============================================================================
tseriesFolder = r'...\tseriesFolder'
outputFolder = r'...\outputFolder'

#==============================================================================
# Duration schemes list may be modified to include any duration in the range 
# of [1, 'MIN'] to [1, 'YEAR'] with units of minutes, days, or years (only 1-year).
#==============================================================================
dur_schemes = [[10, 'MIN'], [15, 'MIN'], [30, 'MIN'], [60, 'MIN'], [120, 'MIN'], [180, 'MIN'], [360, 'MIN'], [720, 'MIN'],
               [1, 'DAY'], [2, 'DAY'], [3, 'DAY'], [4, 'DAY'], [7, 'DAY'], [10, 'DAY'], [30, 'DAY'], 
               [1, 'YEAR']]

#==============================================================================
# Return periods in years list may be modified. Empirical return levels will be
# invalid for any return period that the record length is not evenly divisible by.
# The empirical values will all be valid for the periods below if a 500 year
# time series is used.
#==============================================================================
recurrences = [2, 5, 10, 20, 25, 50, 100, 250, 500]


tseriesFiles = os.listdir( tseriesFolder )


def newton( B, ip ):
    return (ip * (1 - np.exp(-B))) - (B)
  
def empirical_return_levels( xvalues, return_periods ):
    return_levels = []
    for per in return_periods:
        return_levels.append( xvalues[int(-(len(xvalues)/per))] )
    return return_levels

def bootstrap_replicate_1d( data, func ):
    bs_sample = np.random.choice( data, len(data) )
    return func( bs_sample )

def draw_bs_reps( data, func, size=1 ):
    bs_replicates = np.empty( size )
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d( data, func )
    return bs_replicates

def loc_bs( data ):
    loc, scale = genextreme.fit_loc_scale( data, -0.114 )
    return loc

def scale_bs( data ):
    loc, scale = genextreme.fit_loc_scale( data, -0.114 )
    return scale

def minutely_max( lines, MIN_INTERVAL ):
    yrNow = 1
    accumulations = []
    maxima = []
    for line in lines[15:-1]:
        row = line.split( )
        yr = int(row[2])
        if row[3] != '*****':
            p = float(row[3])
        else:
            p = 0.
        d = float(row[4])
   
        if yr != yrNow:
            maxima.append( max(accumulations) )
            accumulations = []
            yrNow = yr
   
        if p > 0 and d >= float(MIN_INTERVAL)/60.:
            ip = float(row[6])
            B = optimize.newton( func=newton, x0=ip, args=(ip,) )
            i_value = (ip/(B*(float(MIN_INTERVAL)/60./d)))*(1-math.exp(-B*(float(MIN_INTERVAL)/60./d)))
            I_value = i_value*(p/d)
   
        elif p > 0 and d < float(MIN_INTERVAL)/60.:
            if MIN_INTERVAL < 60:
                I_value = p*(float(MIN_INTERVAL)/60.)
            else:
                I_value = p/(float(MIN_INTERVAL)/60.)
   
        elif p == 0:
            I_value = 0.
               
        else:
            pass
   
        accumulations.append( I_value*(float(MIN_INTERVAL)/60.) )

    maxima.append( max(accumulations) )

    return maxima

def daily_max( lines, DAY_INTERVAL ):
    yrNow = 1
    daily_accumulations = []
    accumulations = []
    maxima = []
    for line in lines[15:-1]:
        row = line.split( )
        yr = int(row[2])
        if row[3] != '*****':
            p = float(row[3])
        else:
            p = 0.
        daily_accumulations.append( p )

        if yr != yrNow:
            for j, accum in enumerate(daily_accumulations):
                start_index = j
                end_index = j + DAY_INTERVAL
                accumulations.append( sum(daily_accumulations[start_index:end_index]) )
            maxima.append( max(accumulations) )
            
            daily_accumulations = []
            accumulations = []
            yrNow = yr

    for j, accum in enumerate(daily_accumulations):
        start_index = j
        end_index = j + DAY_INTERVAL
        accumulations.append( sum(daily_accumulations[start_index:end_index]) )

    maxima.append( max(accumulations) )

    return maxima

def yearly_max( lines ):
    yrNow = 1
    maxima = []
    accumulations = []
    for line in lines[15:-1]:
        row = line.split( )
        yr = int(row[2])
        if row[3] != '*****':
            p = float(row[3])
        else:
            p = 0.
        accumulations.append( p )
   
        if yr != yrNow:
            maxima.append( sum(accumulations) )
            accumulations = []
            yrNow = yr

    maxima.append( sum(accumulations) )

    return maxima

def ddf( file, tseriesDir, outputDir, schemes, periods ):

    stationID = file.strip( '.txt' )

    schemeLabels = [str(elem[0]) + '_' + elem[1] for elem in schemes]

    return_periods = np.array( periods )

    with open( tseriesDir + '\\' + stationID + '.txt') as f:
        tserieslines = f.readlines()

    scheme_level_data = []
    for scheme in schemes:    
               
        min_interval = scheme[0]
        day_interval = scheme[0]
        timeWindow = scheme[1]

        if timeWindow == 'MIN':
            annualMaxima = minutely_max( tserieslines, min_interval )


        elif timeWindow == 'DAY':
            annualMaxima = daily_max( tserieslines, day_interval )

        elif timeWindow == 'YEAR':
            annualMaxima = yearly_max( tserieslines )
       
        else:
            pass
           
        scheme_level_data.append( annualMaxima )    

    stationdf_emp = pd.DataFrame( None, schemeLabels, return_periods )
    stationdf_gev = pd.DataFrame( None, schemeLabels, return_periods )
    for j, data in enumerate(scheme_level_data):

        data = sorted(data)
        x = data

        return_levels = empirical_return_levels( x, return_periods ) 
        stationdf_emp.loc[schemeLabels[j], return_periods] = return_levels  

        try:
            shape = -0.114
            loc, scale = genextreme.fit_loc_scale( x, shape )

        except RuntimeWarning:
            shape = -0.114
            loc, scale = -9999., -9999.
            print('gev error')

        bs_replicates = draw_bs_reps( x, loc_bs, size=10000 )
        locLowerCI, locUpperCI = np.percentile( bs_replicates, [2.5, 97.5] )
        bs_replicates = draw_bs_reps( x, scale_bs, size=10000 )
        scaleLowerCI, scaleUpperCI = np.percentile( bs_replicates, [2.5, 97.5] )
                
        stationdf_gev.at[schemeLabels[j], 'loc'] = loc
        stationdf_gev.at[schemeLabels[j], 'scale'] = scale
        stationdf_gev.at[schemeLabels[j], 'locUpperCI'] = locUpperCI
        stationdf_gev.at[schemeLabels[j], 'locLowerCI'] = locLowerCI
        stationdf_gev.at[schemeLabels[j], 'scaleUpperCI'] = scaleUpperCI
        stationdf_gev.at[schemeLabels[j], 'scaleLowerCI'] = scaleLowerCI

        fitValues = []
        for per in return_periods:
            xval = loc + ((scale*(1. - (-np.log(1. - 1./per))**shape))/(shape))
            fitValues.append( xval )

        stationdf_gev.loc[schemeLabels[j], return_periods] = fitValues

        n = len(x)
        empirical_plotting_probabilities = []
        for k in range(len(x)):
            empirical_plotting_probabilities.append( (k+1-0.4) / (n+0.2) )

        empirical_plotting_values = x[::-1]

        qq_values = []
        for k in range(len(x)):
            xval = loc + ((scale*(1. - (-np.log(1. - empirical_plotting_probabilities[k]))**shape))/(shape))
            qq_values.append( xval )

        rStat = stats.pearsonr( qq_values, empirical_plotting_values )
        stationdf_gev.at[schemeLabels[j], 'filli'] = rStat[0]
    
    stationdf_emp.to_csv( outputDir + '\\' + stationID + '_emp.txt', index_label='return per. (yrs)' )
    stationdf_gev.to_csv( outputDir + '\\' + stationID + '_gev.txt', index_label='return per. (yrs)' )

    return 0


run_ct = 1
for file in tseriesFiles:
    print(str(run_ct) + ' / ' + str(len(tseriesFiles)))
    output = ddf( file, tseriesFolder, outputFolder, dur_schemes, recurrences )
    run_ct += 1




