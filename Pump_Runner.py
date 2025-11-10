# File Name: <Pump_Runner.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

# Imports
from Part_Runner import runParts

# Pump data
pumps = [
    {"name": "Cheap", "options": [
        {"length": 6, "cost": 200000, "efficiency": 0.80},
        {"length": 9, "cost": 220000, "efficiency": 0.80},
        {"length": 12, "cost": 240000, "efficiency": 0.80},
        {"length": 15, "cost": 260000, "efficiency": 0.80},
        {"length": 18, "cost": 290000, "efficiency": 0.80},
        {"length": 21, "cost": 320000, "efficiency": 0.80},
        {"length": 24, "cost": 350000, "efficiency": 0.80},
        {"length": 27, "cost": 390000, "efficiency": 0.80},
        {"length": 30, "cost": 420000, "efficiency": 0.80},
        {"length": 33, "cost": 470000, "efficiency": 0.80},
        {"length": 36, "cost": 510000, "efficiency": 0.80},
    ]},
    {"name": "Value", "options": [
        {"length": 6, "cost": 240000, "efficiency": 0.83},
        {"length": 9, "cost": 260000, "efficiency": 0.83},
        {"length": 12, "cost": 290000, "efficiency": 0.83},
        {"length": 15, "cost": 310000, "efficiency": 0.83},
        {"length": 18, "cost": 350000, "efficiency": 0.83},
        {"length": 21, "cost": 380000, "efficiency": 0.83},
        {"length": 24, "cost": 420000, "efficiency": 0.83},
        {"length": 27, "cost": 460000, "efficiency": 0.83},
        {"length": 30, "cost": 510000, "efficiency": 0.83},
        {"length": 33, "cost": 560000, "efficiency": 0.83},
        {"length": 36, "cost": 620000, "efficiency": 0.83},
    ]},
    {"name": "Standard", "options": [
        {"length": 6, "cost": 280000, "efficiency": 0.86},
        {"length": 9, "cost": 310000, "efficiency": 0.86},
        {"length": 12, "cost": 340000, "efficiency": 0.86},
        {"length": 15, "cost": 380000, "efficiency": 0.86},
        {"length": 18, "cost": 420000, "efficiency": 0.86},
        {"length": 21, "cost": 460000, "efficiency": 0.86},
        {"length": 24, "cost": 510000, "efficiency": 0.86},
        {"length": 27, "cost": 560000, "efficiency": 0.86},
        {"length": 30, "cost": 610000, "efficiency": 0.86},
        {"length": 33, "cost": 670000, "efficiency": 0.86},
        {"length": 36, "cost": 740000, "efficiency": 0.86},
    ]},
    {"name": "High-Grade", "options": [
        {"length": 6, "cost": 340000, "efficiency": 0.89},
        {"length": 9, "cost": 380000, "efficiency": 0.89},
        {"length": 12, "cost": 410000, "efficiency": 0.89},
        {"length": 15, "cost": 460000, "efficiency": 0.89},
        {"length": 18, "cost": 500000, "efficiency": 0.89},
        {"length": 21, "cost": 550000, "efficiency": 0.89},
        {"length": 24, "cost": 610000, "efficiency": 0.89},
        {"length": 27, "cost": 670000, "efficiency": 0.89},
        {"length": 30, "cost": 740000, "efficiency": 0.89},
        {"length": 33, "cost": 810000, "efficiency": 0.89},
        {"length": 36, "cost": 890000, "efficiency": 0.89},
    ]},
    {"name": "Premium", "options": [
        {"length": 6, "cost": 415000, "efficiency": 0.92},
        {"length": 9, "cost": 456000, "efficiency": 0.92},
        {"length": 12, "cost": 502000, "efficiency": 0.92},
        {"length": 15, "cost": 552000, "efficiency": 0.92},
        {"length": 18, "cost": 607000, "efficiency": 0.92},
        {"length": 21, "cost": 668000, "efficiency": 0.92},
        {"length": 24, "cost": 735000, "efficiency": 0.92},
        {"length": 27, "cost": 808000, "efficiency": 0.92},
        {"length": 30, "cost": 889000, "efficiency": 0.92},
        {"length": 33, "cost": 978000, "efficiency": 0.92},
        {"length": 36, "cost": 1076000, "efficiency": 0.92},
    ]},
]

def getPumpValue(name, length, key):
    for pump in pumps:
        if pump["name"] == name:
            for option in pump["options"]:
                if option["length"] == length:
                    return option.get(key)
    return None

def runPumps(currStep, currCosts, segmentVals, currMaxVal, currMaxSegVals):
    step = currStep
    costs = currCosts
    maxVal = currMaxVal
    maxSegVals = currMaxSegVals
    
    for p in pumps:
        pname = p["name"]
        length = 9
        costs[1][0] = getPumpValue(pname, length, "cost") * segmentVals[0][4]
        etaPump = getPumpValue(pname, length, "efficiency")
            
        segmentVals[1] = [etaPump]
        [step, maxVal, maxSegVals] = runParts(step, costs, segmentVals, maxVal, maxSegVals)
        # print("Working2:", step)
    return [step, maxVal, maxSegVals]