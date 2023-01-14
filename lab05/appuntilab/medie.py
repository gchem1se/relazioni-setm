import numpy as np

def dout(mis):
  A = 3.9083 * 10 ** (-3)
  B = -5.775 * 10 ** (-7)
  Rf = 976
  R0 = 100
  return ( (2**10) * (Rf) ) / ((R0*B)*( - (mis**2) - ((A**2) / (4 * (B**2))) - (A * mis / B) - ((A**2) / (4 * (B**2))) ) + (R0) + (Rf) )

misure = [
    26.54,
    23.50,
    23.50,
    23.50,
    23.50,
    23.50,
    23.50,
    23.50,
    23.50,
    26.54,
    23.50,
    23.50,
    23.50,
    23.50,
    23.50,
    26.54,
    26.54,
    26.54,
    23.50,
    23.50
]


totmis = 0
totunc = 0
for mis in misure:
    print("{}, Dout = {}".format(mis, dout(mis)))

print("---")