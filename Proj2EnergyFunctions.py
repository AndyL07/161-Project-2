import math as m
GRAVITY = 9.81

def calcFluidSpeed(flowRate, radius):
    return flowRate / (m.pi * pow(radius, 2))

def pipeFriction(slurryIn, frictionFactor, length, diameter):
    density = slurryIn.getDensity()
    flowRate = slurryIn.getVolFlowRate()
    headLoss = frictionFactor * 8 * (flowRate ** 2) * length / ((m.pi ** 2) * GRAVITY * pow(diameter, 5))
    mDot = density * flowRate
    energyLoss = mDot * headLoss * GRAVITY
    return energyLoss

def bendLoss(slurryIn, bendFactor, radius):
    density = slurryIn.getDensity()
    flowRate = slurryIn.getVolFlowRate()
    fluidSpeed = calcFluidSpeed(flowRate, radius)
    headLoss = bendFactor * (fluidSpeed ** 2) / (2 * GRAVITY)
    mDot = density * flowRate
    energyLoss = mDot * headLoss * GRAVITY
    return energyLoss

def valveLoss(slurryIn, resistanceCoefficent, radius):
    density = slurryIn.getDensity()
    flowRate = slurryIn.getVolFlowRate()
    fluidSpeed = calcFluidSpeed(flowRate, radius)
    headLoss = pow(fluidSpeed, 2) * resistanceCoefficent / (2 * GRAVITY)
    mDot = density * flowRate
    energyLoss = mDot * headLoss * GRAVITY
    return energyLoss

def leakLoss(slurryIn, pressure, velocity):
    density = slurryIn.getDensity()
    flowRate = slurryIn.getVolFlowRate()
    mDot = density * flowRate
    # thermalLoss = mDot * specHeatCapacity * tempChange
    pressureLoss = mDot * (pressure / density)
    kineticLoss = (1/2) * mDot * velocity
    return (pressureLoss + kineticLoss)