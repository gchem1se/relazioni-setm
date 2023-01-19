import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import json

def toDb(value):
    return 20*np.log10(value)

def toDeg(value, frequency, uncert):
    # uncert === sensitivity here
    # e["value_deg"] = ((360 * e["value"] / (5*e["uncert"])) / ((1 / e["frequency"]) / (5*e["uncert"]))) / 1000000
    # e["uncert_deg"] = ((360 * 1/5) / ((1 / e["frequency"]) / (5*e["uncert"]))) / 1000000
    return (((360 * value) / ((1 / frequency) / (5*uncert))) / 1000000)

def toLatexTable(entries, caption):
    row_format = "|c" * len(entries[0])
    row_format+="|"

    table = \
"\\begin{{table}}[H]\n\
\t\\makebox[\\textwidth][c]{{\n\
\t\t\\begin{{tabular}}{{{row_format}}}\n\
\t\t\t\\hline\n\
\t\t\t{table_body}\
\t\t\\end{{tabular}}\n\t}}\n\
\t\\caption{{{caption}}}\n\
\\end{{table}}\n"

    table_body = ""
    i = 0
    for i in range(len(entries)):
        j = 0

        for j in range(len(entries[i])):
            entry = " & ".join([str(x) for x in entries[i]])
        entry+="\\\\\n\t\t\t\\hline\n\t\t\t"

        if i == len(entries) - 1: 
            entry = entry[:-3]
        
        table_body += entry

    table = table.format(row_format=row_format, table_body=table_body, caption=caption)

    return table
    
def Bode(x, y, **kwargs):
    err = kwargs.get("err", [])
    cutoff = kwargs.get("cutoff", None)    
    cutoff_err = kwargs.get("cutoff_err", None)
    toPlot = kwargs.get("toPlot", None)
    fig, axs = plt.subplots(1)
    axs.plot(x, y, '-ok')
    axs.set_yscale("linear")
    axs.set_xscale("log")
    axs.grid(visible=True, which='major', axis='both')
    if len(err) != 0:
        axs.errorbar(x, y, yerr=err, color='k')
    if cutoff != None:
        axs.axvline(x = cutoff, ls='--', color='r')        
        axs.axvline(x = cutoff-cutoff_err, ls='--', color='r')
        axs.axvline(x = cutoff+cutoff_err, ls='--', color='r')
        axs.axvspan(cutoff-cutoff_err, cutoff+cutoff_err, alpha=0.3, color='red')
    if toPlot == "module":
        axs.axhline(y = -3, ls='--', color='r')
    else:
        axs.axvline(x = cutoff/10, ls='--', color='r')
        axs.axvline(x = (cutoff-cutoff_err)/10, ls='--', color='r')
        axs.axvline(x = (cutoff+cutoff_err)/10, ls='--', color='r')

        axs.axvline(x = cutoff*10, ls='--', color='r')
        axs.axvline(x = (cutoff-cutoff_err)*10, ls='--', color='r')
        axs.axvline(x = (cutoff+cutoff_err)*10, ls='--', color='r')

        axs.axvspan((cutoff-cutoff_err)/10, (cutoff+cutoff_err)*10, alpha=0.1, color='red')
        
    for i, txt in enumerate(y):
        axs.annotate("  "+str(round(float(txt), 2)), (x[i], y[i]+0.6))

    plt.show()

