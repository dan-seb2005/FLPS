import json
import sys
 
OFFSET = 24000  # 24 segundos en milisegundos
 
with open("input.json", "r") as f:
    data = json.load(f)
 
for section in data["song"]["notes"]:
    for note in section["sectionNotes"]:
        note[0] += OFFSET
 
for event in data["song"]["events"]:
    event[0] += OFFSET
 
with open("output.json", "w") as f:
    json.dump(data, f, indent="\t")
 
print("Listo! Chart guardado en output.json")
 