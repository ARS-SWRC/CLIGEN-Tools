#==============================================================================
# Calculates RUSLE2 R-factor from daily CLIGEN timeseries output according to
# Bofu Yu (2002) - Using CLIGEN to Generate RUSLE Climate Inputs [Trans. ASABE]
# erosivity units: (Mj mm / ha h yr), erosivity density units: (Mj / ha h yr)
#==============================================================================

from scipy import optimize
import numpy as np
import os

# =============================================================================
# Manually enter directory paths below
# =============================================================================
tseriesFolder = r'...\tseriesFolder'
outputFolder = r'...\outputFolder'

REC_LEN = 200

tseriesFiles = os.listdir( tseriesFolder )

eo = 0.29; a = 0.72; io = 12.195


def newton( b_, ip_ ):
    return (ip_ * (1 - np.exp(-b_))) - (b_)  

def i30( p_, ip_, d_, b_ ): 
    return ((2*p_*ip_)/(b_)) * (1 - np.exp(-((b_)/(2*d_))))

def energy( p_, ip_, lp_, b_, eo_, a_, io_,  ):
    inside = np.exp( -(lp_ / io_)*np.exp( -b_ ) ) - np.exp( -lp_ / io_ )
    middle = ((a_*ip_)/(b_)) * (io_/lp_)
    outside = p_*eo_
    return (outside)*((1)-(middle*inside))


def Rusle2_R( tseriesFile, tseriesDir, outputDir ):
    
    moEro_dict = {str(i):[] for i in range(1,13)}
    moDen_dict = {str(i):[] for i in range(1,13)}
    yrEro_dict = {str(i):[] for i in range(1,REC_LEN+1)}
    yrDen_dict = {str(i):[] for i in range(1,REC_LEN+1)}
    
    ei_list, mo_ei_list, yr_ei_list = [], [], []
    moLast, yrLast = '1', '1'
    moP, yrP = 0., 0.

    with open(os.path.join( tseriesFolder, tseriesFile )) as f:
        lines = f.readlines()[15:-1]

    for line in lines:

        row = line.split( )
        p = float(row[3])
        tavg = (float(row[7]) + float(row[8])) / 2.
        moNow = row[1]
        yrNow = row[2]

        if p >= 12. and tavg > 0.:
            ip = float(row[6])
            b = optimize.newton( func=newton, x0=ip, args=(ip,) )
            d = float(row[4])
            lp = ip * (p/d)
            if d > 0.5:
                l30 = i30( p, ip, d, b )
            else:
                l30 = 2*p
            e = energy( p, ip, lp, b, eo, a, io )
            ei = e*l30
            ei_list.append( ei )

        else:
            ei = 0.
            ei_list.append( ei )

        if moNow != moLast:
            if moP > 0.:
                moEro_dict[moLast].append( sum(mo_ei_list) )
                moDen_dict[moLast].append( sum(mo_ei_list) / moP )
                moP = p
                mo_ei_list = []
                mo_ei_list.append( ei )
            else:
                moEro_dict[moLast].append( 0. )
                moDen_dict[moLast].append( 0. )
        else:            
            moP += p
            mo_ei_list.append( ei )

        if yrNow != yrLast:

            if yrP > 0.:
                yrEro_dict[yrLast].append( sum(yr_ei_list)  )
                yrDen_dict[yrLast].append( sum(yr_ei_list) / yrP )
                yrP = p
                yr_ei_list = []
                yr_ei_list.append( ei )
            else:
                yrEro_dict[yrLast].append( 0. )
                yrDen_dict[yrLast].append( 0. )
        else:            
            yrP += p
            yr_ei_list.append( ei )

        moLast = moNow
        yrLast = yrNow

    if moP > 0.:
        moEro_dict[moLast].append( sum(mo_ei_list) )
        moDen_dict[moLast].append( sum(mo_ei_list) / moP )
    else:
        moEro_dict[moLast].append( 0. )
        moDen_dict[moLast].append( 0. )
    
    if yrP > 0.:
        yrEro_dict[yrLast].append( sum(yr_ei_list) )
        yrDen_dict[yrLast].append( sum(yr_ei_list) / yrP )
    else:
        yrEro_dict[yrLast].append( 0. )
        yrDen_dict[yrLast].append( 0. )

    moEro_list = [str(sum(value)/REC_LEN) for key, value in moEro_dict.items()]
    moDen_list = [str(sum(value)/REC_LEN) for key, value in moDen_dict.items()]
    annEro = str(sum(value[0] for key, value in yrEro_dict.items()) / REC_LEN)
    annDen = str(sum(value[0] for key, value in yrDen_dict.items()) / REC_LEN)

    with open(os.path.join( outputFolder, tseriesFile ), 'w') as f_out:
        f_out.write( 'Annual Erosivity: ' + annEro + '\n' )
        f_out.write( 'Annual Erosivity Density: ' + annDen + '\n' )
        f_out.write( 'Monthly Erosivity: ' + ','.join( moEro_list ) + '\n' )
        f_out.write( 'Monthly Erosivity Density: ' + ','.join( moDen_list ) + '\n' )

    return 0


for file in tseriesFiles:
    output = Rusle2_R( file, tseriesFolder, outputFolder )

