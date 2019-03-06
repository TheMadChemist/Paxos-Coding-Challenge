import hashlib

'''
Stores the hash digests and messages, and also generates new ones.
'''
class hashDigestService:
    results = {}

    '''
    Creates a new hash based on a message and then saves the pair in a dictionary.
    
    string message the message to hash via sha256
    returns string the resultant message hash
    '''
    def addHash(self, message):
        messageHash = hashlib.sha256(message.encode('utf-8')).hexdigest()
        self.results[messageHash] = message
        return messageHash

    '''
    Gets the message used to generate a given hash
    
    string shaHash the hash to find the paired message for
    returns string the message used to originally generate the hash
    '''
    def getMessage(self, shaHash):
        try:
            return self.results[shaHash]
        except KeyError:
            return None
