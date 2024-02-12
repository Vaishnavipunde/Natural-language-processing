# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:48:16 2023

@author: rajendra
"""

import nltk
nltk.download("punkt")  #internet is required for doumnloading
from nltk import word_tokenize
words=word_tokenize("I am learning NLP fumdamentals")
words

#parts of speech tagging
nltk.download("averaged_perceptron_tagger")
nltk.pos_tag(words)

#stop word from nltk
from nltk.corpus import stopwords
stop_words=stopwords.words("English")
stop_words

sentence1="I am learning NLP:it is one of most popular library python"
#first we tokenize the sentence
sentence_words=word_tokenize(sentence1)
sentence_words

#let's filter the sentence using stop_words
sentence_no_stops=" ".join([words for words in sentence_words])
sentence_no_stops
sentence1

#suppose we wany to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Maleshia").replace("IND", "india").replace("-20", "-2020")
normalized_sentence=normalized_sentence.replace("-19", "-2020")
normalized_sentence

#we want auto corection in sentence
from autocorrect import Speller
#declare the function speller defined for english
spell=Speller(lang="en")
spell("English")

#we want to correct whole sentence
sentence3="ntural lanuage processin deals with the part of extractin sentiiiments"

#let's first tokenize the sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
corrected_sentence





