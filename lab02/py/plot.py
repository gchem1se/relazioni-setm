from utilities import *
from pprint import pprint

FILEPATH = "valori.json"

### questi sono rimasti fissi
VIN = 880
VIN_UNCERT = 80
###

if (input("che filtro vuoi? (0:lowpass, 1:highpass)\n> ")) == str(0):
    FILTER = "low_pass"
else:
    FILTER = "high_pass"
if (input("che plot vuoi? (0:module, 1:phasedelta)\n> ")) == str(0):
    TOPLOT = "module"
else:
    TOPLOT = "phase_delta"

# -------- #

def get_data(filepath, myfilter, mytoplot):
    f = open(FILEPATH, "r")   
    d = json.load(f)
    f.close()

    # preparing data
    for entry in d[myfilter]["samples"][mytoplot]:
        entry["frequency"] = float(entry["frequency"])
        entry["value"] = float(entry["value"])
        entry["uncert"] = float(entry["uncert"])
        entry["avg_on"] = int(entry["avg_on"])

    if mytoplot == "module":
        # create dB fields
        for e in d[myfilter]["samples"][mytoplot]:
            e["transfer"] = e["value"] / VIN # transfer function
            e["transfer_dB"] = 20*np.log10(e["transfer"]) # = 20log10(Vout/Vin)
            e["transfer_uncert"] = np.abs(1/VIN)*e["uncert"]+np.abs(-e["value"]/(VIN**2))*VIN_UNCERT # deterministic model formula
            # asymmetric errors
            e["transfer_uncert_dB_up"] =  np.abs(
                    toDb(e["transfer"]+e["transfer_uncert"]) - toDb(e["transfer"])
            )
            e["transfer_uncert_dB_down"] = np.abs(
                    toDb(e["transfer"]) - toDb(e["transfer"]-e["transfer_uncert"])
            )
    else:
        # create degrees fields
        for e in d[myfilter]["samples"][mytoplot]:
            e["value_deg"] = toDeg(np.abs(e["value"]) / (5*e["uncert"]), e["frequency"], e["uncert"])
            e["uncert_deg"] = toDeg(1/5, e["frequency"], e["uncert"])

    return float(d[myfilter]["cutoff_frequency"]["value"]), float(d[myfilter]["cutoff_frequency"]["uncert"]), d[myfilter]["samples"][mytoplot]

# -------- #

cutoff, cutoff_err, samples = get_data(FILEPATH, FILTER, TOPLOT)

if TOPLOT == "module":
    x = np.array([x["frequency"] for x in samples])
    y = np.array([x["transfer_dB"] for x in samples])
    err = [
        np.array([x["transfer_uncert_dB_down"] for x in samples]),
        np.array([x["transfer_uncert_dB_up"] for x in samples])
    ]
else:
    x = np.array([x["frequency"] for x in samples])
    y = np.array([x["value_deg"] for x in samples])
    err = np.array([x["uncert_deg"] for x in samples])

Bode(x, y, err=err, cutoff=cutoff, cutoff_err=cutoff_err, toPlot=TOPLOT) # wrapper for matplotlib, semilogarithmic graphing and shit 
