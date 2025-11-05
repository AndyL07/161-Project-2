import math as m
GRAVITY = 9.81

def calcFluidSpeed(flowRate, radius):
    return pow(flowRate / (m.pi * pow(radius, 2)), 2)

def pipeFriction(density, time, frictionFactor, flowRate, velocity, length, diameter):
    mass = density * flowRate * time
    headLoss = frictionFactor * 8 * (flowRate ** 2) * length / ((m.pi ** 2) * GRAVITY * pow(diameter, 5))
    energyLoss = mass * headLoss * GRAVITY
    return energyLoss

def bendLoss(bendFactor, fluidSpeed):
    energyLoss = bendFactor * (fluidSpeed ** 2) / (2 * GRAVITY)
    return energyLoss

def valveLoss(resistanceCoefficent, fluidSpeed):
    return (pow(fluidSpeed, 2) * resistanceCoefficent / (2 * GRAVITY))

def leakLoss(density , flowRate, time, specHeatCapacity, tempChange, pressure, fluidDensity, velocity):
    mass = density * flowRate * time
    thermalLoss = mass * specHeatCapacity * tempChange
    pressureLoss = mass * (pressure / fluidDensity)
    kineticLoss = (1/2) * mass * velocity
    return (thermalLoss + pressureLoss + kineticLoss)