import math as m
GRAVITY = 9.81

def calcFluidSpeed(flowRate, radius):
    return flowRate / (m.pi * pow(radius, 2))

def pipeFriction(density, frictionFactor, flowRate, length, diameter):
    mDot = density * flowRate
    headLoss = frictionFactor * 8 * (flowRate ** 2) * length / ((m.pi ** 2) * GRAVITY * pow(diameter, 5))
    energyLoss = mDot * headLoss * GRAVITY
    return headLoss

def bendLoss(bendFactor, fluidSpeed):
    headLoss = bendFactor * (fluidSpeed ** 2) / (2 * GRAVITY)
    return headLoss

def valveLoss(density, flowRate, resistanceCoefficent, radius):
    headLoss = pow(calcFluidSpeed(flowRate, radius), 2) * resistanceCoefficent / (2 * GRAVITY)
    mDot = density * flowRate
    energyLoss = mDot * headLoss * GRAVITY
    return energyLoss

def leakLoss(density , flowRate, time, specHeatCapacity, tempChange, pressure, velocity):
    mass = density * flowRate * time
    thermalLoss = mass * specHeatCapacity * tempChange
    pressureLoss = mass * (pressure / density)
    kineticLoss = (1/2) * mass * velocity
    return (thermalLoss + pressureLoss + kineticLoss)