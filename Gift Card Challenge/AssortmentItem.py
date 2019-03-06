'''
Contains the necessary data for an assortment item, and the associated getters.
'''
class AssortmentItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name