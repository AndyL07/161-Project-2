# File Name: <Slurry.py>
# Date: <11/4/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

ethDen = 789.4              # kg/m3
sugWatPercDen = 4.93596437  # kg/m3/w%
watDen = 998.19             # kg/m3
fibDen = 1500               # kg/m3

class Slurry():
    def __init__(self, eth, sug, wat, fib, volFlowRate):
        self.ethanol = eth
        self.sugar = sug
        self.water = wat
        self.fiber = fib
        self.initVolFlow = volFlowRate
        self.initVol = 1.0
        self.initVol = self.getVolumePerc()
        self.initMass = self.initVol / self.getDensity()
        
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
    
    def getInitVol(self):
        return self.initVol
    
    def getInitFlow(self):
        return self.initVolFlow
    
    def getInitMass(self):
        return self.initMass
    
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
    
    def getDensity(self):
        solMass = self.sugar + self.water
        solDen = (self.sugar / solMass) *    sugWatPercDen + watDen
        
        solVol = solMass / solDen
        ethVol = self.ethanol / ethDen
        fibVol = self.fiber / fibDen
        
        totVol = solVol + ethVol + fibVol
        totMass = solMass + self.ethanol + self.fiber
        
        totDen = totMass / totVol
        return totDen        
    
    def getTotMassPerc(self):
        return self.ethanol + self.sugar + self.water + self.fiber
    
    def getVolumePerc(self):
        return self.getTotMassPerc() / self.getDensity() / self.initVol
    
    def getVolFlowRate(self):
        return self.initVolFlow * self.getVolumePerc()
    
    def __str__(self):
        str = "---------------------------------------------\n"
        str += f"Ethanol: {self.ethanol:2.5}% wt\n"
        str += f"Sugar: {self.sugar:2.5}% wt\n"
        str += f"Water: {self.water:2.5}% wt\n"
        str += f"Fiber: {self.fiber:2.5}% wt\n"
        str += f"Purity: {self.getPurity() * 100:2.5}%\n"
        str += f"Volumetric Flow Rate: {self.getVolFlowRate():2.5} m3/s\n"
        return str