# File Name: <Filtration.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Filtration():
    def __init__(self, etaFilt, wattageFilt, printData):
        self.eta = etaFilt
        self. wattage = wattageFilt
        self.print = printData
        
    def filt(self, slurryIn):
        slurryIn.setFib(slurryIn.getFib() * (1 - self.eta))
        energyUse = self.wattage * (3.6 * (10 ** 6))
        
        if self.print:
            print("Filtering")
            print(slurryIn)
        
        return energyUse
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)