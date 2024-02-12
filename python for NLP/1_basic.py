# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:08:29 2023

@author: sai
"""

import re
text=''''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern='\d\d\d\d\d\d\d\d'
matches=re.findall(pattern, text)
matches



text=''''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d{10}'
matches=re.findall(pattern, text)
matches



import re
text1=''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern='\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern, text)
matches


#printing number in indian or other style using or(|) operator
pattern="\(\d{3}\)-\d{3}-\d{4}|\d{10}"
matches=re.findall(pattern, text)
matches


#for removing symbols use except symbol[^;]  . except ;,- all get printing
text1='A protracted; legal battle; over a 32-carat;Golconda diamond-'
pattern='[^;]'
matches=re.findall(pattern, text)
matches



text3='''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022
'''
pattern=r'Note \d - [^\n]*'
matches=re.findall(pattern, text3)
matches



text3='''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022
'''
pattern=r'Note \d - ([^\n]+)'
matches=re.findall(pattern, text3)
matches


#if both are capital(FY2020)

string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r'FY\d{4} Q\d'
matches=re.findall(pattern, string)
matches

#0r

string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r'FY\d{4} Q[1234]'
matches=re.findall(pattern, string)
matches

#or

string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r'FY\d{4} Q[1-4]'
matches=re.findall(pattern, string)
matches


#if one is capital and other is small

string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern=r'FY\d{4} Q[1-4]'
matches=re.findall(pattern, string,re.IGNORECASE)
matches

#or

pattern='FY\d{4} Q[1-4]|fy\d{4} Q[1-4]'
matches=re.findall(pattern, string)
matches



#display 2020 not FY,here only text which is in bracket that get printed 
string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r'FY(\d{4} Q[1-4])'
matches=re.findall(pattern, string)
matches


#find only financial number means $ no.
string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''

pattern="\$[0-9\.]+"
matches=re.findall(pattern, string)
matches


string='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
#for removing $
pattern="\$([0-9\.]+)"
matches=re.findall(pattern, string)
matches




