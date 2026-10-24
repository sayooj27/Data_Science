from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

svm=SVC(kernel='linear')
svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)
print(f"prediction of testing variables:\n {y_pred}")

s=[[5,5,4,4]]
pred=svm.predict(s)
pred_v=[iris.target_names[p] for p in pred]
print(f"prediction of sample [5,5,4,4]: {pred_v}")
print(f"Accuracy score:  {accuracy_score(y_test,y_pred)}")
print(f"confusion matrix:\n  {confusion_matrix(y_test,y_pred)}")