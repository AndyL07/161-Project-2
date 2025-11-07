#Takes in site, cost, effiency as well as the maxCost and maxEfficiency
#Most likely will need to run code with all three sites to get maxCost/efficiency
def getDecisionMatrixValue(site, cost, efficiency):
    normalizedCost = 0
    normalizedEfficiency = 0
    normalizedEthical= 0
    
    maxEfficiency = 15
    maxCost = 20000000
    maxEthical = 20
    
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
    
    #Returns one value
    return ((0.4 * normalizedCost) + (0.4 * normalizedEfficiency) + (0.2 * normalizedEthical))