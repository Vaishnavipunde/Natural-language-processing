# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:36:24 2023

@author: sai
"""


from PyPDF2 import PdfFileReader
#importing required module
from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader('C:/1-python/python_tutorial.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting specific page from pdf file
page=reader.pages[10]
page

#extract text from page
text=page.extract_text()
text






import re
chat='hi i have a problem with my order number 412889912'
pattern=r'order[^\d]*(\d*)'
matches=re.findall(pattern, chat)
matches

#instead of number there will be #

chat='hi i have a problem with my order # 412889912'
pattern=r'order[^\d]*(\d*)'
matches=re.findall(pattern, chat)
matches

#or   only no. is there

chat='hi my order 412889912 have problem'
pattern=r'order[^\d]*(\d*)'
matches=re.findall(pattern, chat)
matches



#above example using function
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat)



#retrieve email id and phone
chat1='hi:you ask lots of question  12345544,abc@xyz.com'
chat2='hi: here it is : (123)-344-23455,abc@xyz.com'
chat3='phone:1625537 email:abc@xyz.com '
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)










import re
text = '''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
'''
get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n',text)
get_pattern_match(r'Born.\n(.)\(age', text)
get_pattern_match(r'\(age.\n(.)', text)


def extract_personal_information(text):
    age = get_pattern_match(r'age (\d+)',text)
    full_name = get_pattern_match(r'Born(.*)\n',text).strip()
    birth_date = get_pattern_match(r'Born.\n(.)\(age', text).strip()
    birth_place = get_pattern_match(r'\(age.\n(.)', text)

    return{
        'age' : int(age),
        'name' : full_name.strip(),
        'birth_date' : birth_date.strip(),
        'birth_place' :birth_place.strip()
        }
extract_personal_information(text)





string='''Born: 19 April 1957 (age 66)	
Name: Mukesh Dhirubhai Ambani

Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	

    St. Xavier's College, Mumbai
    Institute of Chemical Technology (B.E.)

Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani
​
(m. 1985)​
[3]
Children	3
Parents	

    Dhirubhai Ambani (father)
    Kokilaben Ambani (mother)
''' 
import re
def match_data(pattern,string):
    match=re.findall(pattern, string)
    if match:
        return match[0]
    
match_data("Born\: ([1-9]* [a-zA-Z]* [1-9]*)", string)

match_data("age ([1-9]*)", string)

match_data("Name\: ([A-Za-z ]*)", string)


def person_info(string):
    name=match_data("Born\: ([1-9]* [a-zA-Z]* [1-9]*)", string)
    age=match_data("age ([1-9]*)", string)
    date=match_data("Name\: ([A-Za-z ]*)", string)
    return {"Name":name,"Age":int(age),"Birth-date":date}

person_info(string)

