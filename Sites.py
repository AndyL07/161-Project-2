# File Name: <Sites.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

def getDimensions(site):
    if site == 3:
        segmentList = [
            # [length, bend1 angle, bend2 angle]
            [10, 0, 0]
            [20, 0, 0]
            [10, 90, 90]
            [20, 0, 0]
            ]
    elif site == 2:
        segmentList = [
            # [length, bend1 angle, bend2 angle]
            [10, 0, 0]
            [10, 0, 0]
            [10, 0, 0]
            [16.64, 30, 60]
            ]
    else:
        segmentList = [
            # [length, bend1 angle, bend2 angle]
            [10, 0, 0]
            [10, 0, 0]
            [10, 90, 90]
            [10, 90, 90]
            ]
        
    return segmentList