# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:15:50 2023

@author: sai
"""
#tokenization
txt="welcome to new year 2023"
x=txt.split()
x


#remove special character
import re
def remove_special_character(text):
    pattern=r'[^a-zA-Z0-9.,!?/:;\"\'\s]'
    return re.sub(pattern,"",text)

remove_special_character("""077 not sure @ if this % was #fun!""")




#remove numbers  here ^ sign is used it is called except sign
import re
def remove_special_character(text):
    pattern=r'[^a-zA-Z.,!/:;\"\'\s]'
    return re.sub(pattern,"",text)

remove_special_character("""077 not sure @ if this % was #fun""")







txt="welcome: to the ,new year; 2023"
import re
x=re.split(r'(?:,|;|\s)\s*',txt)
x




#removing punctuations
import string
def fun(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
fun("artical:@first sentence of some,{important}article having lots of ~ punctuations")


#stemming     here ing part of word get removed only original word is remain
import nltk  #natural language tool k
def fun(text):
    x=nltk.porter.PorterStemmer()
    text=' '.join([x.stem(word) for word in text.split()])
    return text
fun("we are eatting and swimming ;we have been eatting and swimming ;he eats and swim;he ate and swam")



#matching text at end or start of string

filename="spam.txt"
filename.endswith('.txt')


text="i live in shevgaon"
text.endswith('shevgaon')


choices=('http:',"ftp:")
url="http://www.python.org"
url.startswith(choices)

#slicing if string
a="anskjki"
a[2:5]

a[-3:-1]

a[2:-3]

a[2:6:2]

a[6:1:-2]

a[:3]

a[2:]

a[::-1]



filename="spam.txt"
filename[-4:]=='.txt'

url="http://www.python.org"
url[:5]=='http:' or url[:6]=='http:' or url[:4]=='ftp:'



from fnmatch import fnmatch,fnmatchcase
names=['doc1.csv','doc2.csv','config.ini','foo.py']
[name for name in names if fnmatch(name,'doc*.csv')]

#get string which is end with ST
addresses=["5421 N CLARK ST","1060 W ADDISON ST","9879 JHIG KJ","989 JFHJ HYFYF"]
from fnmatch import fnmatch,fnmatchcase
[add for add in addresses if fnmatchcase(add,'*ST')]

















