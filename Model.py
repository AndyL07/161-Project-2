# File Name: <Model.py>
# Date: <11/3/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

# Imports
from Slurry import Slurry
from Fermenter import Fermenter
from Filtration import Filtration
from Distiller import Distiller
from Dehydrator import Dehydrator
from Pipe_Segment import Segment
from Proj2EnergyFunctions import *

# Whether or not to print slurry after each unit operation
printUnits = False

# Unit Efficiencies
etaPump = 0.8
etaFerm = 0.9
etaFilt = 0.9
etaDist = 0.9
etaDehy = 0.9

# Initializes slurry and unit operators
volFlowRate = 0.04
slurry = Slurry(0.0, 0.20, 0.60, 0.20, volFlowRate)
ferm = Fermenter(etaFerm, 46600, printUnits)
filt = Filtration(etaFilt, 48800, printUnits)
dist = Distiller(etaDist, 47004, printUnits)
dehy = Dehydrator(etaDehy, 48800, printUnits)

# 
initDen = slurry.getDensity()
initEnergy = 1000000 * (10 ** (2 * 3))
eLossDot = 0
energyLossDay = 0

valveCoeff1 = 0
valveCoeff = 800
bendFact1 = 0.1
bendFact2 = 0.1
frictFact = 0.1

##################################
seg1Dia = 0.1
seg1Len = 10

seg1Size = [seg1Dia, seg1Len]
seg1Parts = [frictFact, valveCoeff1, valveCoeff, bendFact1, bendFact2]
segment1 = Segment(*seg1Size, *seg1Parts)

seg2Parts = [frictFact, valveCoeff, valveCoeff, bendFact1, bendFact2]
segment2 = Segment(*seg1Size, *seg2Parts)
segment3 = Segment(*seg1Size, *seg2Parts)
segment4 = Segment(*seg1Size, *seg2Parts)
segment5 = Segment(*seg1Size, *seg2Parts)

seg5Dia = 0.1

# Calcuate mass and energy loss
##################################
print("Initial")
print(slurry)

energyLossDay += (1 - etaPump) * initEnergy

# Segment 1 - Fermenter
eLossDot += segment1.segLoss(slurry)
energyLossDay += ferm.ferment(slurry)

# Segment 2 - Filtration
eLossDot += segment2.segLoss(slurry)
energyLossDay += filt.filt(slurry)

# Segment 3 - Distillation
eLossDot += segment3.segLoss(slurry)
energyLossDay += dist.distill(slurry)

# Segment 4 - Dehydration
eLossDot += segment4.segLoss(slurry)
energyLossDay += dehy.dehydrate(slurry)
eLossDot += valveLoss(slurry, valveCoeff, seg5Dia / 2)

print("Final")
print(slurry)
############################################

# Conversion constants
ethPerc = slurry.getEth() 
ethDen = slurry.getDensity()
gal_m3 = 264.172
sec_day = 60 * 60 * 24
MJ_gal = 80.1

# Output calculations
in_speed = volFlowRate * gal_m3 * sec_day # Inputted volumetric flow rate in gal/day
initMdot = in_speed * initDen # Inputted mass flow rate in kg/day
outMdot = slurry.getTotMassPerc() * initMdot # Outputted mass flow rate in kg/day
ethGalDay = outMdot / slurry.getDensity() # Outputted "pure" ethanol in gal/day
energy = ethGalDay * MJ_gal # Energy of outputted "pure"ethan in MJ

# Energy conversions 
energyLossDay += eLossDot * sec_day # Convert J/sec to J/day
energyLossDay /= 10 ** (2 * 3) # Convert J/day to MJ/day

# Final Prints
print(f"Input Speed: {in_speed:2.3f} gal/day")
print(f"Output Speed: {ethGalDay:2.3f} gal/day")
print(f"Outputted Ethanol Energy: {energy:2.3f} MJ/day")
print(f"Total Energy Loss: {energyLossDay:2.3f} MJ")