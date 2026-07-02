# %% [markdown]
# ### Data Cleaning

# %%
# importing the required libraries  
import numpy as np
import pandas as pd

# %%
# reading the dataset
df = pd.read_csv('house_prices_raw.csv')
print(df.head())

# %%
# statistical summary of the dataset
print("Description of the dataset:")
pd.set_option('display.float_format', '{:,.2f}'.format)
print(df.describe())
print("\nDataset information:")
print(df.info())
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# %%
# dropping dulicate rows from the dataset
df = df.drop_duplicates()

# %%
# converting the column names to lowercase
df.columns = df.columns.str.lower()
print("\nColumn names after converting to lowercase:")
print(df.columns)
df['area_sqft'] = df['area_sqft'].str.replace(' sqft', '').astype(float)
print(df['area_sqft'].dtype)

# %%
# making values consistent in the 'location' column by converting them to lowercase and removing any whitespace
print(df['location'].unique())
df['location'] = df['location'].astype(str).str.lower().replace(r'\s+','',regex = True)

# checking the unique values in the 'location' column after making them consistent
print(df['location'].unique())

# %%
# handling missing values
df['location'] = df['location'].fillna(df['location'].mode()[0])
df['bathrooms'] = df['bathrooms'].fillna(df['bathrooms'].mode()[0])
df['age_years'] = df['age_years'].fillna(df['age_years'].median())
df['area_sqft'] = df['area_sqft'].fillna(df['area_sqft'].median())

# checking for missing values after handling them 
print(df.isnull().sum())

# %%
# adjust the negative values in the 'age_years' column to 0
df['age_years'] = df['age_years'].apply(lambda x: 0 if x < 0 else x)

# %%
# saving the cleaned dataset to a new CSV file
df.to_csv('house_prices_cleaned.csv', index=False)

# %% [markdown]
# ### EDA Exploratory Data Analysis

# %% [markdown]
# 
#  "The dataset contains some unrealistic property configurations (e.g., 5 BHK in 600 sq ft), but these were retained because there is no evidence they are data-entry errors."

# %%
# importing the required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# loading the cleaned dataset
df = pd.read_csv('house_prices_cleaned.csv')

# %%
print(df.describe())

# %%
df["price_per_sqft"] = (df["price"] / df["area_sqft"])

# %%
# distribution of the target variable 'price'
(sns
 .histplot(df['price'], kde = True, color = 'blue', bins = 30)
 .title.set_text('Distribution of price')
 )

# %% [markdown]
#  the distribution of the target variable 'price' is right-skewed, which indicates that there are some high-priced houses in the dataset. 

# %%
# checking the boxplot for the 'price' column to identify any outliers
sns.boxplot(x = 'price', data = df)

# %%
#  checking the largest area_sqft values in the dataset for the location 'bangalore'
print("Checking the largest area_sqft values in the dataset for the location 'bangalore': ")
df[df['location'] == 'bangalore'].sort_values(by = 'area_sqft', ascending = False)

# %% [markdown]
#  this data helps to understand what are the general rate of the houses in Bangalore and concluding that the house with the house price of 1.5 crore and area of 607 sqft that feels odd as compared to other houses in the same location. So we can remove this data point from the dataset as it is an outlier.

# %%
mask = (df['area_sqft'] == 607) & (df['price'] == 15_000_000)
data = df[mask]
df.drop(index=data.index, inplace=True)

# %%
sns.boxplot(x = 'area_sqft', data = df)

# %%
# checking the largest area_sqft values in the dataset only for the location
print("Checking the largest area_sqft values in the dataset:")
df.sort_values(by ='area_sqft',ascending = False).head(10)

# %%
# checking the largest area_sqft values in the dataset only for the location 'delhi'
print("Checking the largest area_sqft values in the dataset for the location 'delhi': ")
df[df['location'] == 'delhi'].sort_values(by = 'area_sqft', ascending = False).head(10)

# %%
# removing the suspicious data point with price 6,472,000.00 from the dataset
df.drop(index=df[df['price'] == 6_472_000.00].index, inplace=True)

# %% [markdown]
#  Removing a suspicious record where the property has an unusually large area
#  (9500 sqft) but a comparatively low price. Based on price-per-sqft analysis
#  and comparison with other Delhi properties, this record appears inconsistent
#  with the rest of the dataset.

# %%
# checking the boxplot again for the 'area_sqft' column after removing the suspicious data point
sns.boxplot(x = 'area_sqft', data = df)

# %% [markdown]
#  the outlier now looks like a reasonable value for the 'area_sqft' column. We can now proceed to check the largest area_sqft values in the dataset.

# %%
print("Checking the largest area_sqft values in the dataset: ")
print(df.sort_values(by ='area_sqft',ascending = False).head(10))

# %%



