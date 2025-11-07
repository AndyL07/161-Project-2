# File Name: <Flow_Generator.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

def getFlows(start, end, step):
    arr = []
    i = start
    while i <= end:
        arr.append(round(i, 2))
        i += step
    return arr