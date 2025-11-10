# File Name: <Filtration.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import math as m

class Filtration():
    def __init__(self, etaFilt, wattageFilt, printData):
        self.eta = etaFilt
        self. wattage = wattageFilt
        self.print = printData
        
    def filt(self, slurryIn, segmentSizes, diameter):
        initFlow = slurryIn.getVolFlowRate()
        slurryIn.setFib(slurryIn.getFib() * (1 - self.eta))
        
        # Calculates loss from waste energy
        density = 1.815
        height = 0
        for i in range(2):
            height += segmentSizes[i][2]
        flowChange = initFlow - slurryIn.getVolFlowRate()
        velocity = flowChange / (m.pi * (diameter / 2) ** 2)
        potEnergy = density * flowChange * 9.81 * height
        kinEnergy = 0.5 * density * flowChange * velocity ** 2
        wasteEnergy = potEnergy + kinEnergy
        
        if self.print:
            print("Filtering")
            print(slurryIn)
        
        return wasteEnergy
    
    def getWattage(self):
        return self.wattage * (3.6 * (10 ** 6)) # kWh/day to J/day
    
    def getEta(self):
        return self.eta
