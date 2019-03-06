from AssortmentItem import AssortmentItem

'''
Reads assortment data out of a file.
'''
class AssortmentReader:

    '''
    Reads assortment file and places it into an array of assortmentItems.

    filename string the filename to read for assortment data.
    returns [AssortmentItem] the list of items read from the file, an empty array if no file found.
    '''
    def getAssortmentFromFile(self, filename):
        result = []
        try:
            with open(filename) as file:
                for line in file:
                    name, value = line.split(',')
                    entry = AssortmentItem(name, int(value.strip()))
                    result +=[entry]
            return result
        except:
            return []
