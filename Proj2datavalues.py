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

bends = [
    {"angle": 20, "options": [
        {"diameter": 0.10, "cost": 100, "pipeLossCoeff": 0.1},
        {"diameter": 0.11, "cost": 149, "pipeLossCoeff": 0.1},
        {"diameter": 0.12, "cost": 493, "pipeLossCoeff": 0.1},
        {"diameter": 0.13, "cost": 1400, "pipeLossCoeff": 0.1},
        {"diameter": 0.14, "cost": 3200, "pipeLossCoeff": 0.1},
        {"diameter": 0.15, "cost": 6200, "pipeLossCoeff": 0.1},
    ]},
    {"angle": 30, "options": [
        {"diameter": 0.10, "cost": 105, "pipeLossCoeff": 0.15},
        {"diameter": 0.11, "cost": 157, "pipeLossCoeff": 0.15},
        {"diameter": 0.12, "cost": 517, "pipeLossCoeff": 0.15},
        {"diameter": 0.13, "cost": 1500, "pipeLossCoeff": 0.15},
        {"diameter": 0.14, "cost": 3400, "pipeLossCoeff": 0.15},
        {"diameter": 0.15, "cost": 6500, "pipeLossCoeff": 0.15},
    ]},
    {"angle": 45, "options": [
        {"diameter": 0.10, "cost": 110, "pipeLossCoeff": 0.2},
        {"diameter": 0.11, "cost": 164, "pipeLossCoeff": 0.2},
        {"diameter": 0.12, "cost": 543, "pipeLossCoeff": 0.2},
        {"diameter": 0.13, "cost": 1600, "pipeLossCoeff": 0.2},
        {"diameter": 0.14, "cost": 3600, "pipeLossCoeff": 0.2},
        {"diameter": 0.15, "cost": 6900, "pipeLossCoeff": 0.2},
    ]},
    {"angle": 60, "options": [
        {"diameter": 0.10, "cost": 116, "pipeLossCoeff": 0.22},
        {"diameter": 0.11, "cost": 173, "pipeLossCoeff": 0.22},
        {"diameter": 0.12, "cost": 570, "pipeLossCoeff": 0.22},
        {"diameter": 0.13, "cost": 1600, "pipeLossCoeff": 0.22},
        {"diameter": 0.14, "cost": 3800, "pipeLossCoeff": 0.22},
        {"diameter": 0.15, "cost": 7200, "pipeLossCoeff": 0.22},
    ]},
    {"angle": 75, "options": [
        {"diameter": 0.10, "cost": 122, "pipeLossCoeff": 0.27},
        {"diameter": 0.11, "cost": 181, "pipeLossCoeff": 0.27},
        {"diameter": 0.12, "cost": 599, "pipeLossCoeff": 0.27},
        {"diameter": 0.13, "cost": 1700, "pipeLossCoeff": 0.27},
        {"diameter": 0.14, "cost": 3900, "pipeLossCoeff": 0.27},
        {"diameter": 0.15, "cost": 7600, "pipeLossCoeff": 0.27},
    ]},
    {"angle": 90, "options": [
        {"diameter": 0.10, "cost": 128, "pipeLossCoeff": 0.3},
        {"diameter": 0.11, "cost": 190, "pipeLossCoeff": 0.3},
        {"diameter": 0.12, "cost": 700, "pipeLossCoeff": 0.3},
        {"diameter": 0.13, "cost": 1800, "pipeLossCoeff": 0.3},
        {"diameter": 0.14, "cost": 4100, "pipeLossCoeff": 0.3},
        {"diameter": 0.15, "cost": 8000, "pipeLossCoeff": 0.3},
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

def getPumpValue(name, length, key):
    for pump in pumps:
        if pump["name"] == name:
            for option in pump["options"]:
                if option["length"] == length:
                    return option.get(key)
    return None

def getPipeValue(name, diameter, key):
    for pipe in pipes:
        if pipe["name"] == name:
            for option in pipe["options"]:
                if option["diameter"] == diameter:
                    return option.get(key)
    return None

def getBendValue(angle, diameter, key):
    for bend in bends:
        if bend["angle"] == angle:
            for option in bend["options"]:
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

max = 0

step = 0

for f in fermenters:
    
    efficiency = 0
    cost = 0
    
    fname = f["name"]
    efficiency += getFermenterValue(fname, "efficiency")
    cost += getFermenterValue(fname, "cost")
    
    for d in distillers:
        dname = d["name"]
        efficiency += getDistillerValue(dname, "efficiency")
        cost += getDistillerValue(dname, "cost")
        
        for dehyd in materialRemoval:
            dehydname = dehyd["name"]
            efficiency += getDistillerValue(dehydname, "efficiency")
            cost += getDistillerValue(dehydname, "cost")
            
            for m in materialRemoval:
                mname = m["name"]
                efficiency += getMaterialRemovalValue(mname, "efficiency")
                cost += getMaterialRemovalValue(mname, "cost")
                
                for p in pumps:
                    pname = p["name"]
                    length = 6
                    for i in range(11):
                        cost += getPumpValue(pname, length, "cost")
                        efficiency += getPumpValue(pname, length, "efficiency")
                        length += 3
                        
                        for pi in pipes:
                            piname = pi["name"]
                            diameter = 0.1
                            for i in range(6):
                                diameter = round(diameter, 2)
                                cost += getPipeValue(piname, diameter, "cost")
                                #efficiency += getPipeValue(piname, diameter, "efficiency")
                                diameter += 0.01
                                
                                for b in bends:
                                    angle = b["angle"]
                                    diam = 0.1
                                    for i in range(6):
                                        diam = round(diam, 2)
                                        cost += getBendValue(angle, diam, "cost")
                                        #efficiency += getBendValue(angle, diam, "efficiency")
                                        diam += 0.01
                                        
                                        for v in valves:
                                            vname = v["name"]
                                            dia = 0.1
                                            for i in range(6):
                                                dia = round(dia, 2)
                                                cost += getValveValue(vname, dia, "cost")
                                                #efficiency += getValveValue(vname, dia, "efficiency")
                                                dia += 0.01
                                                step += 1
                                                print(step)
                                                if(efficiency / cost > max):
                                                    max = efficiency / cost
print(max)




#=======
    #return None
#>>>>>>> Stashed changes
