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

etaFerm = 0.5
etaFilt = 0.5
etaDist = 0.81
etaDehy = 0.81

slurry = Slurry(0.0, 0.20, 0.60, 0.20)
ferm = Fermenter(etaFerm)
filt = Filtration(etaFilt)
dist = Distiller(etaDist)
dehy = Dehydrator(etaDehy)

print("Initial")
print(slurry)

ferm.ferment(slurry)
filt.filt(slurry)
dist.distill(slurry)
dehy.dehydrate(slurry)

print("Final")
slurry.normalize()
print(slurry)