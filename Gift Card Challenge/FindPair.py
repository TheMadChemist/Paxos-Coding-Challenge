import argparse
from AssortmentReader import AssortmentReader
from CardOptimizer import CardOptimizer

def main():
    parser = argparse.ArgumentParser(description="Find gifts to most effectively consume a gift card")
    parser.add_argument('assortmentFileName', help='a file to retrieve the assortment')
    parser.add_argument('giftCardValue', type=int, help='the value of the gift card')
    parser.add_argument('--findTrio', dest='findTrio', const=True, default=False, action='store_const', help='set if you want to get three items instead of two')
    args = parser.parse_args()

    assortmentReader = AssortmentReader()
    assortmentList = assortmentReader.getAssortmentFromFile(args.assortmentFileName)
    if not assortmentList:
        print('No items retrieved from assortment file.')
        return 1
    assortmentList.sort(key=lambda x: x.getPrice())

    giftCardValue = args.giftCardValue

    cardOptimizer = CardOptimizer()
    if args.findTrio:
        solution = cardOptimizer.optimizeThreeGifts(giftCardValue, assortmentList)
    else:
        solution = cardOptimizer.optimizeTwoGifts(giftCardValue, assortmentList)

    if len(solution) == 0:
        print('Not possible')
    else:
        output = []
        for item in solution:
            output += [item.getName() + ' ' + str(item.getPrice())]
        print(', '.join(output))
    return 0

if __name__ == "__main__":
    exit(main())
