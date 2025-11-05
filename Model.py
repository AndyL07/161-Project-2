# File Name: <Model.py>
# Date: <11/3/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Slurry import Slurry
from Fermenter import Fermenter
from Filtration import Filtration
from Distiller import Distiller
from Dehydrator import Dehydrator
from Proj2EnergyFunctions import *

etaPump = 0.8
etaFerm = 0.9
etaFilt = 0.9
etaDist = 0.9
etaDehy = 0.9

slurry = Slurry(0.0, 0.20, 0.60, 0.20)
ferm = Fermenter(etaFerm)
filt = Filtration(etaFilt)
dist = Distiller(etaDist)
dehy = Dehydrator(etaDehy)

volFlowRate = 0.04
initDen = slurry.getDensity()
initEnergy = 1000000 * (10 ** (2 * 3))
eLossDot = 0

valveCoeff = 800
frictFact = 0.1

##################################
seg1Dia = 0.1
seg1Len = 10

seg2Dia = 0.1
seg2Len = 10

seg3Dia = 0.1
seg3Len = 10

seg4Dia = 0.1
seg4Len = 10

seg5Dia = 0.1
seg5Len = 10

##################################
print("Initial")
print(slurry)

# Segment 1 - Fermenter
eLossDot += pipeFriction(slurry.getDensity(), frictFact, volFlowRate, seg1Len, seg1Dia)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg1Dia / 2)
ferm.ferment(slurry)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg2Dia / 2)

# Segment 2 - Filtration
eLossDot += pipeFriction(slurry.getDensity(), frictFact, volFlowRate, seg2Len, seg1Dia)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg2Dia / 2)
filt.filt(slurry)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg3Dia / 2)

# Segment 3 - Distillation
eLossDot += pipeFriction(slurry.getDensity(), frictFact, volFlowRate, seg3Len, seg1Dia)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg3Dia / 2)
dist.distill(slurry)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg4Dia / 2)

# Segment 4 - Dehydration
eLossDot += pipeFriction(slurry.getDensity(), frictFact, volFlowRate, seg4Len, seg1Dia)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg4Dia / 2)
dehy.dehydrate(slurry)
eLossDot += valveLoss(slurry.getDensity(), volFlowRate, valveCoeff, seg5Dia / 2)

############################################
print("Final")
print(slurry)

ethPerc = slurry.getEth()
ethDen = slurry.getDensity()
gal_m3 = 264.172
sec_day = 60 * 60 * 24
MJ_gal = 80.1

in_speed = volFlowRate * gal_m3 * sec_day
initMdot = in_speed * initDen
ethMdot = ethPerc * initMdot
ethGalDay = ethMdot / ethDen
energy = ethGalDay * MJ_gal

energyLoss = eLossDot * sec_day
energyLoss += (1 - etaPump) * initEnergy
energyLoss /= 10 ** (2 * 3)

print(f"Input Speed: {in_speed:2.3f} gal/day")
print(f"Output Speed: {ethGalDay:2.3f} gal/day")
print(f"Outputted Ethanol Energy: {energy:2.3f} MJ/day")
print(f"Total Energy Loss: {energyLoss:2.3f} MJ")