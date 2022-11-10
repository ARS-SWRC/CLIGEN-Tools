# =============================================================================
# Disaggregates to chosen sub-daily interval.
# 200 yr time series disaggregated to 10 min produces ~500mb output file
# =============================================================================
import datetime as dt
import math
import os
from classes.Disaggregate import Disaggregate
disagg_obj = Disaggregate()

#==============================================================================
# Manually enter directory paths below
#==============================================================================
tseriesFolder = r'...\tseriesFolder'
outputFolder = r'...\outputFolder'

MIN_INTERVAL = 10
START_DATE = '2001,01,01' #Zero-padded year,month,day. Needs to be the first day of a year after a leap year.
PRECIP_HOUR = 12 #Must be equally divisible by MIN_INTERVAL. 

tseriesFiles = os.listdir( tseriesFolder )


def disagg( tseriesFile, tseriesDir, outputDir ):
    
    time = dt.datetime.strptime( START_DATE, '%Y,%m,%d' )
    
    daily_interval_n = int(1440./MIN_INTERVAL)

    with open(os.path.join( tseriesDir, tseriesFile )) as f:
        lines = f.readlines()
    
    lat = float(lines[4].split()[0])
    lon = float(lines[4].split()[1])
    
    yrLast = 0
    precip_two = [0.]*int(PRECIP_HOUR*60./MIN_INTERVAL)
    with open(os.path.join( outputDir, tseriesFile ), 'w') as f_out:
    
        f_out.write( 'yr,mo,day,hr,min,precip,temp,dewpt,solrad,windsp,windir\n' )
        for i, line in enumerate(lines[15:-2]):
    
            row = line.split()
            rownext = lines[i+1+15].split()
    
            yr = int(row[2])
            if yr != yrLast:
                jday = 0
        
            jday += 1.
    
            yrLast = yr
    
            precip_list = disagg_obj.precip( row, MIN_INTERVAL )
    
            precip_one = [elem for elem in precip_list[:int(PRECIP_HOUR*60./MIN_INTERVAL)]]                  \
                       + [0.]*math.ceil((24. - PRECIP_HOUR - len(precip_list)*MIN_INTERVAL/60.)*60./MIN_INTERVAL)
    
            precip_list_one = ['%.3f'%elem for elem in precip_one]
            precip_list_two = ['%.3f'%elem for elem in precip_two]     
            temps_list = ['%.3f'%elem for elem in disagg_obj.temp( row, MIN_INTERVAL )]
            dewpt_list = ['%.3f'%elem for elem in disagg_obj.dewpt( row, rownext, MIN_INTERVAL )]
            solrad_list = ['%.3f'%elem for elem in disagg_obj.solrad( row, jday, lat, lon, MIN_INTERVAL )]
            windsp_list = ['%.3f'%elem for elem in disagg_obj.windspeed( row, MIN_INTERVAL )]
            winddir_list = ['%.3f'%elem for elem in [float(row[11])]*daily_interval_n]
    
            for j in range(daily_interval_n):
    
                outDate = dt.datetime.strftime( time, '%Y,%m,%d,%H,%M' )    
                
                if j >= int(PRECIP_HOUR*60./MIN_INTERVAL):
                    precip = precip_list_one[int(j - PRECIP_HOUR*60./MIN_INTERVAL)]
    
                else:
                    precip = precip_list_two[j]
    
                output_list = [outDate, precip, temps_list[j], dewpt_list[j], solrad_list[j], windsp_list[j], winddir_list[j]]
                f_out.write( ','.join( output_list ) + '\n' )
    
                time = time + dt.timedelta( seconds=60.*MIN_INTERVAL )

            if len(precip_list)*MIN_INTERVAL/60. > 24. - PRECIP_HOUR:
                precip_two = [elem for elem in precip_list[int(PRECIP_HOUR*60./MIN_INTERVAL):]]                  \
                            + [0.]*int(PRECIP_HOUR*60./MIN_INTERVAL - (len(precip_list) - PRECIP_HOUR*60./MIN_INTERVAL))
            else:
                precip_two = [0.]*int(PRECIP_HOUR*60./MIN_INTERVAL)
    
    return 0


run_ct = 0
for file in tseriesFiles:
    output = disagg( file, tseriesFolder, outputFolder )
    run_ct += 1
    print(str(run_ct) + ' / ' + str(len(tseriesFiles)))
    


