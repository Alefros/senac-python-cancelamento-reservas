# -*- coding: utf-8 -*-

#! pip list | grep boto
#
#!pip install boto3
#!pip install pandas
#!pip install sklearn
#!pip install matplotlib
#!pip install itertools

AWS_SERVICE_S3 = 's3'
AWS_S3_BUCKET_NAME
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

s3_client = boto3.client(service_name='AWS_SERVICE_S3', 
                         aws_access_key_id='AWS_ACCESS_KEY',
                         aws_secret_access_key='AWS_SECRET_KEY')

response = s3_client.create_bucket(Bucket= AWS_S3_BUCKET_NAME)

s3_client.download_file(AWS_S3_BUCKET_NAME, "regmodelo_2.json", "./regmodelo_2.json")

s3_client.download_file(AWS_S3_BUCKET_NAME, "model.h5", "./model.h5")

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
#import itertools
#
import calendar as cl
from pandas import read_csv
#from pandas import to_csv
#
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import mutual_info_classif

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from keras.models import model_from_json

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Prediction!"
    
@app.route('/DoPredict', methods = ['POST'])
def DoPredict():
    if request.method == 'POST':
        # load json and create model
        json_file = open('regmodelo_2.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")
        msg = request.form['msg']
        n1	= float(request.form['n1'])
        n2	= float(request.form['n2'])
        n3	= float(request.form['n3'])
        n4	= float(request.form['n4'])
        n5	= float(request.form['n5'])
        n6	= float(request.form['n6'])
        n7	= float(request.form['n7'])
        n8	= float(request.form['n8'])
        n9	= float(request.form['n9'])
        n10 = float(request.form['n10'])
        n11 = float(request.form['n11'])
        n12 = float(request.form['n12'])
        n13 = float(request.form['n13'])
        n14 = float(request.form['n14'])
        n15 = float(request.form['n15'])
        n16 = float(request.form['n16'])
        n17 = float(request.form['n17'])
        n18 = float(request.form['n18'])
        n19 = float(request.form['n19'])
        n20 = float(request.form['n20'])
        n21 = float(request.form['n21'])
        n22 = float(request.form['n22'])
        n23 = float(request.form['n23'])
        n24 = float(request.form['n24'])
        n25 = float(request.form['n25'])
        n26 = float(request.form['n26'])
        n27 = float(request.form['n27'])
        X_teste = np.array([[n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27]])
        print(X_teste)
        X_teste.shape
        res_2 = loaded_model.predict(X_teste)
        return "Valores previstos: {}".format(res_2), 200


## load json and create model
#json_file = open('regmodelo_2.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
## load weights into new model
#loaded_model.load_weights("model.h5")
#print("Loaded model from disk")
#









#X_teste = np.array([[2,30,1,0,1,2,1,19,3,3,0,0,0,2,2,0,1,27,0,1,135.9,0,0,17,21,13,15]])
#print(X_teste)
#X_teste.shape
#
#res_2 = loaded_model.predict(X_teste)
#
#print('valores previstos:\n'+str(res_2))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)