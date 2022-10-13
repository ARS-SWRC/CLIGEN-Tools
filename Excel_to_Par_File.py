#==============================================================================
#Converts an Excel file that contains imported text output from 
#Par_File_Delimiting.py into a par file
#==============================================================================

import os
import pandas as pd
from classes.Formatting import Formatting
formatting_obj = Formatting()

# =============================================================================
# Manually enter directory paths below
# =============================================================================
excelFolder = r'...\excelFolder'
outputFolder = r'...\outputFolder'

files = os.listdir( excelFolder )


def write_par( excelFile, excelFolder, outputFolder ):

    filePath = os.path.join( excelFolder, excelFile )
    
    names = ['par', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    df = pd.read_excel( filePath, names=names, header=None, index_col=False )
    
    meanP_list = df.loc[df['par'] == 'MEAN P'].iloc[:,1:].values.tolist()[0]
    sdevP_list = df.loc[df['par'] == 'S DEV P'].iloc[:,1:].values.tolist()[0]
    skewP_list = df.loc[df['par'] == 'SKEW  P'].iloc[:,1:].values.tolist()[0]
    ww_list = df.loc[df['par'] == 'P(W/W)'].iloc[:,1:].values.tolist()[0]
    wd_list = df.loc[df['par'] == 'P(W/D)'].iloc[:,1:].values.tolist()[0]
    tmax_list = df.loc[df['par'] == 'TMAX AV'].iloc[:,1:].values.tolist()[0]
    tmin_list = df.loc[df['par'] == 'TMIN AV'].iloc[:,1:].values.tolist()[0]
    sdtmax_list = df.loc[df['par'] == 'SD TMAX'].iloc[:,1:].values.tolist()[0]
    sdtmin_list = df.loc[df['par'] == 'SD TMIN'].iloc[:,1:].values.tolist()[0]
    solrad_list = df.loc[df['par'] == 'SOL.RAD'].iloc[:,1:].values.tolist()[0]
    solsdev_list = df.loc[df['par'] == 'SD SOL'].iloc[:,1:].values.tolist()[0]
    mx5p_list = df.loc[df['par'] == 'MX .5 P'].iloc[:,1:].values.tolist()[0]
    dewpt_list = df.loc[df['par'] == 'DEW PT'].iloc[:,1:].values.tolist()[0]
    timepk_list = df.loc[df['par'] == 'Time Pk'].iloc[:,1:].values.tolist()[0]
    N_list = df.loc[df['par'] == '% N'].iloc[:,1:].values.tolist()[0]
    Nmean_list = df.iloc[18][1:].values.tolist()
    Nsdev_list = df.iloc[19][1:].values.tolist()
    Nskew_list = df.iloc[20][1:].values.tolist()
    NNE_list = df.loc[df['par'] == '% NNE'].iloc[:,1:].values.tolist()[0]
    NNEmean_list = df.iloc[22][1:].values.tolist()
    NNEsdev_list = df.iloc[23][1:].values.tolist()
    NNEskew_list = df.iloc[24][1:].values.tolist()
    NE_list = df.loc[df['par'] == '% NE'].iloc[:,1:].values.tolist()[0]
    NEmean_list = df.iloc[26][1:].values.tolist()
    NEsdev_list = df.iloc[27][1:].values.tolist()
    NEskew_list = df.iloc[28][1:].values.tolist()
    ENE_list = df.loc[df['par'] == '% ENE'].iloc[:,1:].values.tolist()[0]
    ENEmean_list = df.iloc[30][1:].values.tolist()
    ENEsdev_list = df.iloc[31][1:].values.tolist()
    ENEskew_list = df.iloc[32][1:].values.tolist()
    E_list = df.loc[df['par'] == '% E'].iloc[:,1:].values.tolist()[0]
    Emean_list = df.iloc[34][1:].values.tolist()
    Esdev_list = df.iloc[35][1:].values.tolist()
    Eskew_list = df.iloc[36][1:].values.tolist()
    ESE_list = df.loc[df['par'] == '% ESE'].iloc[:,1:].values.tolist()[0]
    ESEmean_list = df.iloc[38][1:].values.tolist()
    ESEsdev_list = df.iloc[39][1:].values.tolist()
    ESEskew_list = df.iloc[40][1:].values.tolist()
    SE_list = df.loc[df['par'] == '% SE'].iloc[:,1:].values.tolist()[0]
    SEmean_list = df.iloc[42][1:].values.tolist()
    SEsdev_list = df.iloc[43][1:].values.tolist()
    SEskew_list = df.iloc[44][1:].values.tolist()
    SSE_list = df.loc[df['par'] == '% SSE'].iloc[:,1:].values.tolist()[0]
    SSEmean_list = df.iloc[46][1:].values.tolist()
    SSEsdev_list = df.iloc[47][1:].values.tolist()
    SSEskew_list = df.iloc[48][1:].values.tolist()
    S_list = df.loc[df['par'] == '% S'].iloc[:,1:].values.tolist()[0]
    Smean_list = df.iloc[50][1:].values.tolist()
    Ssdev_list = df.iloc[51][1:].values.tolist()
    Sskew_list = df.iloc[52][1:].values.tolist()
    SSW_list = df.loc[df['par'] == '% SSW'].iloc[:,1:].values.tolist()[0]
    SSWmean_list = df.iloc[54][1:].values.tolist()
    SSWsdev_list = df.iloc[55][1:].values.tolist()
    SSWskew_list = df.iloc[56][1:].values.tolist()    
    SW_list = df.loc[df['par'] == '% SW'].iloc[:,1:].values.tolist()[0]
    SWmean_list = df.iloc[58][1:].values.tolist()
    SWsdev_list = df.iloc[59][1:].values.tolist()
    SWskew_list = df.iloc[60][1:].values.tolist()      
    WSW_list = df.loc[df['par'] == '% WSW'].iloc[:,1:].values.tolist()[0]
    WSWmean_list = df.iloc[62][1:].values.tolist()
    WSWsdev_list = df.iloc[63][1:].values.tolist()
    WSWskew_list = df.iloc[64][1:].values.tolist()   
    W_list = df.loc[df['par'] == '% W'].iloc[:,1:].values.tolist()[0]
    Wmean_list = df.iloc[66][1:].values.tolist()
    Wsdev_list = df.iloc[67][1:].values.tolist()
    Wskew_list = df.iloc[68][1:].values.tolist()
    WNW_list = df.loc[df['par'] == '% WNW'].iloc[:,1:].values.tolist()[0]
    WNWmean_list = df.iloc[70][1:].values.tolist()
    WNWsdev_list = df.iloc[71][1:].values.tolist()
    WNWskew_list = df.iloc[72][1:].values.tolist()  
    NW_list = df.loc[df['par'] == '% NW'].iloc[:,1:].values.tolist()[0]
    NWmean_list = df.iloc[74][1:].values.tolist()
    NWsdev_list = df.iloc[75][1:].values.tolist()
    NWskew_list = df.iloc[76][1:].values.tolist()  
    NNW_list = df.loc[df['par'] == '% NNW'].iloc[:,1:].values.tolist()[0]
    NNWmean_list = df.iloc[78][1:].values.tolist()
    NNWsdev_list = df.iloc[79][1:].values.tolist()
    NNWskew_list = df.iloc[80][1:].values.tolist()      
    calm_list = df.loc[df['par'] == 'CALM'].iloc[:,1:].values.tolist()[0]
    
    meanP, sdevP, skewP, ww, wd = [], [], [], [], []
    tmax, tmin, sdtmax, sdtmin = [], [], [], []
    solrad, solsdev, mx5p, dewpt, timepk = [], [], [], [], []
    n, nmean, nsdev, nskew = [], [], [], []
    nne, nnemean, nnesdev, nneskew = [], [], [], []
    ne, nemean, nesdev, neskew = [], [], [], []
    ene, enemean, enesdev, eneskew = [], [], [], []
    e, emean, esdev, eskew = [], [], [], []    
    ese, esemean, esesdev, eseskew = [], [], [], []
    se, semean, sesdev, seskew = [], [], [], []
    sse, ssemean, ssesdev, sseskew = [], [], [], []
    s, smean, ssdev, sskew = [], [], [], []
    ssw, sswmean, sswsdev, sswskew = [], [], [], []
    sw, swmean, swsdev, swskew = [], [], [], []
    wsw, wswmean, wswsdev, wswskew = [], [], [], []
    w, wmean, wsdev, wskew = [], [], [], []
    wnw, wnwmean, wnwsdev, wnwskew = [], [], [], []
    nw, nwmean, nwsdev, nwskew = [], [], [], []
    nnw, nnwmean, nnwsdev, nnwskew = [], [], [], []
    calm = []
    
    for i in range(1, 13):
        meanP.append( '{:.2f}'.format( meanP_list[i-1] ).lstrip( '0' ) )
        sdevP.append( '{:.2f}'.format( sdevP_list[i-1] ).lstrip( '0' ) )
        skewP.append( '{:.2f}'.format( skewP_list[i-1] ).lstrip( '0' ) )
        ww.append( '{:.2f}'.format( ww_list[i-1] ).lstrip( '0' ) )
        wd.append( '{:.2f}'.format( wd_list[i-1] ).lstrip( '0' ) )
        tmax.append( '{:.2f}'.format( tmax_list[i-1] ).lstrip( '0' ) )
        tmin.append( '{:.2f}'.format( tmin_list[i-1] ).lstrip( '0' ) )
        sdtmax.append( '{:.2f}'.format( sdtmax_list[i-1] ).lstrip( '0' ) )
        sdtmin.append( '{:.2f}'.format( sdtmin_list[i-1] ).lstrip( '0' ) ) 
        solrad.append( '%.0f' %round(float(solrad_list[i-1]), 0) + '.' )
        solsdev.append( '%.1f' %round(float(solsdev_list[i-1]), 1) )
        mx5p.append( ('%.2f' %round(float(mx5p_list[i-1]), 2)).lstrip( '0' ) )
        dewpt.append( '%.2f' %round(float(dewpt_list[i-1]), 2) )
        timepk.append( ('%.3f' %round(float(timepk_list[i-1]), 3)).lstrip( '0' ) )
        
        n.append( '{:.2f}'.format( N_list[i-1] ).lstrip( '0' ) )
        nmean.append( '{:.2f}'.format( Nmean_list[i-1] ).lstrip( '0' ) ) 
        nsdev.append( '{:.2f}'.format( Nsdev_list[i-1] ).lstrip( '0' ) ) 
        nskew.append( '{:.2f}'.format( Nskew_list[i-1] ).lstrip( '0' ) ) 
    
        nne.append( '{:.2f}'.format( NNE_list[i-1] ).lstrip( '0' ) )
        nnemean.append( '{:.2f}'.format( NNEmean_list[i-1] ).lstrip( '0' ) ) 
        nnesdev.append( '{:.2f}'.format( NNEsdev_list[i-1] ).lstrip( '0' ) ) 
        nneskew.append( '{:.2f}'.format( NNEskew_list[i-1] ).lstrip( '0' ) ) 
    
        ne.append( '{:.2f}'.format( NE_list[i-1] ).lstrip( '0' ) )
        nemean.append( '{:.2f}'.format( NEmean_list[i-1] ).lstrip( '0' ) ) 
        nesdev.append( '{:.2f}'.format( NEsdev_list[i-1] ).lstrip( '0' ) ) 
        neskew.append( '{:.2f}'.format( NEskew_list[i-1] ).lstrip( '0' ) ) 
    
        ene.append( '{:.2f}'.format( ENE_list[i-1] ).lstrip( '0' ) )
        enemean.append( '{:.2f}'.format( ENEmean_list[i-1] ).lstrip( '0' ) ) 
        enesdev.append( '{:.2f}'.format( ENEsdev_list[i-1] ).lstrip( '0' ) ) 
        eneskew.append( '{:.2f}'.format( ENEskew_list[i-1] ).lstrip( '0' ) ) 
    
        e.append( '{:.2f}'.format( E_list[i-1] ).lstrip( '0' ) )
        emean.append( '{:.2f}'.format( Emean_list[i-1] ).lstrip( '0' ) ) 
        esdev.append( '{:.2f}'.format( Esdev_list[i-1] ).lstrip( '0' ) ) 
        eskew.append( '{:.2f}'.format( Eskew_list[i-1] ).lstrip( '0' ) ) 
    
        ese.append( '{:.2f}'.format( ESE_list[i-1] ).lstrip( '0' ) )
        esemean.append( '{:.2f}'.format( ESEmean_list[i-1] ).lstrip( '0' ) ) 
        esesdev.append( '{:.2f}'.format( ESEsdev_list[i-1] ).lstrip( '0' ) ) 
        eseskew.append( '{:.2f}'.format( ESEskew_list[i-1] ).lstrip( '0' ) ) 
    
        se.append( '{:.2f}'.format( SE_list[i-1] ).lstrip( '0' ) )
        semean.append( '{:.2f}'.format( SEmean_list[i-1] ).lstrip( '0' ) ) 
        sesdev.append( '{:.2f}'.format( SEsdev_list[i-1] ).lstrip( '0' ) ) 
        seskew.append( '{:.2f}'.format( SEskew_list[i-1] ).lstrip( '0' ) ) 
    
        sse.append( '{:.2f}'.format( SSE_list[i-1] ).lstrip( '0' ) )
        ssemean.append( '{:.2f}'.format( SSEmean_list[i-1] ).lstrip( '0' ) ) 
        ssesdev.append( '{:.2f}'.format( SSEsdev_list[i-1] ).lstrip( '0' ) ) 
        sseskew.append( '{:.2f}'.format( SSEskew_list[i-1] ).lstrip( '0' ) ) 
    
        s.append( '{:.2f}'.format( S_list[i-1] ).lstrip( '0' ) )
        smean.append( '{:.2f}'.format( Smean_list[i-1] ).lstrip( '0' ) ) 
        ssdev.append( '{:.2f}'.format( Ssdev_list[i-1] ).lstrip( '0' ) ) 
        sskew.append( '{:.2f}'.format( Sskew_list[i-1] ).lstrip( '0' ) ) 
    
        ssw.append( '{:.2f}'.format( SSW_list[i-1] ).lstrip( '0' ) )
        sswmean.append( '{:.2f}'.format( SSWmean_list[i-1] ).lstrip( '0' ) ) 
        sswsdev.append( '{:.2f}'.format( SSWsdev_list[i-1] ).lstrip( '0' ) ) 
        sswskew.append( '{:.2f}'.format( SSWskew_list[i-1] ).lstrip( '0' ) ) 
    
        sw.append( '{:.2f}'.format( SW_list[i-1] ).lstrip( '0' ) )
        swmean.append( '{:.2f}'.format( SWmean_list[i-1] ).lstrip( '0' ) ) 
        swsdev.append( '{:.2f}'.format( SWsdev_list[i-1] ).lstrip( '0' ) ) 
        swskew.append( '{:.2f}'.format( SWskew_list[i-1] ).lstrip( '0' ) ) 
    
        wsw.append( '{:.2f}'.format( WSW_list[i-1] ).lstrip( '0' ) )
        wswmean.append( '{:.2f}'.format( WSWmean_list[i-1] ).lstrip( '0' ) ) 
        wswsdev.append( '{:.2f}'.format( WSWsdev_list[i-1] ).lstrip( '0' ) ) 
        wswskew.append( '{:.2f}'.format( WSWskew_list[i-1] ).lstrip( '0' ) ) 
    
        w.append( '{:.2f}'.format( W_list[i-1] ).lstrip( '0' ) )
        wmean.append( '{:.2f}'.format( Wmean_list[i-1] ).lstrip( '0' ) ) 
        wsdev.append( '{:.2f}'.format( Wsdev_list[i-1] ).lstrip( '0' ) ) 
        wskew.append( '{:.2f}'.format( Wskew_list[i-1] ).lstrip( '0' ) ) 
    
        wnw.append( '{:.2f}'.format( WNW_list[i-1] ).lstrip( '0' ) )
        wnwmean.append( '{:.2f}'.format( WNWmean_list[i-1] ).lstrip( '0' ) ) 
        wnwsdev.append( '{:.2f}'.format( WNWsdev_list[i-1] ).lstrip( '0' ) ) 
        wnwskew.append( '{:.2f}'.format( WNWskew_list[i-1] ).lstrip( '0' ) ) 
    
        nw.append( '{:.2f}'.format( NW_list[i-1] ).lstrip( '0' ) )
        nwmean.append( '{:.2f}'.format( NWmean_list[i-1] ).lstrip( '0' ) ) 
        nwsdev.append( '{:.2f}'.format( NWsdev_list[i-1] ).lstrip( '0' ) ) 
        nwskew.append( '{:.2f}'.format( NWskew_list[i-1] ).lstrip( '0' ) ) 
    
        nnw.append( '{:.2f}'.format( NNW_list[i-1] ).lstrip( '0' ) )
        nnwmean.append( '{:.2f}'.format( NNWmean_list[i-1] ).lstrip( '0' ) ) 
        nnwsdev.append( '{:.2f}'.format( NNWsdev_list[i-1] ).lstrip( '0' ) ) 
        nnwskew.append( '{:.2f}'.format( NNWskew_list[i-1] ).lstrip( '0' ) ) 
    
        calm.append( '{:.2f}'.format( calm_list[i-1] ).lstrip( '0' ) )

    file = excelFile.strip( '.xlsx' )
    with open(os.path.join( outputFolder, file + '.par' ), 'w') as f_out: 
        
        title = df.iloc[0,0].strip( '\n' )
        yrsStr = df.iloc[1,4]
        tpStr = df.iloc[2,2]
        end_i = df[df.par == 'CALM'].index[0]
        if end_i < len(df) - 1:
            bottStr = df.iloc[end_i+1:,0].str.cat( sep='\n' ) + '\n'
        else:
            bottStr = '\n'
    
        lat, lon = df.iloc[1,1], df.iloc[1,3]
        lat, lon = '%.2f' % round(float(lat), 2), '%.2f' % round(float(lon), 2)
        elev = df.iloc[2,1]
        elev = '%.0f' % round(elev, 0) + '.'
    
        f_out.write( title + '\n' )
        f_out.write( ' LATT=' + formatting_obj.spacing_lat_lon( lat ) + lat )
        f_out.write( ' LONG=' + formatting_obj.spacing_lat_lon( lon ) + lon )
        f_out.write( ' ' + yrsStr + '\n' )
        f_out.write( ' ELEVATION =' + formatting_obj.spacing_elev( elev ) + elev )
        f_out.write( ' ' + tpStr + '\n' )
        
        gen = formatting_obj.spacing_gen_new( meanP )
        f_out.write( ' MEAN P ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(meanP)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sdevP )
        f_out.write( ' S DEV P' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sdevP)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( skewP )
        f_out.write( ' SKEW  P' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(skewP)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( ww )
        f_out.write( ' P(W/W) ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ww)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wd )
        f_out.write( ' P(W/D) ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wd)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( tmax )
        f_out.write( ' TMAX AV' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(tmax)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( tmin )
        f_out.write( ' TMIN AV' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(tmin)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sdtmax )
        f_out.write( ' SD TMAX' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sdtmax)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sdtmin )
        f_out.write( ' SD TMIN' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sdtmin)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( solrad )
        f_out.write( ' SOL.RAD' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(solrad)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( solsdev )
        f_out.write( ' SD SOL ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(solsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( mx5p )
        f_out.write( ' MX .5 P' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(mx5p)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( dewpt )
        f_out.write( ' DEW PT ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(dewpt)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( timepk )
        f_out.write( 'Time Pk ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(timepk)] ) + '\n' )
        
        gen = formatting_obj.spacing_gen_new( n )
        f_out.write( '% N     ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(n)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( nne )
        f_out.write( '% NNE   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nne)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nnemean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnemean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nnesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nneskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nneskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( ne )
        f_out.write( '% NE    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ne)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nemean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nemean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( neskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(neskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( ene )
        f_out.write( '% ENE   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ene)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( enemean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(enemean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( enesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(enesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( eneskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(eneskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( e )
        f_out.write( '% E     ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(e)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( emean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(emean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( esdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(esdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( eskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(eskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( ese )
        f_out.write( '% ESE   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ese)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( esemean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(esemean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( esesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(esesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( eseskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(eseskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( se )
        f_out.write( '% SE    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(se)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( semean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(semean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( seskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(seskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( sse )
        f_out.write( '% SSE   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sse)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( ssemean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ssemean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( ssesdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ssesdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sseskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sseskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( s )
        f_out.write( '% S     ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(s)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( smean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(smean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( ssdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ssdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( ssw )
        f_out.write( '% SSW   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(ssw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sswmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sswmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sswsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sswsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( sswskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sswskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( sw )
        f_out.write( '% SW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(sw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( swmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(swmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( swsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(swsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( swskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(swskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( wsw )
        f_out.write( '% WSW   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wsw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wswmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wswmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wswsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wswsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wswskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wswskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( w )
        f_out.write( '% W     ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(w)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( wnw )
        f_out.write( '% WNW   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wnw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wnwmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wnwmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wnwsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wnwsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( wnwskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(wnwskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( nw )
        f_out.write( '% NW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nwmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nwmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nwsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nwsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nwskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nwskew)] ) + '\n' )
    
        gen = formatting_obj.spacing_gen_new( nnw )
        f_out.write( '% NNW   ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnw)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nnwmean )
        f_out.write( 'MEAN    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnwmean)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nnwsdev )
        f_out.write( 'STD DEV ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnwsdev)] ) + '\n' )
        gen = formatting_obj.spacing_gen_new( nnwskew )
        f_out.write( 'SKEW    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(nnwskew)] ) + '\n' )
                                                                                                                                                                                   
        gen = formatting_obj.spacing_gen_new( calm )
        f_out.write( 'CALM    ' + ''.join( [next(gen) + str(x) + next(gen) if i < 1 else str(x) if i == 11 else str(x) + next(gen) for i, x in enumerate(calm)] ) + '\n' )    
        
        f_out.write( bottStr )
    
    return 0


for file in files:
    output = write_par( file, excelFolder, outputFolder )

