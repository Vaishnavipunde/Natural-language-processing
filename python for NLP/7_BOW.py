# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:06:51 2023

@author: rajendra
"""

import pandas as pd
df=pd.read_csv("c:/2-dataset/Ecommerce_data.csv")
df.shape
df.head()
df.columns
df["label"].value_count()
df["label_num"]=df["label"].map({'Houshold':0,
                                 'books':1,
                                 'electornics':2,
                                 'clothing and accesseries':3})


df.head()
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2,
    random_state=2022,
    stratify=df.label_num)


print("shape of x_train:",x_train.shape)
print("shape of x_test:",x_test.shape)

y_train.value_count()
y_test.value_count()

from sklearn.feature_extraction import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

clf=Pipeline([('vectorization_tfidf',TfidfVectorizer()),
              ('KNN',KNeighborsClassifier())])

clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print(classification_report(y_test, y_pred))
