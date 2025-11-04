# File Name: <Dehydrator.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Dehydrator():
    def __init__(self, etaDehy):
        self.eta = etaDehy
        
    def dehydrate(self, slurryIn):
        slurryIn.setWat(slurryIn.getWat() * (1 - self.eta))
        
        print("Dehydrating")
        print(slurryIn)
        
        # slurryIn.normalize()
        # print("Normalizing")
        # print(slurryIn)