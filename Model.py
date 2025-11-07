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
from Pipe_Bends import getBendValue
#from Part_Runner import getBendValue
from Sites import getDimensions

# Whether or not to print slurry after each unit operation
printUnits = False
site = 1

siteDims = getDimensions(site)

def runModel(segmentLoop):
    # Initializes slurry and unit operators
    volFlowRate = segmentLoop[0][4]
    ferm = segmentLoop[0][0]
    filt = segmentLoop[0][1]
    dist = segmentLoop[0][2]
    dehy = segmentLoop[0][3]
    etaPump = segmentLoop[1]
    
    # Create slurry
    slurry = Slurry(0.0, 0.20, 0.60, 0.20, volFlowRate)
    
    # Initial Conditions
    initDen = slurry.getDensity()
    initEnergy = 1000000 * (10 ** (2 * 3))
    eLossDot = 0
    energyLossDay = 0
    
    # Constant values from loop
    diameter = segmentLoop[2][0]
    frictFact = segmentLoop[2][1]
    valveCoeff = segmentLoop[2][2]
    
    # Segment dependent values
    segmentNum = 0
    segmentSizes = [[], [], [], [], []]
    segmentParts = [[], [], [], [], []]
    for segment in siteDims:
        length = segment[0]
        bendAngle1 = segment[1]
        bendAngle2 = segment[2]
        bendFact1 = getBendValue(bendAngle1, diameter, "pipeLossCoeff")
        bendFact2 = getBendValue(bendAngle2, diameter, "pipeLossCoeff")
        
        # Use the values to create a size and parts list
        segSize = [diameter, length]
        segPartList = [frictFact, 0, valveCoeff, bendFact1, bendFact2]
        
        # Input the current sizes and parts list to the entry for the given segment
        segmentSizes[segmentNum] = segSize
        segmentParts[segmentNum] = segPartList
        
        # Don't include a valve for hypothtical initial output and final input
        if segment == 0:
            segPartList[1] = 0
        elif segment == 4:
            segPartList[2] = 0
            
        # Increment the segment counter
        segmentNum += 1
    
    # Defining segment specifications
    segment1 = Segment(*segmentSizes[0], *segmentParts[0])
    segment2 = Segment(*segmentSizes[1], *segmentParts[1])
    segment3 = Segment(*segmentSizes[2], *segmentParts[2])
    segment4 = Segment(*segmentSizes[3], *segmentParts[3])
    segment5 = Segment(*segmentSizes[4], *segmentParts[4])
    
    # Calcuate mass and energy loss
    ##################################
    if printUnits:
        print("Initial")
        print(slurry)
    
    energyLossDay += (1 - etaPump) * initEnergy
    
    # Segment 1 - Fermenter
    eLossDot += segment1.segLoss(slurry)
    energyLossDay += ferm.ferment(slurry)
    #print(leakLoss(slurry))
    
    # Segment 2 - Filtration
    eLossDot += segment2.segLoss(slurry)
    energyLossDay += filt.filt(slurry)
    
    # Segment 3 - Distillation
    eLossDot += segment3.segLoss(slurry)
    energyLossDay += dist.distill(slurry)
    
    # Segment 4 - Dehydration
    eLossDot += segment4.segLoss(slurry)
    energyLossDay += dehy.dehydrate(slurry)
    
    # Segment 5 - Output
    eLossDot += segment5.segLoss(slurry)
    
    if printUnits:
        print("Final")
        print(slurry)
    ############################################
    
    # Conversion constants
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
    if printUnits:
        print(f"Input Speed: {in_speed:2.3f} gal/day")
        print(f"Output Speed: {ethGalDay:2.3f} gal/day")
        print(f"Outputted Ethanol Energy: {energy:2.3f} MJ/day")
        print(f"Total Energy Loss: {energyLossDay:2.3f} MJ")
        
    return energyLossDay
        
# # Test - Uncomment this entire section by highlighitng and doing Ctrl + 1
# #####################################################################################
# etaFerm = 0.9
# etaFilt = 0.9
# etaDist = 0.9
# etaDehy = 0.9
# etaPump = 0.8
# volFlowRate = 0.04

# ferm = Fermenter(etaFerm, 46600, printUnits)
# filt = Filtration(etaFilt, 48800, printUnits)
# dist = Distiller(etaDist, 47004, printUnits)
# dehy = Dehydrator(etaDehy, 48800, printUnits)

# diameter = 0.1
# length = 10
# frictFact = 0.1
# valveCoeff = 800
# bendAngle1 = 90
# bendAngle2 = 90
# bendFact1 = getBendValue(bendAngle1, diameter, "pipeLossCoeff")
# bendFact2 = getBendValue(bendAngle2, diameter, "pipeLossCoeff")

# segLoop = [[ferm, filt, dist, dehy, volFlowRate], etaPump, [diameter, frictFact, valveCoeff]]

# runModel(segLoop)
# #####################################################################################