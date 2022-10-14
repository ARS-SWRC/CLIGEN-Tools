#==============================================================================
#Runs the International CLIGEN Conversion Tool.
#Takes the first 12 lines of par files and 
#finds similar stations to take the remaining parameters from. 
#Makes new par files from the parameters.
#==============================================================================

from subprocess import Popen, PIPE
import shutil
import os

# =============================================================================
# Manually enter directory paths below
# =============================================================================
parFolder = r'...\parFolder'
outputFolder = r'...\outputFolder'
intlFolder = r'...\international'

parFiles = os.listdir( parFolder )
topFiles = [file.strip( '.par' ) + '.top' for file in parFiles]


def make_tops( parFile, topFile, parDir, intlDir ):
    with open(os.path.join( parDir, parFile )) as f_in:
        lines = f_in.readlines()
    with open(os.path.join( intlDir, topFile ), 'w') as f_out:
        for line in lines[:12]:
            f_out.write( line )
    return 0

def run_intl( topFile ):
    p = Popen( ['FindMatch'], cwd=intlFolder, stdin=PIPE, stdout=PIPE, shell=True )
    p.communicate( bytes(topFile + '\r\n\r\n', 'utf-8') )
    return 0

def clear_files( parFile, topFile, parDir, intlDir, outputDir ):
    os.remove( os.path.join( intlDir, topFile ) )        
    shutil.copyfile( os.path.join( intlDir, parFile ), os.path.join( outputDir, parFile ) )
    os.remove( os.path.join( intlDir, parFile ) )        
    return 0
    
for i, file in enumerate(parFiles):
    output = make_tops( parFiles[i], topFiles[i], parFolder, intlFolder )
    output = run_intl( topFiles[i] )
    output = clear_files( parFiles[i], topFiles[i], parFolder, intlFolder, outputFolder )

