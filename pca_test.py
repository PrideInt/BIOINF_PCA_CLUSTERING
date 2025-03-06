import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import csv

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import mplcursors

target = ['name']

features = [
    '1-sample', '2-sample',
    '1-infected', '1-uninfected', 
    '2-infected', '2-uninfected',
]

n_clusters = 5
r_state = 88

# Load the data
frame = pd.read_csv('sample.csv')

X = frame.loc[:, features].values

print(X)

X = StandardScaler().fit_transform(X)

# print(X)

pca = PCA(n_components=2)
result = pca.fit_transform(X)

kmeans = KMeans(n_clusters=n_clusters, random_state=r_state)
clusters = kmeans.fit_predict(result)

frame['cluster'] = clusters

# print(frame)

plt.scatter(result[:, 0], result[:, 1], c=clusters, s=50, cmap='viridis')

# centers = kmeans.cluster_centers_

# nplt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

def show_annotation(sel):
    index = sel.index
    sel.annotation.set_text(f"Target: {cluster_df.loc[index, 'target']}, Cluster: {cluster_df.loc[index, 'cluster']}")

mplcursors.cursor(hover=True).connect('add', show_annotation)

plt.xlabel('Principal Component 1', fontsize = 15)
plt.ylabel('Principal Component 2', fontsize = 15)
plt.title('PCA', fontsize = 20)

plt.colorbar()
plt.show()

clusters = []
for i in range(n_clusters):
    clusters.append([])

cluster_labels = kmeans.labels_

cluster_df = pd.DataFrame({'cluster': cluster_labels, 'target': frame['name']})
cluster_df.to_csv('cluster-test.csv', index=False)

with open('cluster-test.csv', mode ='r') as file:
    csv_file = csv.reader(file)
    
    for lines in csv_file:
        try:
            cluster_id = int(lines[0])
            cluster_name = lines[1]
            clusters[cluster_id].append(cluster_name)
        except:
            continue

for i in range(n_clusters):
    pd.DataFrame(clusters[i]).to_excel(f'./clusters-test/cluster-{i}.xlsx', index=False)

# 3D projection

pca = PCA(n_components=3)
result = pca.fit_transform(X)

kmeans = KMeans(n_clusters=n_clusters, random_state=r_state)
clusters = kmeans.fit_predict(result)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

p = ax.scatter(result[:, 0], result[:, 1], result[:, 2], c=clusters, s=50, cmap='viridis')

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')

fig.colorbar(p)
plt.show()