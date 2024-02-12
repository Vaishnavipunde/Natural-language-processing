# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:57:43 2023

@author: rajendra
"""

import re
sentence="sharat twitted ,Wittnessing 70th republic day in India"
re.sub(r'([\s\w]/_)+', '', sentence).split()


#extracting n-gram using custom defined function
import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([\s\w]/_)+', '', input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extractor("cute little boy play with kitten", 2)  #digram tokenization
n_gram_extractor("cute little boy play with kitten", 3)  #trigram tokenization

#ngram tokenization
from nltk import ngrams
list(ngrams("cute little boy play with kitten", 2))
list(ngrams("cute little boy play with kitten", 3))


from textblob import TextBlob
blob=TextBlob("cute little boy play with kitten")
blob.ngrams(n=2)
blob.ngrams(n=3)



#tokenization using keras
sentence
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence)

#tokenization using textblob
from textblob import TextBlob
blob=TextBlob(sentence)
blob.words

#tweet tokenizer
from nltk.tokenize import MWETokenizer
sentence
tweet_tokenizer=MWETokenizer([('republic','day')])
tweet_tokenizer.tokenize(sentence.split())
tweet_tokenizer.tokenize(sentence.replace('i','').split())

#regular expression tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\s+')
reg_tokenizer.tokenize(sentence)

#white space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence)

#word punct tokenizer
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence)

#########################################
sentence6="I love playing cricket.Criket players practices hard in their playing"
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
''.join(regex_stemmer.stem(wd)for wd in sentence6.split())
#######################################
sentence7='before eating,it would be nice to sanitize your hands'
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
"".join([ps_stemmer.stem(wd)for wd in words])


#lemitization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download("wordnet")
lemmitizer=WordNetLemmatizer()
sentence8="The codes executed today are far better than what we executed generally "
words=word_tokenize(sentence8)
"".join([lemmitizer.lemmatize(words)for words in words])

#singularize and pluralization
from textblob import TextBlob
sentence9=TextBlob("she shellas seashells on the seashore")
words=sentence9.words
sentence9.words[2].singularize()
sentence9.words[3].pluralize()

#language  translation from spanish to enaglish
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')

#custom stopwards removal
from nltk import word_tokenize
sentence9="she shellas seashells on the seashore"
custom_stop_words_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_words_list])

#extracting general features from raw text
#number of words
#detect presesnce of wh word
#polarity
#subjectivity
#language identification
#to identify number of words
import pandas as pd
df=pd.DataFrame([['The vacine for covid-19 will be announced on 1 st August'],['do you know how uch expectations the world populartin is having from this research'],['the risk of virus will come to an end on 31st july']])

df.columns=['text']
df

#now let us mwasure the wh
from textblob import TextBlob
df['number_of_wh']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_wh']


#detect the presence of wh word
from textblob import TextBlob
wh_words=set(['why','who','where','what','which','when','how'])
df['is_wh_words_present']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']


#polarity of sentence
df['polarity']=df['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity) 
df['polarity']

sentence10='I like this example very much'
pol=TextBlob(sentence10).sentiment.polarity
pol


sentence10='this is fantastic example and i like it very much'
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10='this was helpful example but i would have prefer another '
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10='this is my personal option that i would prefer another option'
pol=TextBlob(sentence10).sentiment.polarity
pol

#subjectivity of the dataframe df and check whether there is presence
df['subjectivity']=df['text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']


#to find language of the sentence 
df['language']=df['text'].apply(lambda x: TextBlob(str(x)).detect_language())











