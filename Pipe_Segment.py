# File Name: <Pipe_Segment.py>
# Date: <11/6/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Proj2EnergyFunctions import * 

class Segment():
    def __init__(self,  diameter, length, frictFact, valveCoeffOut, valveCoeffIn, bendFact1, bendFact2):
        self.dia = diameter
        self.rad = self.dia / 2
        self.len = length
        self.frictFact = frictFact
        self.valveCoeff1 = valveCoeffOut
        self.valveCoeff2 = valveCoeffIn
        self.bendFact1 = bendFact1
        self.bendFact2 = bendFact2
        self.energyLoss = 0
        
    def segLoss(self, slurryIn):
        self.energyLoss += valveLoss(slurryIn, self.valveCoeff1, self.rad)
        self.energyLoss += bendLoss(slurryIn, self.bendFact1, self.rad)
        self.energyLoss += bendLoss(slurryIn, self.bendFact2, self.rad)
        self.energyLoss += pipeFriction(slurryIn, self.frictFact, self.len, self.dia)
        self.energyLoss += valveLoss(slurryIn, self.valveCoeff2, self.rad)
        
        return self.energyLoss