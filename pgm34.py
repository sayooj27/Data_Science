from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

x=df.iloc[:, :4]
print(x.head())
km=KMeans(n_clusters=3)
print("fitting model")
print(km.fit(x))
y=km.predict(x)
print("predicted clustres")
print(y)
centroid=km.cluster_centers_
print("cluster centroids")
print(centroid)