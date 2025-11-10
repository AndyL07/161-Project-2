# File Name: <Fermenter.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import math as m

class Fermenter():
    def __init__(self, etaFerm, wattageFerm, printData):
        self.eta = etaFerm
        self.wattage = wattageFerm
        self.print = printData
        
    def ferment(self, slurryIn, segmentSizes, diameter):      
        initFlow = slurryIn.getVolFlowRate()
        slurryIn.setEth(0.51 * slurryIn.getSug() * self.eta)
        slurryIn.setSug(slurryIn.getSug() * (1 - self.eta))
        
        density = 1.815
        height = 0
        for i in range(1):
            height += segmentSizes[i][2]
        flowChange = initFlow - slurryIn.getVolFlowRate()
        velocity = flowChange / (m.pi * (diameter / 2) ** 2)
        potEnergy = density * flowChange * 9.81 * height
        kinEnergy = 0.5 * density * flowChange * velocity ** 2
        wasteEnergy = potEnergy + kinEnergy
        
        if self.print:
            print("Fermenting")  
            print(slurryIn)
           
        return wasteEnergy
    
    def getWattage(self):
        return self.wattage * (3.6 * (10 ** 6)) # kWh/day to J/day
    
    def getEta(self):
        return self.eta
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)