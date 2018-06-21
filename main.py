import os
from flask import Flask,redirect,render_template,request
import pypyodbc
import urllib
import json
import hashlib
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
data = pd.read_csv('titanic3.csv')
data.head()

app = Flask(__name__)

   
def randrange():
    lat = data['age'].values
    long = data['fare'].values
    X = np.array(list(zip(lat, long)))
    # plt.scatter(lat, long, c='red', s=7)
    # plt.show()
    kmeans = KMeans(n_clusters=8)
    kmeans.fit(X)
    centroid = kmeans.cluster_centers_
    labels = kmeans.labels_

    all = [[]] * 8
    print(all)
    for i in range(len(X)):

        # print(index)
        # print(X[i], labels[i])

        colors = ["b.", "r.", "g.", "w.", "y.", "c.", "m.", "k."]
        for i in range(len(X)):
            plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=3)

        plt.scatter(centroid[:, 0], centroid[:, 1], marker="x", s=150, linewidths=5, zorder=10)
        plt.show()
	

@app.route('/multiplerun', methods=['GET'])
def randquery():
    return randrange() 	

@app.route('/')
def hello_world():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()
