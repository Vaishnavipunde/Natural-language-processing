# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:23:24 2023

@author: sai
"""

#UTF==>Unicode Transformation format


#normalizing unicode text to standard presentation
#NFC and NFD  both are normalization technique there is no difference bet them.
s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
s1
s2
s1==s2


import unicodedata
t1=unicodedata.normalize('NFC',s1) #here NFC is one of the normalization technique
t2=unicodedata.normalize('NFC',s2)
t1==t2



###############################################333333


string1="apple"
string2="jeeil123"
string3="2345"
string4="lkkn@98"

string1.encode(encoding="UTF-8",errors="strict")

string2.encode(encoding="UTF-8",errors="strict")

string3.encode(encoding="UTF-8",errors="strict")

string4.encode(encoding="UTF-8",errors="strict")


############################################

text="one 🐘 and three 🐋"
text
print(len(text))


####################################

e=text.encode('utf-8')
print(e)
print(len(e))


####################################

fname='data.txt'
with open(fname,mode='rb') as f:
    content=f.read()
    print(type(content))
    print(content)
    print(content.decode('utf-8'))


###########################################

#stripping  for remove white space

s='  hello world  \n'
s.strip()
s.lstrip()
s.rstrip()

#####################################
t='------hello=====--'
t.rstrip('-')
t.strip('=')
t.lstrip('-')

######################################

#concatenation of string
u='hello  word       \n'
u.replace(' ', '')

################################

import re
re.sub('\s+',"  ",s)


###################################3333

#aligning the text
text='hello world'
text.ljust(20)
text.center(40)
text.rjust(20)

text.rjust(20,'=')
text.center(30,'-')

#####################################

format(text,'>20') #>for right
format(text,'<20') #<for left
format(text,'^20') #^ for center

format(text,'=>20')
format(text,'*^20')

##########################################
'{:>10} {:>10}'.format('hello','world')

#############################################

x=1.23444
x
format(x,'>10')

format(x,'^10.2f')

#########################################
parts=["is","chicago",'not','chicago']
''.join(parts)

','.join(parts)

'  '.join(parts)


########################################












