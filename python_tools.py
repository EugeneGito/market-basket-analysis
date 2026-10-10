#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


def load_data(path): return pd.read_csv(path)


# In[4]:


def inspect_data(df):
    print('------- HEAD -------')
    print(df.head()) 

    print('\n ------- SHAPE -------')
    print(df.shape)

    print('\n ------- INFO -------')
    df.info()

    print('\n ------- MISSING VALUES -------')
    print(df.isnull().sum())

    print('\n ------- DATA TYPES -------')
    print(df.dtypes)

    return df


# In[ ]:




