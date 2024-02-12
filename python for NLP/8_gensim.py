# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:02:39 2023

@author: rajendra
"""

import gensim
import pandas as pd

# Read the JSON file
df=pd.read_json("C:/2-dataset/reviews_Cell_Phones_and_Accessories_5.json.gz",lines=True)

# Tokenize and preprocess the reviewText column
review_text = df.reviewText.apply(lambda x: gensim.utils.simple_preprocess(x))

# Instantiate the Word2Vec model
model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4
)

# Build vocabulary
model.build_vocab(review_text, progress_per=1000)

# Train the Word2Vec model
model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)

# Save the model
model.save(r"C:\1-python\python for NLP\review_short_model")

# Find most similar words
similar_words = model.wv.most_similar("bad")

# Check similarity between words
similarity_cheap_inexpensive = model.wv.similarity(w1="cheap", w2="inexpensive")
similarity_great_good = model.wv.similarity(w1="great", w2="good")

print(similar_words)
print(similarity_cheap_inexpensive)
print(similarity_great_good)



