# =============================================================================
# Creates tab delimited text file from a *.par file that can be properly imported 
# into an Excel spreadsheet. Also makes Excel workbook using Pandas.
# =============================================================================

import pandas as pd
import string
import os

# =============================================================================
# Manually enter directory paths below
# =============================================================================
parFolder = r'...\parFolder'
delimitedFolder = r'...\delimitedFolder'
excelFolder = r'...\excelFolder'

parFiles = os.listdir( parFolder )


def delimit_parFile( parFile, parDir, delimitedDir, excelDir ):
    
    with open(os.path.join( parDir, parFile )) as f_in:
        lines = f_in.readlines()

    for i, line in enumerate(lines):
        if line[:4] == 'CALM':
            bott_skip_lines = len(lines) - i - 1
    
    with open(os.path.join( delimitedDir, parFile.strip( '.par' ) + '.txt' ), 'w') as f_out:    
    
        top_skip_lines = 3    
    
        all_lbl_chars = ((string.punctuation + string.ascii_letters)           \
                         .replace( '.', '' ))                                  \
                         .replace( '-', '' )
    
        for i, line in enumerate(lines):
    
            if i < top_skip_lines:
                
                if i == 1:            
                    row = line.split( '=' )
                    lat = row[1].split()[0]
                    lon = row[2].split()[0]                
                    asIs_i = line.index( 'Y' )
                    f_out.write( '\t'.join( ['LATT', lat, 'LONG', lon, line[asIs_i:]] ) )
                
                elif i == 2:
                    row = line.split( '=' )
                    elev = row[1].split()[0]
                    asIs_i = line.index( 'P' ) - 1
                    f_out.write( '\t'.join( ['ELEVATION', elev, line[asIs_i:]] ) )
    
                else:
                    f_out.write( line )
    
            else:
                pass
    
            if i > top_skip_lines - 1 and i < len(lines) - bott_skip_lines:
        
                for j, elem in enumerate(line):
                    
                    if elem in all_lbl_chars: 
                        label_end_i = j
                    
                    else:
                        pass
    
                label = line[:label_end_i+1]
                label = label.strip()
    
                f_out.write( label + '\t' )

                dataline = line[8:]
                row = [dataline[k*6:k*6+6] for k in range(0,12)]
                print(row)
                print(len(row))

                for j, elem in enumerate(row):

                    if j < len(row)-1:
                        f_out.write( elem + '\t' )
                    
                    elif j == len(row) - 1:
                        f_out.write( elem + '\n' )
                        
                    else:
                        pass
    
            else:
                pass
    
            if i > len(lines) - bott_skip_lines - 1:
                f_out.write( line )
            else:
                pass
    
    df = pd.read_csv( os.path.join( delimitedDir, parFile.strip( '.par' ) + '.txt' ), sep='\t', 
                      names=list(range(13)), header=None, index_col=False, 
                      skip_blank_lines=False, dtype=str )
    
    excelFile = parFile.strip( '.par' ) + '.xlsx'
    
    df.to_excel( os.path.join( excelDir, excelFile ), columns=None, 
                  header=False, index=False )
    
    return 0


run_ct = 0
for file in parFiles:
    output = delimit_parFile( file, parFolder, delimitedFolder, excelFolder )
    run_ct += 1
    print(str(run_ct) + ' / ' + str(len(parFiles)))
