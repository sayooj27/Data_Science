import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(f"prediction of testing values: \n {y_pred}")
ac = accuracy_score(y_test, y_pred)
print(f"Accuracy: ",ac)

plt.figure(figsize=(12, 8))
tree.plot_tree(classifier)
plt.title("Decision Tree for Iris Dataset")
plt.savefig("pgm35.png")