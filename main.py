from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
data = pd.read_csv('titanic3.csv')
print(data.shape)
data.head()

lat = data['age'].values
long = data['fare'].values
X = np.array(list(zip(lat, long)))
# plt.scatter(lat, long, c='red', s=7)
 #plt.show()
kmeans = KMeans(n_clusters = 8)
kmeans.fit(X)
centroid = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroid)
print(labels)

print(len(labels))

all = [[]]*8
print(all)
for i in range(len(X)):
   
    # print(index)
    #print(X[i], labels[i])

 colors = ["b.","r.","g.","w.","y.","c.","m.","k."]
 for i in range(len(X)):
     plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 3)

 plt.scatter(centroid[:,0], centroid[:,1], marker = "x",s=150,linewidths = 5, zorder = 10)
 plt.show()