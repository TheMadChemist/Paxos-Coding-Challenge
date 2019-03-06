import unittest
from AssortmentReader import AssortmentReader


class TestAssortmentReader(unittest.TestCase):
    def testGetAssortment(self):
        reader = AssortmentReader()
        result = reader.getAssortmentFromFile('testFile.txt')
        self.assertEqual(result[0].getPrice(), 200000, 'The first items price doesnt match')
        self.assertEqual(result[0].getName(), 'That thing you\'ve always wanted', 'The first items name doesnt match')
        self.assertEqual(result[1].getPrice(), 100, 'The second items price doesnt match')
        self.assertEqual(result[1].getName(), 'That other thing no one wants ever', 'The second items name doesnt match')

    def testBadFile(self):
        reader = AssortmentReader()
        result = reader.getAssortmentFromFile('imABadBad.File')
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
