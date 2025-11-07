#Takes in site, cost, effiency as well as the maxCost and maxEfficiency
#Most likely will need to run code with all three sites to get maxCost/efficiency
def getDecisionMatrixValue(site, cost, efficiency):
    normalizedCost = 0
    normalizedEfficiency = 0
    
    maxEfficiency = .98
    maxCost = 10000000
    
    if(site == 1):
        cost += 6660000
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
    elif(site == 2):
        cost += 9300000
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
    elif(site == 3):
        cost += 1616500 
        normalizedCost = (1 - (cost / maxCost))
        
        normalizedEfficiency = efficiency / maxEfficiency
    
    #Returns the weighted normalized cost and efficiency
    return [0.4 * normalizedCost, 0.4 * normalizedEfficiency]
