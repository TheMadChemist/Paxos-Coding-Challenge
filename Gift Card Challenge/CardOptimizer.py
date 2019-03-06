
'''
Finds the best items of an assortment to maximize dollars used on a gift card
'''
class CardOptimizer:
    '''
    Returns two items with prices that sum to as close to giftCardTotal as possible without going over.

    giftCardTotal int the value to try to meet with the sum of item prices
    assortmentList [AssortmentItems] a list of AssortmentItems, sorted by price
    returns [AssortmentItems] representing the best pair of items, returns [] if no pairs found
    '''
    def optimizeTwoGifts(self, giftCardTotal, assortmentList):
        bestPair = []
        bestTotal = 0
        startIndex = 0
        endIndex = len(assortmentList) - 1
        while startIndex < endIndex:
            startElement = assortmentList[startIndex]
            endElement = assortmentList[endIndex]
            currentSum = startElement.getPrice() + endElement.getPrice()
            if currentSum > bestTotal and currentSum <= giftCardTotal:
                bestPair = [startElement, endElement]
                bestTotal = currentSum
            if currentSum < giftCardTotal:
                startIndex += 1
            elif currentSum > giftCardTotal:
                endIndex -= 1
            else:
                return bestPair
        return bestPair

    '''
    Returns three items with prices that sum to as close to giftCardTotal as possible without going over.

    giftCardTotal int the value to try to meet with the sum of item prices
    assortmentList [AssortmentItems] a list of AssortmentItems, sorted by price
    returns [AssortmentItems] representing the best pair of items, returns [] if no pairs found
    '''
    def optimizeThreeGifts(self, giftCardTotal, assortmentList):
        bestTrio = []
        bestTotal = 0
        subListOfset = 1
        for item in assortmentList:
            otherTwo = self.optimizeTwoGifts(giftCardTotal - item.getPrice(), assortmentList[subListOfset:])
            if otherTwo:
                currentTotal = item.getPrice() + otherTwo[0].getPrice() + otherTwo[1].getPrice()
                if currentTotal > bestTotal and currentTotal <= giftCardTotal:
                    bestTotal = currentTotal
                    bestTrio = [item] + otherTwo
                if bestTotal == giftCardTotal:
                    return bestTrio
            subListOfset += 1
        return bestTrio