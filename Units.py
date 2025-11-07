# File Name: <Units.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

# Value table
[[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]]], [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]], [[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]], [[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]]]

# Imports
from Slurry import Slurry
from Fermenter import Fermenter
from Filtration import Filtration
from Distiller import Distiller
from Dehydrator import Dehydrator

# Unit data
fermenters = [
    {"name": "Scrap", "efficiency": 0.5, "cost": 320000, "energy": 46600},
    {"name": "Average", "efficiency": 0.75, "cost": 380000, "energy": 47200},
    {"name": "Premium", "efficiency": 0.9, "cost": 460000, "energy": 47500},
    {"name": "World-class", "efficiency": 0.95, "cost": 1100000, "energy": 48000},
]

distillers = [
    {"name": "Scrap", "efficiency": 0.81, "cost": 390000, "energy": 47004},
    {"name": "Average", "efficiency": 0.9, "cost": 460000, "energy": 47812},
    {"name": "Premium", "efficiency": 0.915, "cost": 560000, "energy": 48200},
    {"name": "World-class", "efficiency": 0.98, "cost": 1370000, "energy": 49500},
]

materialRemoval = [
    {"name": "Scrap", "efficiency": 0.5, "cost": 200000, "energy": 48800},
    {"name": "Average", "efficiency": 0.75, "cost": 240000, "energy": 49536},
    {"name": "Premium", "efficiency": 0.9, "cost": 280000, "energy": 50350},
    {"name": "World-class", "efficiency": 0.98, "cost": 480000, "energy": 51000},
]

# Getter functions
def getFermenterValue(name, key):
    for item in fermenters:
        if item["name"] == name:
            return item.get(key)
    return None

def getDistillerValue(name, key):
    for item in distillers:
        if item["name"] == name:
            return item.get(key)
    return None

def getMaterialRemovalValue(name, key):
    for item in materialRemoval:
        if item["name"] == name:
            return item.get(key)
    return None

# Initializae loop variables
printUnits = False
fermRun = 0
filtRun = 0
distRun = 0
dehyRun = 0
values = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(4)] for m in range()

# Loop
for f in fermenters:
    fermRun += 1
    distRun = 0
    
    efficiency = 0
    cost = 0
    
    fname = f["name"]
    etaFerm = getFermenterValue(fname, "efficiency")
    cost += getFermenterValue(fname, "cost")
    
    for d in distillers:
        distRun += 1
        dehyRun = 0
        
        dname = d["name"]
        etaDist = getDistillerValue(dname, "efficiency")
        cost += getDistillerValue(dname, "cost")
        
        for dehyd in materialRemoval:
            dehyRun += 1
            filtRun = 0
            
            dehydname = dehyd["name"]
            etaDehy = getMaterialRemovalValue(dehydname, "efficiency")
            cost += getMaterialRemovalValue(dehydname, "cost")
            
            for m in materialRemoval:
                filtRun += 1
                
                mname = m["name"]
                etaFilt = getMaterialRemovalValue(mname, "efficiency")
                cost += getMaterialRemovalValue(mname, "cost")
                
                # Initializing objects
                volFlowRate = 0.04
                slurry = Slurry(0.0, 0.20, 0.60, 0.20, volFlowRate)
                ferm = Fermenter(etaFerm, 46600, printUnits)
                filt = Filtration(etaFilt, 48800, printUnits)
                dist = Distiller(etaDist, 47004, printUnits)
                dehy = Dehydrator(etaDehy, 48800, printUnits)
                
                # Running Model
                ferm.ferment(slurry)
                filt.filt(slurry)
                dist.distill(slurry)
                dehy.dehydrate(slurry)
                
                # Data
                purity = slurry.getPurity()
                if purity >= 0.98:
                    values[fermRun - 1][filtRun - 1][distRun - 1][dehyRun - 1] = 1
                
                # Print values
                print("\n--------------------------------------------")
                print("Fermenter:", fermRun, fname)
                print("Filter:", filtRun, mname)
                print("Distiller:", distRun, dname)
                print("Dehydrator:", dehyRun, dehydname)
                print("Purity:", purity)
                print()
                print(values)