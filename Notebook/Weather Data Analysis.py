#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv("weather_data(1) (1).csv")


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[12]:


df["Date"] = pd.to_datetime(df["Date"])


# In[13]:


df


# In[14]:


df.dtypes


# In[10]:


df.info()


# In[11]:


df.describe()


# In[15]:


df.isnull().sum()


# In[16]:


df.duplicated().sum()


# In[17]:


df.drop_duplicates(inplace=True)


# In[18]:


df.duplicated().sum()


# In[19]:


df.isnull().sum()


# In[20]:


df["Temperature"].fillna(df["Temperature"].median(), inplace=True)
df["Humidity"].fillna(df["Humidity"].median(), inplace=True)
df["WindSpeed"].fillna(df["WindSpeed"].median(), inplace=True)
df["Rainfall"].fillna(df["Rainfall"].median(), inplace=True)


# In[21]:


df.isnull().sum()


# In[26]:


df["Month"] = df["Date"].dt.month_name()
df["Year"] = df["Date"].dt.year

df.head()


# In[69]:


def get_season(month):
    if month in [10,11,12,1]:
        return "Winter"
    elif month in [2,3, 4, 5]:
        return "Summer"
    else:
        return "Monsoon"

df["Season"] = df["Date"].dt.month.apply(get_season)

df.head()


# In[28]:


monthly_summary = df.groupby("Month")["Temperature"].agg(["mean", "median", "std"])

monthly_summary


# In[29]:


season_summary = df.groupby("Season")["Temperature"].agg(["mean", "median", "std"])

season_summary


# In[30]:


#hottest day
df[df["Temperature"] == df["Temperature"].max()]


# In[31]:


#coolest day
df[df["Temperature"] == df["Temperature"].min()]


# In[32]:


#Windiest Day
df[df["WindSpeed"] == df["WindSpeed"].max()]


# In[33]:


#Wettest Day
df[df["Rainfall"] == df["Rainfall"].max()]


# In[34]:


correlation = df[["Temperature", "Humidity", "WindSpeed", "Rainfall"]].corr()

correlation


# In[50]:


plt.plot(df["Date"], df["WindSpeed"])

plt.title("WindSpeed Trend Over Time")
plt.xlabel("Date")
plt.ylabel("WindSpeed (km/h)")
plt.grid(True)

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\wind_trend.png", dpi=300)

plt.show()


# In[64]:


sns.histplot(df["Rainfall"], bins=20, kde=True)

plt.title("Rainfall Distribution")

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\Rainfall_histogram.png", dpi=300)
plt.show()


# In[63]:


sns.boxplot(x=df["Temperature"])

plt.title("Temperature Boxplot")

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\Temp_boxplot.png", dpi=300)
plt.show()


# In[53]:


sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\correlation_heatmap.png", dpi=300)
plt.show()


# In[54]:


df["Month_Year"] = df["Date"].dt.strftime("%Y-%m")
df.head()


# In[57]:


monthly_mean = df.groupby("Month_Year")["Temperature"].mean().reset_index()

plt.figure(figsize=(14,5))

plt.bar(monthly_mean["Month_Year"], monthly_mean["Temperature"])

plt.title("Monthly Mean Temperature")
plt.xticks(rotation=45)

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\monthly_mean_temperature.png", dpi=300)
plt.show()


# In[70]:


df["Rolling_Avg"] = df["Humidity"].rolling(7).mean()

plt.figure(figsize=(14,5))

plt.plot(df["Date"], df["Rolling_Avg"])

plt.title("7-Day Rolling Average Humidity")

plt.savefig(r"E:\PowerBI Desktop\Weather Data Analysis\plots\rolling_average.png", dpi=300)
plt.show()


# # Business Insights

# In[65]:


# The monthly average temperature follows a clear seasonal pattern, with warmer months showing higher average temperatures.

# Rainfall is concentrated during the monsoon months, indicating seasonal precipitation patterns.

# The correlation heatmap shows a negative relationship between temperature and humidity.

# Most weather observations fall within the normal range, with only a few outliers detected during data cleaning.

# The cleaned dataset is suitable for visualization and future predictive analysis.


# # Recommendations

# In[66]:


# Plan outdoor activities during low rainfall months.
# Improve drainage systems before the monsoon season.
# Use the cleaned dataset for future weather forecasting.
# Continue monitoring temperature and rainfall trends for better planning.


# In[71]:


df.to_csv(r"E:\PowerBI Desktop\Weather Data Analysis\data\Weather Data Analysis.csv", index=False)


# In[72]:


df


# In[ ]:




