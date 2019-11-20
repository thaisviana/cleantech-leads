from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request
from flask_pymongo import PyMongo
import json

from lead import Lead

app = Flask(__name__)

ors = CORS(app)
app.config.from_object('config.Config')

mongo = PyMongo(app)


@cross_origin()
@app.route('/lead', methods=['GET'])
def get_all_leads():
    lead_db = mongo.db.leads
    output = []
    for s in lead_db.find():
        output.append(Lead.jsonify(s))
    return jsonify({'result': output})


@cross_origin()
@app.route('/lead', methods=['POST'])
def add_lead():
    lead_db = mongo.db.leads
    data_dict = json.loads(request.data)
    data = Lead.jsonify(data_dict)

    lead_id = lead_db.insert(data)
    
    new_star = lead_db.find_one({'_id': lead_id})
    return jsonify({'result': Lead.jsonify(new_star)})


if __name__ == '__main__':
    app.run(debug=True)

