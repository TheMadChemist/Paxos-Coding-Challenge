import unittest
from CardOptimizer import CardOptimizer
from AssortmentItem import AssortmentItem


class TestCardOptimizer(unittest.TestCase):
    def testOptimizeTwoGifts(self):
        cardOptimizer = CardOptimizer()
        items = self.makePassableItemList()
        result = cardOptimizer.optimizeTwoGifts(1000, items)
        self.assertEqual(result[0].getPrice(), 300, 'The first items price doesnt match')
        self.assertEqual(result[0].getName(), 'awesomer item', 'The first items name doesnt match')
        self.assertEqual(result[1].getPrice(), 700, 'The second items price doesnt match')
        self.assertEqual(result[1].getName(), 'awesomerest(?) item', 'The second items name doesnt match')

    def testOptimizeTwoGiftsNoSolution(self):
        cardOptimizer = CardOptimizer()
        items = self.makePassableItemList()
        result = cardOptimizer.optimizeTwoGifts(100, items)
        self.assertEqual(len(result), 0, 'No result should have been found')

    def testOptimizeThreeGifts(self):
        cardOptimizer = CardOptimizer()
        items = self.makePassableItemList()
        result = cardOptimizer.optimizeThreeGifts(1500, items)
        self.assertEqual(result[0].getPrice(), 300, 'The first items price doesnt match')
        self.assertEqual(result[0].getName(), 'awesomer item', 'The first items name doesnt match')
        self.assertEqual(result[1].getPrice(), 500, 'The second items price doesnt match')
        self.assertEqual(result[1].getName(), 'awesomest item', 'The second items name doesnt match')
        self.assertEqual(result[2].getPrice(), 700, 'The third items price doesnt match')
        self.assertEqual(result[2].getName(), 'awesomerest(?) item', 'The third items name doesnt match')

    def makePassableItemList(self):
        itemList = []
        itemList += [AssortmentItem('awesome item', 100)]
        itemList += [AssortmentItem('awesomer item', 300)]
        itemList += [AssortmentItem('awesomest item', 500)]
        itemList += [AssortmentItem('awesomerest(?) item', 700)]
        return itemList

if __name__ == '__main__':
    unittest.main()