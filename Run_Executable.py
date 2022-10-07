#==============================================================================
#Runs CLIGEN for all par files in a directory
#==============================================================================

from shutil import copyfile
import subprocess as sub
import os


# =============================================================================
# Manually enter directory paths below
# =============================================================================
cligenFolder = r'...\cligenv53'
parFolder = r'...\parFolder'
outputFolder = r'...\outputFolder'
consoleFolder = r'...\consoleFolder'

REC_LEN = 300

parFiles = os.listdir( parFolder )


def run_cligen( parFile, cligenDir, parDir, outputDir, consoleDir ):

    error_file = []

    # =========================================================================
    # copy parfile to cligen directory
    # =========================================================================
    copyfile( os.path.join( parDir, parFile ), os.path.join( cligenDir, parFile ) )

    args = 'cligen53 -b1 -y{} -t5 -i{} -o{}'.format( REC_LEN, parFile, parFile.strip( '.par' ) + '.txt' )
    with open(os.path.join( consoleDir, parFile.strip( '.par' ) + '.txt' ), 'w+') as f_out:
    
        try:
            result = sub.run( args=args, check=True, capture_output=True, text=True, shell=True, cwd=cligenDir )
            # =========================================================================
            # remove parfile after it's been run
            # =========================================================================
            os.remove( os.path.join( cligenDir + '\\' + parFile ) )
        
            # =========================================================================
            # copy output to output folder and remove output to cligen directory
            # =========================================================================
            copyfile( os.path.join( cligenDir, parFile.strip( '.par' ) + '.txt' ), 
                      os.path.join( outputDir, parFile.strip( '.par' ) + '.txt' ) )
        
            os.remove( os.path.join( cligenDir, parFile.strip( '.par' ) + '.txt' ) )
        
            f_out.write( result.stdout )
            f_out.write( result.stderr )
        
        except sub.CalledProcessError:
            # =========================================================================
            # remove parfile after it's been run
            # =========================================================================
            os.remove( os.path.join( cligenDir, parFile ) )
                    
            error_file.append( parFile )

    return error_file


run_ct = 0
error_files = []
for file in parFiles:
    output = run_cligen( file, cligenFolder, parFolder, outputFolder, consoleFolder )
    run_ct += 1
    print(str(run_ct) + ' / ' + str(len(parFiles)))
    error_files.extend( output )


print('error files:\n', error_files)
