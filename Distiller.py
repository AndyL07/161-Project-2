# File Name: <Distiller.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Distiller():
    def __init__(self, etaDist, wattageDist, printData):
        self.eta = etaDist
        self.wattage = wattageDist
        self.print = printData
        
    def distill(self, slurryIn):
        multFactor = (slurryIn.getEth() * ((1 / self.eta) - 1) /
                        (slurryIn.getSug() + slurryIn.getWat() + slurryIn.getFib()))
        
        slurryIn.setWat(slurryIn.getWat() * multFactor)
        slurryIn.setSug(slurryIn.getSug() * multFactor)
        slurryIn.setFib(slurryIn.getFib() * multFactor)
        
        energyUse = self.wattage * (3.6 * (10 ** 6))
                
        if self.print:
            print("Distilling")
            print(slurryIn)
        
        return energyUse

        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)