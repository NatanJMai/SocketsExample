def abort(msg):
   print(msg)
   exit()

def read(line):
   spl = line.split()
   return float(spl[1]) * float(spl[2]) if len(spl) >= 3 else 0.0