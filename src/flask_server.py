import pickle
from flask import Flask,render_template, request,jsonify,Response
import pandas as pd
import time
import json
from pandas.io.json import json_normalize
from flask_pymongo import PyMongo

app = Flask(__name__)


###########################
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods = ['GET'])
def something():
    get_data()
    df = pd.read_json('newdata.json')
    df = json_normalize(list(df.data))
    mindf = feature_engineer(df)
    y_hat = model.predict_proba(mindf)
    with open ('prediction.csv','w') as f:
        f.write(str(y_hat[0][1]))

    prob = pd.read_csv('prediction.csv',header=None,names=['probability'])
    p = prob.probability
    df['probability'] = p

    if p[0] > 0.8:
        df['label'] = 'high risk'
    elif p[0] <= 0.8 and p[0] >0.6:
        df['label'] = 'middle risk'
    elif p[0] <= 0.6 and p[0] >=0.5:
        df['label'] = 'low risk'
    # if 'label' in df.keys():
    else:
        df['label'] = 'Not Fraud'
    df.to_json('df_predictions.json')
    import os
    os.system("mongoimport -h ds155461.mlab.com:55461-d fraud_db -c events -u bertolero16 -p lambo5 --file df_predictions.json")

# Route for getting new data
def get_data():
    import requests
    api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
    url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
    sequence_number = 0
    response = requests.post(url, json={'api_key': api_key,
                                        'sequence_number': sequence_number})
    raw_data = response.json()
    with open ('newdata.json','w') as f:
        f.write(json.dumps(raw_data))

    # flask pymongo
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    # mongo = PyMongo(app)
    # doc = mongo.db.fraud.insert(raw_data)



    #mongo db
    # from bson import json_util
    # data = json_util.loads(response.json())
    # # data = json.loads(raw_data) #json.loads returns dictionary
    # from pymongo import MongoClient
    # mongo_client = MongoClient()
    # db = mongo_client.mydb2
    # coll = db.fraud
    # # posts = db.posts
    # # #mongo needs to insert dictionary, however not a json file 
    # # post_id = posts.insert_one(raw_data['data']).inserted_ids
    # coll.insert_one(data)


    return jsonify(raw_data)



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)
