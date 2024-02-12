# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:00:16 2023

@author: rajendra
"""
#BOW is used to convert unstructured data into  structurd data

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven indian farma companies are working to develop vaccine against the corona virus.',' the deadly virus has already infected more than14 people globally','Bharat biotech is the among domestic pharma firm working on the corona virus cannine in india']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_dataframe=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_dataframe.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_dataframe.head()




#bag of words model small
bag_of_word_model_small=CountVectorizer(max_features=5)
print(bag_of_word_model_small.fit_transform(corpus).todense())
bag_of_word_dataframe_small=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
bag_of_word_dataframe_small.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_dataframe_small.head()
















































































