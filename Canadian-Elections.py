
# coding: utf-8

# In[251]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.io.sql as psql
get_ipython().magic(u'matplotlib inline')


# In[45]:

# http://www12.statcan.gc.ca/census-recensement/2011/dp-pd/prof/details/page.cfm?Lang=E&Geo1=FED2013&Code1=24028&Geo2=PR&Code2=24&Data=Count&SearchText=Hochelaga&SearchType=Begins&SearchPR=01&B1=All&GeoLevel=PR&GeoCode=028&TABID=1
# download Federal electoral districts (2013 representation order)
df = pd.read_csv("./data/98-316-XWE2011001-511.csv", low_memory=False, skiprows=1)


# In[46]:

df.head()


# In[191]:

df["Topic_Characteristic"] = df.Topic + ' ' + df.Characteristic


# In[246]:

census = df.pivot_table(index=['Geo_Code', 'Prov_Name', 'FED_Name'], columns='Topic_Characteristic', values='Total')
census.reset_index(inplace=True)
census.head()


# In[247]:

# Compute male ratio
ratio_male = df.ix[df.Characteristic=='Total population by age groups',['Geo_Code', 'Total', 'Male']]
ratio_male['ratio_male'] = ratio_male.Male/ratio_male.Total

census = pd.merge(census, ratio_male[['Geo_Code', 'ratio_male']], on='Geo_Code', how='left')


# In[257]:

# Plotting the resulting variable
census['ratio_male'].hist()
plt.show()
plt.boxplot(census['ratio_male'])
plt.show()


# In[277]:

l = list()
for i in list(census.columns.values):
    if 'Age characteristics' in i:
        l.append(i)


# In[283]:

l


# In[286]:

(census['Age characteristics    55 to 59 years']/census['Age characteristics Total population by age groups']).hist()


# In[193]:

## Creating new columns

# % by age
# % by marital status
# % size of family
# % by Total number of occupied private dwellings by structural type of dwelling
# % by mother tongue (french, english, non-official language, multiple response)
# % Knowledge of official languages

# To keep
# Total Population
# Average number of persons per census family
# Average number of persons in private households

