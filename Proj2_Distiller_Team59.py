# File Name: <Distiller.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import math as m

class Distiller():
    def __init__(self, etaDist, wattageDist, printData):
        self.eta = etaDist
        self.wattage = wattageDist
        self.print = printData
        
    def distill(self, slurryIn, segmentSizes, diameter):
        initFlow = slurryIn.getVolFlowRate()
        multFactor = (slurryIn.getEth() * ((1 / self.eta) - 1) /
                        (slurryIn.getSug() + slurryIn.getWat() + slurryIn.getFib()))
        
        slurryIn.setWat(slurryIn.getWat() * multFactor)
        slurryIn.setSug(slurryIn.getSug() * multFactor)
        slurryIn.setFib(slurryIn.getFib() * multFactor)
        
        # Calculates loss from waste energy
        density = 1.815
        height = 0
        for i in range(3):
            height += segmentSizes[i][2]
        flowChange = initFlow - slurryIn.getVolFlowRate()
        velocity = flowChange / (m.pi * (diameter / 2) ** 2)
        potEnergy = density * flowChange * 9.81 * height
        kinEnergy = 0.5 * density * flowChange * velocity ** 2
        wasteEnergy = potEnergy + kinEnergy
                
        if self.print:
            print("Distilling")
            print(slurryIn)
        
        return wasteEnergy
    
    def getWattage(self):
        return self.wattage * (3.6 * (10 ** 6)) # kWh/day to J/day
    
    def getEta(self):
        return self.eta
