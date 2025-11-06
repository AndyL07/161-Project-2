# File Name: <Fermenter.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Fermenter():
    def __init__(self, etaFerm, wattageFerm, printData):
        self.eta = etaFerm
        self.wattage = wattageFerm
        self.print = printData
        
    def ferment(self, slurryIn):
        slurryIn.setEth(0.51 * slurryIn.getSug() * self.eta)
        slurryIn.setSug(slurryIn.getSug() * (1 - self.eta))
        energyUse = self.wattage * (3.6 * (10 ** 6))
        
        if self.print:
            print("Fermenting")  
            print(slurryIn)
        
        return energyUse
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)