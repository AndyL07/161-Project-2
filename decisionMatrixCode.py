#Takes in site, cost and efficiency
def getDecisionMatrixValue(site, cost, efficiency):
    normalizedCost = 0
    normalizedEfficiency = 0
    normalizedEthical= 0
    
    #intialize max values for each parameter
    maxEfficiency = 40
    maxCost = 20000000
    maxEthical = 20
    
    #calculate decision matrix values based on site
    if(site == 1):
        cost += 6660000
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
        normalizedEthical = 1 - (20 / maxEthical)
    elif(site == 2):
        cost += 9300000
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
        normalizedEthical = 1 - (0 / maxEthical) 
    elif(site == 3):
        cost += 1616500 
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
        normalizedEthical = 1 - (0 / maxEthical)
    
    #Returns three seperate values as array
    #return [0.4 * normalizedCost, 0.4 * normalizedEfficiency, 0.2 * normalizedEthical]
   
    # Returns total score for decision matrix  
    finalVal = ((0.4 * normalizedCost) + (0.4 * normalizedEfficiency) + (0.2 * normalizedEthical))
    if finalVal > 1:
        print(f"Cost: {normalizedCost:2.3f} --- Eff: {normalizedEfficiency:2.3f} --- Eth: {normalizedEthical:2.3f}")
        print(efficiency)
        print(finalVal)
    return finalVal