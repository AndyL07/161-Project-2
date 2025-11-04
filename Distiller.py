# File Name: <Distiller.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Distiller():
    def __init__(self, etaDist):
        self.eta = etaDist
        
    def distill(self, slurryIn):
        multFactor = (slurryIn.getEth() * ((1 / self.eta) - 1) /
                        (slurryIn.getSug() + slurryIn.getWat() + slurryIn.getFib()))
        
        slurryIn.setWat(slurryIn.getWat() * multFactor)
        
        slurryIn.setSug(slurryIn.getSug() * multFactor)
        
        slurryIn.setFib(slurryIn.getFib() * multFactor)
        
        print("Distilling")
        print(slurryIn)
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)