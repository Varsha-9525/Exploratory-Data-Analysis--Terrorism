#!/usr/bin/env python
# coding: utf-8

# # Name - **Varsha Dhamdhere**

# # Data Science and Business Analytics Intern @ The Sparks Foundation 
# 
# ## Task-4: Exploraatory Data Analysis- Terrorism
# 

# ### Problem Statement:-
# - Perform 'Exploratory Data Analysis' on dataset 'Global Terrorism'
# - As a security/defense analyst, try to find out the hot zone of terrorism.
# - What all security issues and insights you can derive by EDA?
# 

# ### Dataset - [ https://bit.ly/2TK5Xn5 ]

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[3]:


data = pd.read_csv("C:\globalterrorismdb_0718dist.csv",encoding='latin1')
data.head()


# In[4]:


data.columns.values


# In[5]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City','latitude':'latitude',
    'longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound'},inplace=True)


# In[6]:


data = data[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill',
               'Wound','target1','summary','Group','Targettype','Weapon','motive']]


# In[7]:


data.head()


# In[8]:


data.shape


# In[9]:


data.isnull().sum()


# In[10]:


data['Wound'] = data['Wound'].fillna(0)
data['kill'] = data['kill'].fillna(0)


# In[11]:


data['Casualities'] = data['kill'] + data['Wound']


# In[12]:


data.info()


# In[13]:


data.describe()


# In[35]:


year = data['Year'].unique()
years_count = data['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,y = years_count,palette = "Set2")
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year',fontsize=20)
plt.ylabel('No. of Attacks Each Year',fontsize=20)
plt.title('Attacks In Years',fontsize=30)
plt.show()


# In[32]:


pd.crosstab(data.Year, data.Region).plot(kind='area',stacked=False,figsize=(20,10))
plt.title('Terrorist Activities In Region Every Year',fontsize=25)
plt.ylabel('No.of Attacks',fontsize=20,color='navy')
plt.xlabel("Year",fontsize=20,color='navy')
plt.show()


# In[16]:


attack = data.Country.value_counts()[:10]
attack


# In[17]:


data.Group.value_counts()[1:10]


# In[29]:


plt.subplots(figsize=(20,10))
sns.barplot(data['Country'].value_counts()[:10].index,data['Country'].value_counts()[:10].values,palette='Set2')
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation = 50)
plt.show()


# In[19]:


df = data[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4,color='g')
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# In[22]:


data['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(20,10),color='cyan')
plt.xticks(rotation = 50)
plt.xlabel("City",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Top 10 most effected city",fontsize=20)
plt.show()


# In[23]:


data['Attacktype'].value_counts().plot(kind='bar',figsize=(20,10),color='blue')
plt.xticks(rotation = 50)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Name of attacktype",fontsize=20)
plt.show()


# In[60]:


data[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['darkslateblue'])
plt.xticks(rotation=50)
plt.title("Number of killed ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[24]:


data[['Attacktype','Wound']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['pink'])
plt.xticks(rotation=50)
plt.title("Number of wounded  ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[26]:


plt.subplots(figsize=(20,10))
sns.countplot(data["Targettype"],order=data['Targettype'].value_counts().index,palette="gist_heat",edgecolor=sns.color_palette("mako"));
plt.xticks(rotation=90)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.title("Attack per year",fontsize=20)
plt.show()


# In[27]:


data['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='olive',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("Attack number",fontsize=15)
plt.show()


# In[28]:


data[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='goldenrod',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("No of killed people",fontsize=15)
plt.show()


# In[65]:


df=data[['Group','Country','kill']]
df=df.groupby(['Group','Country'],axis=0).sum().sort_values('kill',ascending=False).drop('Unknown').reset_index().head(10)
df


# In[66]:


kill = data.loc[:,'kill']
print('Number of people killed by terror attack:', int(sum(kill.dropna())))


# In[67]:


typeKill = data.pivot_table(columns='Attacktype', values='kill', aggfunc='sum')
typeKill


# In[68]:


countryKill = data.pivot_table(columns='Country', values='kill', aggfunc='sum')
countryKill


# ## **Conclusion and Results :**

# - Country with the most attacks: **Iraq**
# 
# 
# - City with the most attacks: **Baghdad**
# 
# 
# - Region with the most attacks: **Middle East & North Africa**
# 
# 
# - Year with the most attacks: **2014**
# 
# 
# - Month with the most attacks: **5**
# 
# 
# - Group with the most attacks: **Taliban**
# 
# 
# - Most Attack Types: **Bombing/Explosion**
# 

# ## Thank You ! 

# In[ ]:





# In[ ]:




