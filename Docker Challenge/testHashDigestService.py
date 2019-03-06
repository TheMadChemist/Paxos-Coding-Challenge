import unittest
from hashDigestService import hashDigestService


class TestHashDigestService(unittest.TestCase):
    def testAddHash(self):
        digestService = hashDigestService()
        hash = digestService.addHash('foo')
        self.assertEqual(hash, "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae")

    def testGetMessage(self):
        digestService = hashDigestService()
        hash = digestService.addHash('foo')
        message = digestService.getMessage(hash)
        self.assertEqual(message, 'foo')

if __name__ == '__main__':
    unittest.main()
