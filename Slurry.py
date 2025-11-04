# File Name: <Slurry.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Slurry():
    def __init__(self, eth, sug, wat, fib):
        self.ethanol = eth
        self.sugar = sug
        self.water = wat
        self.fiber = fib
        
    def setEth(self, eth):
        self.ethanol = eth
        
    def setSug(self, sug):
        self.sugar = sug
    
    def setWat(self, wat):
        self.water = wat
        
    def setFib(self, fib):
        self.fiber = fib
        
    def getEth(self):
        return self.ethanol
    
    def getSug(self):
        return self.sugar
    
    def getWat(self):
        return self.water
    
    def getFib(self):
        return self.fiber
    
    def sumWeights(self):
        return self.ethanol + self.sugar + self.water + self.fiber
    
    def normalize(self):
        total = self.sumWeights()
        self.ethanol = self.ethanol / total
        self.sugar = self.sugar / total
        self.water = self.water / total
        self.fiber = self.fiber / total
    
    def getPurity(self):
        return self.ethanol / self.sumWeights()
    
    def __str__(self):
        str = "---------------------------------------------\n"
        str += f"Ethanol: {self.ethanol:2.5}\n"
        str += f"Sugar: {self.sugar:2.5}\n"
        str += f"Water: {self.water:2.5}\n"
        str += f"Fiber: {self.fiber:2.5}\n"
        str += f"Purity: {self.getPurity():2.5}\n"
        return str