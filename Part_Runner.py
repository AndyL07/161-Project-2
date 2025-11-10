# File Name: <Part_Runner.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Model import runModel

pipes = [
    {"name": "Salvage", "options": [
        {"diameter": 0.10, "cost": 1000, "darcy": 0.05},
        {"diameter": 0.11, "cost": 1200, "darcy": 0.03},
        {"diameter": 0.12, "cost": 2570, "darcy": 0.02},
        {"diameter": 0.13, "cost": 6300, "darcy": 0.01},
        {"diameter": 0.14, "cost": 26000, "darcy": 0.005},
        {"diameter": 0.15, "cost": 37000, "darcy": 0.002},
    ]},
    {"name": "Questionable", "options": [
        {"diameter": 0.10, "cost": 1200, "darcy": 0.05},
        {"diameter": 0.11, "cost": 1440, "darcy": 0.03},
        {"diameter": 0.12, "cost": 3080, "darcy": 0.02},
        {"diameter": 0.13, "cost": 7560, "darcy": 0.01},
        {"diameter": 0.14, "cost": 31000, "darcy": 0.005},
        {"diameter": 0.15, "cost": 31000, "darcy": 0.002},
    ]},
    {"name": "Better", "options": [
        {"diameter": 0.10, "cost": 1440, "darcy": 0.02},
        {"diameter": 0.11, "cost": 1720, "darcy": 0.02},
        {"diameter": 0.12, "cost": 3700, "darcy": 0.02},
        {"diameter": 0.13, "cost": 9070, "darcy": 0.01},
        {"diameter": 0.14, "cost": 37000, "darcy": 0.005},
        {"diameter": 0.15, "cost": 37000, "darcy": 0.002},
    ]},
    {"name": "Nice", "options": [
        {"diameter": 0.10, "cost": 2160, "darcy": 0.01},
        {"diameter": 0.11, "cost": 2580, "darcy": 0.01},
        {"diameter": 0.12, "cost": 5550, "darcy": 0.01},
        {"diameter": 0.13, "cost": 14000, "darcy": 0.01},
        {"diameter": 0.14, "cost": 55000, "darcy": 0.005},
        {"diameter": 0.15, "cost": 55000, "darcy": 0.002},
    ]},
    {"name": "Outstanding", "options": [
        {"diameter": 0.10, "cost": 2700, "darcy": 0.005},
        {"diameter": 0.11, "cost": 3230, "darcy": 0.005},
        {"diameter": 0.12, "cost": 6940, "darcy": 0.005},
        {"diameter": 0.13, "cost": 17000, "darcy": 0.005},
        {"diameter": 0.14, "cost": 69000, "darcy": 0.005},
        {"diameter": 0.15, "cost": 69000, "darcy": 0.002},
    ]},
    {"name": "Glorious", "options": [
        {"diameter": 0.10, "cost": 2970, "darcy": 0.002},
        {"diameter": 0.11, "cost": 3550, "darcy": 0.002},
        {"diameter": 0.12, "cost": 7640, "darcy": 0.002},
        {"diameter": 0.13, "cost": 19000, "darcy": 0.002},
        {"diameter": 0.14, "cost": 76000, "darcy": 0.002},
        {"diameter": 0.15, "cost": 76000, "darcy": 0.002},
    ]}
]

valves = [
    {"name": "Salvage", "options": [
        {"diameter": 0.10, "cost": 100, "flowCoeff": 800},
        {"diameter": 0.11, "cost": 120, "flowCoeff": 800},
        {"diameter": 0.12, "cost": 257, "flowCoeff": 800},
        {"diameter": 0.13, "cost": 630, "flowCoeff": 800},
        {"diameter": 0.14, "cost": 1400, "flowCoeff": 800},
        {"diameter": 0.15, "cost": 2600, "flowCoeff": 800},
    ]},
    {"name": "Questionable", "options": [
        {"diameter": 0.10, "cost": 120, "flowCoeff": 700},
        {"diameter": 0.11, "cost": 144, "flowCoeff": 700},
        {"diameter": 0.12, "cost": 308, "flowCoeff": 700},
        {"diameter": 0.13, "cost": 756, "flowCoeff": 700},
        {"diameter": 0.14, "cost": 1600, "flowCoeff": 700},
        {"diameter": 0.15, "cost": 3100, "flowCoeff": 700},
    ]},
    {"name": "Outstanding", "options": [
        {"diameter": 0.10, "cost": 270, "flowCoeff": 600},
        {"diameter": 0.11, "cost": 323, "flowCoeff": 600},
        {"diameter": 0.12, "cost": 694, "flowCoeff": 600},
        {"diameter": 0.13, "cost": 1700, "flowCoeff": 600},
        {"diameter": 0.14, "cost": 3700, "flowCoeff": 600},
        {"diameter": 0.15, "cost": 6900, "flowCoeff": 600},
    ]},
    {"name": "Glorious", "options": [
        {"diameter": 0.10, "cost": 297, "flowCoeff": 500},
        {"diameter": 0.11, "cost": 355, "flowCoeff": 500},
        {"diameter": 0.12, "cost": 764, "flowCoeff": 500},
        {"diameter": 0.13, "cost": 1900, "flowCoeff": 500},
        {"diameter": 0.14, "cost": 4000, "flowCoeff": 500},
        {"diameter": 0.15, "cost": 7600, "flowCoeff": 500},
    ]}
]

def getPipeValue(name, diameter, key):
    for pipe in pipes:
        if pipe["name"] == name:
            for option in pipe["options"]:
                if option["diameter"] == diameter:
                    return option.get(key)
    return None

def getValveValue(name, diameter, key):
    for valve in valves:
        if valve["name"] == name:
            for option in valve["options"]:
                if option["diameter"] == diameter:
                    return option.get(key)
#<<<<<<< Updated upstream
    return None

def runParts(currStep, currCost, segmentVals, currMaxVal, currMaxSegVals, currMaxSite):
    step = currStep
    costs = currCost
    maxVal = currMaxVal
    maxSegVals = currMaxSegVals
    maxSite = currMaxSite
    
    diameters = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
    
    for diameter in diameters:
        for pi in pipes:
            piname = pi["name"]
            costs[2][0] = getPipeValue(piname, diameter, "cost")
            frictFact = getPipeValue(piname, diameter, "darcy")
                
            for v in valves:
                vname = v["name"]
                costs[2][1] = getValveValue(vname, diameter, "cost")
                valCoeff = getValveValue(vname, diameter, "flowCoeff")
                
                partLoop = [diameter, frictFact, valCoeff]
                segmentVals[2] = partLoop
                
                site = 2
                
                val = runModel(segmentVals, costs, site, False)
                
                step += 1
                
                if val > maxVal:
                    maxVal = val
                    maxSite = site
                    
                    listNum = 0
                    entryNum = 0
                    
                    for lists in segmentVals:
                        for entry in lists:
                            maxSegVals[listNum][entryNum] = segmentVals[listNum][entryNum]
                            entryNum += 1
                        entryNum = 0
                        listNum += 1
                    for i in range(4):
                        maxSegVals[0][i] = maxSegVals[0][i].getEta()
                    print(f"New Max Val: {maxVal:}")
                    print(maxSegVals)
                    
# print(max)
    return [step, maxVal, maxSegVals, maxSite]