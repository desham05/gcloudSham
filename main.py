import os
from flask import Flask,redirect,render_template,request
import pypyodbc
import urllib
import json
import hashlib
import numpy as np
from sklearn.cluster import KMeans
print (scikit-learn._version)

app = Flask(__name__)


server = 'sham05.database.windows.net'
database = 'sqldb'
username = 'sham05'
password = '1qaz!QAZ'
driver= '{ODBC Driver 13 for SQL Server}'
   
def randrange(rangfro=None,rangto=None,num=None):
    dbconn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()
    success='SELECT '+rangfro+','+rangto+' from [titanic3]'
    cursor.execute(success)
    
    result_set = cursor.fetchall()
    age =[]
    fare =[]	
    for row in result_set:
       age.append(row[rangfro])
       fare.append(row[rangto])	   

    X = np.array(list(zip(age, fare)))
    kmeans = KMeans(n_clusters = int(num))
    kmeans.fit(X)
    centroid = kmeans.cluster_centers_
    labels = kmeans.labels_

    return render_template('display.html', ci=X, l=len(X), cen=centroid, lab=labels)	

@app.route('/multiplerun', methods=['GET'])
def randquery():
    rangfro = request.args.get('rangefrom')
    rangto = request.args.get('rangeto')
    num = request.args.get('nom')
    return randrange(rangfro,rangto,num) 	

@app.route('/')
def hello_world():
  return render_template('index.html')
  
if __name__ == '__main__':
  app.run()
