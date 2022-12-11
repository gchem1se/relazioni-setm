from utilities import *

FILEPATH = "valori.json"

def lab02LatexTable(file, filter_pass):
    file.seek(0,0)
    data = json.loads(file.read())[filter_pass]["samples"]
    
    entries = [] 
    for i in range(len(data["module"])):
        entry = []
        entry.append(data["module"][i]["frequency"])
        entry.append("$880\\pm 80$")
        entry.append("${}\\pm{}$".format(data["module"][i]["value"], data["module"][i]["uncert"]))
        entry.append("${}\\pm{}$".format(
            np.abs(round(toDeg(
                (float(data["phase_delta"][i]["value"]) / (5*float(data["phase_delta"][i]["uncert"]))), 
                float(data["phase_delta"][i]["frequency"]), 
                float(data["phase_delta"][i]["uncert"])
            ), 2)), 
            round(toDeg(
                1/5,
                float(data["phase_delta"][i]["frequency"]),
                float(data["phase_delta"][i]["uncert"])
            ), 2),
        ))
        entry.append(str(round(toDb(float(data["module"][i]["value"]) / 880), 2)))
        entries.append(entry)

    return toLatexTable(entries, filter_pass)

with open(FILEPATH, "r") as file:   
    print("LOW_PASS\n--------------------------")
    print(lab02LatexTable(file, "low_pass"))
    print("HIGH_PASS\n--------------------------")
    print(lab02LatexTable(file, "high_pass"))
