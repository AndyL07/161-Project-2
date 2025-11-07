# File Name: <Pipe_Bends.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

def getBendValue(angle, diameter, key):
    for bend in bends:
        if bend["angle"] == angle:
            for option in bend["options"]:
                if option["diameter"] == diameter:
                    return option.get(key)
    return None

bends = [
    {"angle": 0, "options": [
        {"diameter": 0.10, "cost": 100, "pipeLossCoeff": 0},
        {"diameter": 0.11, "cost": 149, "pipeLossCoeff": 0},
        {"diameter": 0.12, "cost": 493, "pipeLossCoeff": 0},
        {"diameter": 0.13, "cost": 1400, "pipeLossCoeff": 0},
        {"diameter": 0.14, "cost": 3200, "pipeLossCoeff": 0},
        {"diameter": 0.15, "cost": 6200, "pipeLossCoeff": 0},
    ]},
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