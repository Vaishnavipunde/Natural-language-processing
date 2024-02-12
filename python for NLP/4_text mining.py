# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:27:02 2023

@author: rajendra
"""

sentence='we are learning TextMining from sanjivani AI'
#we want to know position of learning

sentence.index("learning")
#we want to know index of TextMining
sentence.split().index("TextMining")
#it will split words in list and count the position
#if we want to see the list select sentence .split()

#suppose we want to print a word in  reverse order
sentence.split()[2][::-1]
#here learning get reversed in gninrarel

#suppose we want to print first and last word
words=sentence.split()
first_word=words[0]
last_word=words[-1]
first_word
last_word

#concanate first and last word
concat_word=first_word+""+last_word
concat_word

#print even word from sentence
even_word=[words[x] for x in range(len(words))  if x%2==0]
even_word

#display only AI
sentence[-3:]


#display entire sentence in reverse order
sentence[::-1]

#select each word and display in reverse order
words
print( "".join(word[::-1] for word in words))











