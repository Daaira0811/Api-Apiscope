from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util
app = Flask(__name__)

app.config['MONGO_URI'] ='mongodb://root:ap1scop3@localhost:27017/apiscope_data?authSource=admin'
mongo = PyMongo(app)


@app.route('/', methods = ['POST'])
def post_data():
    data=request.json['data']
    id=mongo.db.data.insert_one({'data':data})
    return str(id)

@app.route('/', methods = ['GET'])
def get_data():
    id=mongo.db.data.find().sort("_id",-1).limit(1);
    resp=json_util.dumps(id)
    return resp


if __name__ == "__main__":
    app.run(debug=True)