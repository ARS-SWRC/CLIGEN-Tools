inFolder = r'...\tseries'
outFolder = r'...\RHEM_formatted'

inFiles = os.listdir(inFolder)

for f in inFiles:
  inFILE = os.path.join(inFolder, f)
  outFILE = os.path.join(outFolder, f)

  with open(inFILE) as f:
    lines = f.readlines()

  save_lines = []
  event_ct = 0
  for line in lines[15:-1]:
    row = line.split()
    pr = float(row[3])
    if pr > 0:
      event_ct += 1
      id = str(event_ct).ljust(6)
      dy = row[0].ljust(6)
      mo = row[1].ljust(6)
      yr = row[2].ljust(6)
      pr = row[3].ljust(6)
      dr = row[4].ljust(7)
      tp = row[5].ljust(7)
      ip = row[6]
      save_lines.append(''.join([id, dy, mo, yr, pr, dr, tp, ip]))


  with open(outFILE, 'w') as fo:
    fo.write(str(event_ct) + '\n')
    fo.write('0\n')
    fo.write('#  id     day  month  year  Rain   Dur    Tp     Ip\n')
    fo.write('#                           (mm)   (h)\n')
    for line in save_lines:
      fo.write('    ' + line + '\n')

