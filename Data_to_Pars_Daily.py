# =============================================================================
# Calculates daily CLIGEN precip parameters based on daily timeseries.
# The formatting of input data should match Daily_Data_WG_1.csv.
# Partial months or years are allowed (no checks for gaps).
# Creates tab separated .txt file and comma separated .csv of parameter values.
# =============================================================================

import datetime as dt
import pandas as pd
import numpy as np
import os

#==============================================================================
# Manually enter directory path below that contains script and data file.
#==============================================================================
dataFolder = r'...\dataFolder'
parFolder = r'...\dataParFolder'

acc_threshold = 0.0001 #Made very small. Any daily accumulation less than this number is omitted.

dataFiles = os.listdir( dataFolder )


def daily_pars( dataFile, dataDir, parDir ):

    rows = []
    with open(os.path.join( dataDir, dataFile )) as f:
        next(f)
        for line in f:            
            row = line.strip( '\n' ).split( ',' )
            date = dt.datetime( year=int(row[0]), month=int(row[1]), day=int(row[2]) )
            rows.append( [date, float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])] )
    
    dataset = pd.DataFrame()
    dataset['year'] = [date[0].year for date in rows]
    dataset['month'] = [date[0].month for date in rows]
    dataset['day'] = [date[0].day for date in rows]
    dataset['pcp in.'] = [value[1] for value in rows]
    dataset['Tmax F'] = [value[2] for value in rows] 
    dataset['Tmin F'] = [value[3] for value in rows] 
    dataset['Tdew F'] = [value[4] for value in rows] 
    dataset['Srad L'] = [value[5] for value in rows] 
    
    output_rows = []
    output_rows_tmp = []
    meanP_list, stddevP_list, skewP_list = [], [], []
    wd_list, ww_list = [], []
    tmax_list, tmin_list, tdew_list, tmax_sd_list, tmin_sd_list, tdew_sd_list = [], [], [], [], [], []
    srad_list, srad_sd_list = [], []
    
    for mo in range(1, 13):
        
        yr_mo_query = dataset.loc[(dataset['month'] == mo)]
        monthly_precip_by_year = yr_mo_query.groupby('year')['pcp in.'].apply( list )
        nonzeros = [item for month in monthly_precip_by_year for item in month if item >= acc_threshold]
    
        if len(nonzeros) > 0:
            meanP = sum(nonzeros) / len(nonzeros)
            meanP_list.append( meanP )
    
            stddevP = (sum([(x - meanP)**2 for x in nonzeros]) / (len(nonzeros) - 1))**0.5
            stddevP_list.append( stddevP )
    
            if stddevP != 0.0:
                skewP = sum([((x - meanP)/stddevP)**3 for x in nonzeros]) / (len(nonzeros) - 1)
                skewP_list.append( skewP )                
            else:    
                skewP_list.append( 0 )
    
        else:
            meanP_list.append( 0.0 )
            stddevP_list.append( 0.0 )
            skewP_list.append( 0.0 )

        monthly_tmax_by_year = yr_mo_query.groupby('year')['Tmax F'].apply( list )
        monthly_tmin_by_year = yr_mo_query.groupby('year')['Tmin F'].apply( list )
        monthly_tdew_by_year = yr_mo_query.groupby('year')['Tdew F'].apply( list )
        monthly_srad_by_year = yr_mo_query.groupby('year')['Srad L'].apply( list )

        tmax_values = [item for month in monthly_tmax_by_year for item in month]
        tmin_values = [item for month in monthly_tmin_by_year for item in month]
        tdew_values = [item for month in monthly_tdew_by_year for item in month]
        srad_values = [item for month in monthly_srad_by_year for item in month]

        tmax_list.append( np.mean( tmax_values ) )
        tmin_list.append( np.mean( tmin_values ) )
        tdew_list.append( np.mean( tdew_values ) )
        srad_list.append( np.mean( srad_values ) )   
        tmax_sd_list.append( np.std( tmax_values, ddof=1 ) )
        tmin_sd_list.append( np.std( tmin_values, ddof=1 ) )
        tdew_sd_list.append( np.std( tdew_values, ddof=1 ) )
        srad_sd_list.append( np.std( srad_values, ddof=1 ) )

        wd_ct = 0; dd_ct = 0; dw_ct = 0; ww_ct = 0
        dry_ct = 0; wet_ct = 0

        for mo_data in monthly_precip_by_year:

            for i, elem in enumerate(mo_data):
                
                if i < len(mo_data) - 1:
    
                    if (elem) < acc_threshold and (mo_data[i+1]) >= acc_threshold:
                        wd_ct += 1
                    elif (elem) < acc_threshold and (mo_data[i+1]) < acc_threshold:
                        dd_ct += 1
                    elif (elem) >= acc_threshold and (mo_data[i+1]) < acc_threshold:
                        dw_ct += 1
                    elif (elem) >= acc_threshold and (mo_data[i+1]) >= acc_threshold:
                        ww_ct += 1
                    else:
                        pass
    
                else:
                    pass
    
                if elem < acc_threshold:
                    dry_ct += 1
                else:
                    wet_ct += 1
    
            if wd_ct + dd_ct > 0:
                wd = wd_ct / (wd_ct + dd_ct)
            else:
                wd = 0
        
            if dw_ct + ww_ct > 0:
                ww = ww_ct / (dw_ct + ww_ct)
            else:
                ww = 0
        
            wd_list.append( wd )
            ww_list.append( ww )


    for i in range(12):
        meanP = '{:.2f}'.format( meanP_list[i] ).lstrip( '0' )
        sdevP = '{:.2f}'.format( stddevP_list[i] ).lstrip( '0' )
        skewP = '{:.2f}'.format( skewP_list[i] ).lstrip( '0' )
        ww = '{:.2f}'.format( ww_list[i] ).lstrip( '0' )
        wd = '{:.2f}'.format( wd_list[i] ).lstrip( '0' )
        tmax = '{:.2f}'.format( tmax_list[i] ).lstrip( '0' )
        tmin = '{:.2f}'.format( tmin_list[i] ).lstrip( '0' )
        tmaxsd = '{:.2f}'.format( tmax_sd_list[i] ).lstrip( '0' )
        tminsd = '{:.2f}'.format( tmin_sd_list[i] ).lstrip( '0' )
        srad = '{:.0f}'.format( srad_list[i] ) + '.'
        sradsd = '{:.1f}'.format( srad_sd_list[i] ).lstrip( '0' )
        tdew = '{:.2f}'.format( tdew_list[i] ).lstrip( '0' )
        
        ###
        #Cases that could result in divide by zero error
        ###
        
        #In case wd rounds to zero when there is non-zero monthly accumulation
        if wd == '.00' and float(meanP) >= 0.01:
            wd = '.01' 
        else:
            wd = wd
        
        #In case there is zero monthly accumulation
        if meanP == '.00':
            wd = '0.01'
            ww = '0.00'
        else:
            pass
            
        #In case it rains every day 
        if ww == '1.00':
            ww = '.99'
        else:
            ww = ww
    
        output_rows_tmp.append( [meanP, sdevP, skewP, ww, wd, tmax, tmin, tmaxsd, tminsd, srad, sradsd, tdew] )
    
    output_rows.extend( output_rows_tmp )
    
    flipped = np.array( output_rows ).transpose()
    
    indices = ['MEAN P', 'S DEV P', 'SKEW  P', 'P(W/W)', 'P(W/D)', 'TMAX AV', 'TMIN AV', 'SD TMAX', 'SD TMIN', 'SOL.RAD', 'SD SOL', 'DEW PT']
    df = pd.DataFrame( flipped, index=indices, columns=list(range(1,13)) )
    df.columns.name = dataFile
    df.to_csv( os.path.join( parDir, dataFile ), index_label=dataFile )
    
    with open(os.path.join( parDir, dataFile.strip( '.csv' ) + '.txt' ), 'w') as f_out:
    
        for index in indices:

            row = df.loc[index,:]
            f_out.write( index.ljust( 4 ) + '\t' )
            for j, elem in enumerate(row):
    
                if j < len(row)-1:
                    f_out.write( elem.rjust( 6 ) + '\t' )
                elif j == len(row) - 1:
                    f_out.write( elem.rjust( 6 ) + '\n' )
                else:
                    pass
                
    return 0


run_ct = 0
for file in dataFiles:
    output = daily_pars( file, dataFolder, parFolder )
    run_ct += 1
    print(str(run_ct) + ' / ' + str(len(dataFiles)))
    
