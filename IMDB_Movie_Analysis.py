#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Project_DataAnalyst\Python project\Python_IMDB_Analysis\IMDB-Movie-Data.CSV')


# In[3]:


data


# # 1. Display Top 10 Rows of The Dataset

# In[4]:


data.head(10)


# # 2. Check Last 10 Rows of The Dataset
# 

# In[5]:


data.tail(10)


# # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# 

# In[7]:


data.shape


# # 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[8]:


data.info()


# # 5. Check Missing Values In The Dataset

# In[9]:


data.isnull().sum()


# # 6. Drop All The  Missing Values

# In[11]:


data.dropna(inplace=True)


# In[12]:


data.isnull().sum()


# # 7. Check For Duplicate Data

# In[13]:


data.duplicated()


# # 8. Get Overall Statistics About The DataFrame

# In[15]:


data.describe()


# # 9. Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes
# 

# In[19]:


data.columns


# In[25]:


Title_greaterthan_180=data[data['Runtime (Minutes)']>=180]['Title']


# In[28]:


print(Title_greaterthan_180)


# # 10. In Which Year There Was The Highest Average Voting?
# 

# In[29]:


data.columns


# In[45]:


data.groupby('Year')['Votes'].mean().sort_values(ascending = False)


# In[49]:


sns.barplot(x='Year',y='Votes',data=data)


# In[51]:


sns.countplot(x='Year',data=data)


# # 11. In Which Year There Was The Highest Average Revenue?
# 

# In[52]:


data.columns


# In[58]:


data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending =False)


# In[63]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title('Year vs Revenue')
plt.show()


# # 12. Find The Average Rating For Each Director

# In[64]:


data.columns


# In[67]:


avg_Rating_director=data.groupby('Director')['Rating'].mean()
print(avg_Rating_director)


# # 13. Display Top 10 Lengthy Movies Title and Runtime

# In[68]:


data.columns


# In[80]:


data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']].set_index('Title')


# # 14. Display Number of Movies Per Year
# 

# In[82]:


data.columns


# In[84]:


data['Year'].value_counts()


# In[85]:


sns.countplot(x='Year',data=data)


# # 15. Find Most Popular Movie Title (Highest Revenue)

# In[86]:


data.columns


# In[97]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]


# # 16. Display Top 10 Highest Rated Movie Titles And its Directors

# In[99]:


data.columns


# In[112]:


data.nlargest(10,'Rating')[['Title','Director']].set_index('Title')


# # 17. Display Top 10 Highest Revenue Movie Titles

# In[113]:


data.columns


# In[117]:


data.nlargest(10,'Revenue (Millions)')[['Title']].set_index('Title')


# # 18.  Find Average Rating of Movies Year Wise

# In[118]:


data.columns


# In[124]:


data.groupby('Year')['Rating'].mean().sort_values(ascending = False)


# # 19. Does Rating Affect The Revenue?

# In[126]:


sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)
plt.title('Revenue vs Rating')


# # 20. Classify Movies Based on Ratings [Excellent, Good, and Average]

# In[127]:


def Rating(rating):
    if Rating >=7.0:
        return"Excellent"
    elif rating >=6.0:
        return "Good"
    else :
        return "Average"


# # 21. Count Number of Action Movies

# In[137]:


data.columns


# In[138]:


data.head(5)


# In[141]:


data['Genre'].str_contains('Action')


# In[142]:


data['Genre'].dtype


# In[152]:


data[data['Genre'].str.contains('Action',case= False)]


# In[ ]:





# In[ ]:





# In[ ]:




