
from shutil import copyfile
import subprocess as sub
import os

# =============================================================================
# Manually enter directory paths below
# =============================================================================
cligenFolder = r'...\cligenv53'
parFolder = r'...\pars'
outputFolder = r'...\ouputs'
consoleFolder = r'...\cons'

REC_LEN = 30

parFiles = os.listdir(parFolder)


failed_files = []

def run_file(parfile):

  # =========================================================================
  # copy parfile to cligen directory
  # =========================================================================
  copyfile(os.path.join(parFolder, parfile), os.path.join(cligenFolder, parfile))

  print(parfile)

  args = 'cligen53 -b1 -y{} -t5 -i{} -o{}'.format(REC_LEN, parfile, parfile[:-4] + '.txt')

  with open(os.path.join(consoleFolder, parfile[:-4] + '.txt'), 'w') as f_out:
  
    try:
      result = sub.run(args=args, check=True, capture_output=True, text=True, shell=True, cwd=cligenFolder)
      # =========================================================================
      # remove parfile after it's been run
      # =========================================================================
      os.remove(os.path.join(cligenFolder, parfile))
      # =========================================================================
      # copy output to output folder and remove output to cligen directory
      # =========================================================================
      copyfile(os.path.join(cligenFolder, parfile[:-4] + '.txt'),
               os.path.join(outputFolder, parfile[:-4] + '.txt'))
  
      os.remove(os.path.join(cligenFolder, parfile[:-4] + '.txt'))
  
      f_out.write(result.stdout)
      f_out.write(result.stderr)
  
    except sub.CalledProcessError:
      # =========================================================================
      # remove parfile after it's been run
      # =========================================================================
      os.remove(os.path.join(cligenFolder, parfile))
      
      failed_files.append(parfile)

  return None


for f in parFiles:
  run_file(f)

print(len(failed_files))
print(failed_files)
