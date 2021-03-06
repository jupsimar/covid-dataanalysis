# -*- coding: utf-8 -*-
"""ProgramOne.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bLLYYl_ytkcmzvq-fVOBkTBRCSgRP-zE
"""

# importing the libraries
# importing the libraries
import json
import requests
import pandas as pd
from pandas import json_normalize

"""#Working With Covid data

"""

#endpoint
url ='https://api.covid19api.com/summary'

response = requests.get(url).json()
response
print(response.keys())

#Convert the json dictionary to dataframe(df)
rec = response['Countries']
#normalize functiona is used to flatten data
df=json_normalize(rec) 

df.head()

df.drop(['ID'],axis=1,inplace=True)

df.head()

df.set_index('Country')