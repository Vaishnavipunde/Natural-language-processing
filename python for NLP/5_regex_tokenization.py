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
























