from flask import Flask, request
from flask_restful import Resource, Api
from hashDigestService import hashDigestService
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

'''
handles api requests for get and post for sha digests and messages
'''
class shaDigest(Resource):
    def __init__(self):
        self.hashDigestService = hashDigestService()

    '''
    Gets the message that created the sha hash, returns an error if no such hash is found
    
    string shaHash the hash to query 
    returns string the message that created the hash in the first place
    '''
    def get(self, shaHash):
        message = self.hashDigestService.getMessage(shaHash)
        if message:
            return {"message": message}
        else:
            resp = jsonify({'err_msg': 'Message not found'})
            resp.status_code = 404
            return resp

    '''
    posts a message expecting a sha hash in return. The message lives in the request body.
    
    returns string a sha digest generated through the message
    '''
    def post(self, shaHash=None):
        postBody = request.get_json(force=True)
        return {'digest': self.hashDigestService.addHash(postBody['message'])}

api.add_resource(shaDigest, '/messages/<shaHash>', '/messages')

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)