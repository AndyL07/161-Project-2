# File Name: <Fermenter.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Fermenter():
    def __init__(self, etaFerm):
        self.eta = etaFerm
        
    def ferment(self, slurryIn):
        slurryIn.setEth(0.51 * slurryIn.getSug() * self.eta)
        slurryIn.setSug(slurryIn.getSug() * (1 - self.eta))
        
        print("Fermenting")  
        print(slurryIn)
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)