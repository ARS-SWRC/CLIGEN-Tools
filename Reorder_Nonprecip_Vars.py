# =============================================================================
# Creates CLIGEN output file with Tmax, Tmin, and srad reordered on a monthly 
# basis. Tmax is reordered to increase autocorrelation. Then, Tmin is reordered 
# to pair values in sorted order with coinciding Tmax values in sorted order. 
# Srad is reordered by pairing srad values in reverse sorted order to the sorted 
# order of precip amounts on days with precip. The ordering of srad on nonprecip
# days is unchanged.
# =============================================================================
import pandas as pd
import os
import random

#==============================================================================
# Manually enter directory paths below
#==============================================================================
tseriesFolder = r'C:\Users\afullhart\Desktop\CLIGEN-Tools\tseriesFolder'
reorderedFolder = r'C:\Users\afullhart\Desktop\CLIGEN-Tools\reorderedFolder'

tseriesFiles = os.listdir( tseriesFolder )

TEMP_WINDOW = 5 #Affects the strength of autocorrelation in reordered Tmax
REC_LEN = 200


def reorder( tseriesFile, tseriesDir, reorderedDir ):
    
    with open(os.path.join( tseriesDir, tseriesFile) ) as f:
        lines = f.readlines()
    
    columns=lines[13].split()
    
    df = pd.DataFrame( data=[row.split() for row in lines[15:-1]], columns=columns )
    
    tminsmaxs_list = []
    srads_list = []
    for yrnum in range(1,REC_LEN+1):
        for monum in range(1, 13):
            monthdf = df.loc[(df['year']==str(yrnum)) & (df['mo']==str(monum))]
            prcps = monthdf['prcp'].astype(float).to_list()
            srads = monthdf['rad'].astype(float).to_list()
            tmaxs = monthdf['tmax'].astype(float).to_list()
            tmins = monthdf['tmin'].astype(float).to_list()
    
            reordered = []
            reordered.append( tmaxs[0] )
            pool = tmaxs[1:]
            for i in range(len(tmaxs[:-1])):
                
                filterPool = [pool[j] for j, elem in enumerate(pool) if abs(reordered[i] - pool[j]) <= TEMP_WINDOW] 
                if len(filterPool) > 0:
                    pick = random.choice( filterPool )
                else:
                    pick = min(pool, key=lambda x:abs(x-reordered[i]))
                
                xi = pool.index( pick )
                pool = pool[:xi] + pool[xi+1:]
                reordered.append( pick )
            
            tmaxs = reordered
            tminsmaxs = list(zip(sorted(tmins), sorted(tmaxs)))
            tDict = {pair[1]:[] for pair in tminsmaxs}
            for minmax in tminsmaxs:
                tDict[minmax[1]].append( minmax[0] )
            
            tminsmaxs = []
            for tmax in tmaxs:
                tmin = tDict[tmax][0]
                tDict[tmax] = tDict[tmax][1:]
                tminsmaxs.append( [tmin, tmax] )
    
            tminsmaxs_list.extend( tminsmaxs )
    
            prcpssrads = list(zip(sorted(srads, reverse=True), sorted(prcps)))
            sradDict = {pair[1]:[] for pair in prcpssrads}
            for prcpsrad in prcpssrads:
                sradDict[prcpsrad[1]].append( prcpsrad[0] )
            
            srads = []
            for prcp in prcps:
                srad = sradDict[prcp][0]
                sradDict[prcp] = sradDict[prcp][1:]
                srads.append( srad )
    
            srads_list.extend( srads )
    
    
    with open(os.path.join( reorderedDir, tseriesFile ), 'w') as f_out:
        for line in lines[:15]:
            f_out.write( line )
        for i, line in enumerate(lines[15:-1]):
            tmax = tminsmaxs_list[i][1]
            tmin = tminsmaxs_list[i][0]
            srad = srads_list[i]
            part1 = line[:35]
            part2 = str(tmax).rjust( 6 )
            part3 = str(tmin).rjust( 6 )
            part4 = str(srad).rstrip( '0' ).rjust( 5 )
            part5 = line[52:]
            f_out.write( part1 + part2 + part3 + part4 + part5 )
        
        f_out.write( lines[-1] )
    
    return 0



run_ct = 0
for file in tseriesFiles:
    output = reorder( file, tseriesFolder, reorderedFolder )
    run_ct += 1
    print(str(run_ct) + ' / ' + str(len(tseriesFiles)))

