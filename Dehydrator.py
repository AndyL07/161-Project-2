# File Name: <Dehydrator.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Dehydrator():
    def __init__(self, etaDehy, wattageDehy, printData):
        self.eta = etaDehy
        self.wattage = wattageDehy
        self.print = printData
        
    def dehydrate(self, slurryIn):
        slurryIn.setWat(slurryIn.getWat() * (1 - self.eta))
        energyUse = self.wattage * (3.6 * (10 ** 6))
                
        if self.print:
            print("Dehydrating")
            print(slurryIn)
        
        return energyUse

        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)