import numpy as np

def inc(mis):
    return 0.3+0.005*np.abs(mis)

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
    totmis+=mis
    totunc+=inc(mis)
    print("{}+-{}".format(mis, inc(mis)))

print("---")
print("{}+-{}".format(totmis/len(misure), totunc/len(misure)))