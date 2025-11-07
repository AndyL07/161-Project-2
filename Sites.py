# File Name: <Sites.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

def getDimensions(site):
    if site == 3:
        segmentList = [
            # [length, bend1 angle, bend2 angle, change in height]
            [10, 0, 0, 10],
            [20, 0, 0, 0],
            [10, 90, 90, 10],
            [20, 0, 0, 20],
            [10, 0, 0, 0]
            ]
    elif site == 2:
        segmentList = [
            # [length, bend1 angle, bend2 angle]
            [10, 0, 0, 10],
            [10, 0, 0, 0],
            [10, 0, 0, 0],
            [15, 0, 90, 15],
            [10, 0, 0, 0]
            ]
    else:
        segmentList = [
            # [length, bend1 angle, bend2 angle]
            [10, 0, 0, 10],
            [10, 0, 0, 0],
            [10, 90, 90, 10],
            [10, 90, 90, 0],
            [10, 0, 0, 0]
            ]
        
    return segmentList
