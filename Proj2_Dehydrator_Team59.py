# File Name: <Dehydrator.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import math as m

class Dehydrator():
    def __init__(self, etaDehy, wattageDehy, printData):
        self.eta = etaDehy
        self.wattage = wattageDehy
        self.print = printData
        
    def dehydrate(self, slurryIn, segmentSizes, diameter):
        initFlow = slurryIn.getVolFlowRate()
        slurryIn.setWat(slurryIn.getWat() * (1 - self.eta))
        
        # Calculates loss from waste energy
        density = 1.815
        height = 0
        for i in range(4):
            height += segmentSizes[i][2]
        flowChange = initFlow - slurryIn.getVolFlowRate()
        velocity = flowChange / (m.pi * (diameter / 2) ** 2)
        potEnergy = density * flowChange * 9.81 * height
        kinEnergy = 0.5 * density * flowChange * velocity ** 2
        wasteEnergy = potEnergy + kinEnergy
                
        if self.print:
            print("Dehydrating")
            print(slurryIn)
        
        return wasteEnergy
    
    def getWattage(self):
        return self.wattage * (3.6 * (10 ** 6)) # kWh/day to J/day
    
    def getEta(self):
        return self.eta
