# File Name: <Filtration.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Filtration():
    def __init__(self, etaFilt):
        self.eta = etaFilt
        
    def filt(self, slurryIn):
        slurryIn.setFib(slurryIn.getFib() * (1 - self.eta))
        
        print("Filtering")
        print(slurryIn)
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)