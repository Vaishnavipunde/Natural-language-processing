# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 08:28:25 2023

@author: rajendra
"""
#steaming
import nltk
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")




#lemitizer
#lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")



#chunking(shallow partitioning)identifying named entity
from nltk import word_tokenize
nltk.download("maxent_ne_chunker")
nltk.download("words")
sentence="we are learning NLP in python by sanjivaniAI"
words=word_tokenize(sentence)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]


#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in sanijivaniAI . it is located in kopargaon")
sent


from nltk.wsd import lesk
sentence="keep your savings in the bank"
print(lesk(word_tokenize(sentence), 'bank'))
sentence1="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence1), 'bank'))


from nltk.corpus import wordnet as wn
for ss in wn.synset('bank'): print(ss, ss.defination())


'''
types of tokenization

tweet tokenizer
multiword expression tokenizer  (in which certain group of multiple word treated as one entity)
regular expression tokenizer  (develope during expression)
whight space tokenizer
word punct tokenizer

'''
