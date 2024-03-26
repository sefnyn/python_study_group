# -*- coding: utf-8 -*-
"""ML Linear Regression attempt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lgcD24cAvcRCDvLWTg3g4EYx8It7bauv

# **Linear Regression**
"""

## This was originally a .ipynb (but too large to upload to GitHub) so there are no print statements
# so the code may not run smoothly...

import pandas as pd

df = pd.read_excel('English archives deprivation data.xlsx')
df.head()

df.info()
df.dtypes
df.describe()

df.isnull().sum()

df[df['Type'].isnull()]
df.at[2157, 'Type']='University'
df.loc[[2157]]

df['PoD'].fillna('no', inplace=True)
df.isnull().sum()

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
stats_df = df[['Index of Multiple Deprivation Rank', 'Income Score', 'Employment Score', 'Education and Skills Rank', 'Health and Disability Rank', 'Crime Rank', 'Barriers to Housing and Services Rank', 'Living Environment Rank', 'IDACI Score', 'IDAOPI Score']]
plt.figure(figsize=(12, 12))
sns.heatmap(stats_df.corr(), annot=True)
#to show the correlations between data

from matplotlib import pyplot as plt
import seaborn as sns
df1 = df[['Type', 'Region', 'Index of Multiple Deprivation Rank','Income Score', 'Employment Score', 'IDACI Score', 'IDAOPI Score']]
sns.pairplot(df1, hue='Type')
#There is significant correlation between the Income, Employment, IDACI and IDAOPI scores and with the Index of Multiple Deprivation Rank

df2 = df[['Type', 'Region', 'Index of Multiple Deprivation Rank', 'Education and Skills Rank', 'Health and Disability Rank', 'Crime Rank', 'Barriers to Housing and Services Rank', 'Living Environment Rank']]
sns.pairplot(df2, hue='Region')
#There is a correlation between the Index of Multiple Deprivation Rank and the Education and Skills, Health and Disability and Crime Ranks, but surprisingly, not with the Barriers to Housing or Living Environment Ranks

df3 = df[['Income Score', 'Employment Score', 'Education and Skills Rank', 'Health and Disability Rank', 'Crime Rank', 'Barriers to Housing and Services Rank', 'Living Environment Rank']]
sns.pairplot(df3)

df4 = df[['IDACI Score', 'IDAOPI Score', 'Education and Skills Rank', 'Health and Disability Rank', 'Crime Rank', 'Barriers to Housing and Services Rank', 'Living Environment Rank']]
sns.pairplot(df4)

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Index of Multiple Deprivation Rank', y='Income Score', data=df )

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Index of Multiple Deprivation Rank', y='IDACI Score', data=df )

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Income Score', y='IDACI Score', data=df )
#only a few outliers

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Income Score', y='IDAOPI Score', data=df )
#there are a more few outliers here

from matplotlib import pyplot as plt
import seaborn as sns

sns.lmplot(x= 'Income Score', y='Employment Score', data=df )
#very few outliers, and the homoscedasticity is fairly good

sns.displot(df['Employment Score'])
#Employmenr score has a positive skew

sns.displot(df['IDACI Score'])
#IDACI score also skews to the right

a = df['Income Score'] <0.23
b = df['IDAOPI Score'] > 0.75
print(df[a & b])
df = df.drop([215, 216, 507, 508, 509, 850, 851, 852, 853, 854], axis=0)

sns.lmplot(x= 'Income Score', y='IDAOPI Score', data=df )
#there are still outliers, but it looks a little better

a = df['Income Score'] < 0.3
b = df['IDACI Score'] > 0.75
print(df[a & b])
df=df.drop([170], axis=0)

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Income Score', y='IDACI Score', data=df )

sns.lmplot(x= 'Income Score', y='Employment Score', data=df, fit_reg=False, hue='Type')
#The income and Employment scores relate to the proportion of the population that is 'imcome deprived' or 'employment deprived'
#with a larger score correpsonding to a more deprived area (e.g. a score of 0.38 indictes 38% of the population is income deprived in that area)
#The graph shows that the majority of business archives, and most national archives, are located in less income or employment deprived areas
#and specialist and local archives more evenly dispersed.

stats_df = df[['Education and Skills Rank', 'Health and Disability Rank', 'Barriers to Housing and Services Rank', 'Living Environment Rank']]
sns.boxplot(data=stats_df)
#There is considerable variability in most of the 'Rank' categories

stats_df = df[['Income Score', 'Employment Score', 'IDACI Score','IDAOPI Score']]
sns.boxplot(data=stats_df)
#The 'Score' categories show less variability, but have more outliers

#There is a strong correlation between the depravation income score and the employment, IDACI and IDAOPI scores (which relate to deprivation affecting childern and older people respectively)
#These all relate directly to proportions of the population that are deprived and are more comparable than the ranks, which relate to the relative deprevation of an area as complared with another
import numpy as np
from sklearn.linear_model import LinearRegression

X = df[['Employment Score', 'IDACI Score', 'IDAOPI Score']]
y = df[['Income Score']]
y=np.array(y)

linreg = LinearRegression()
linreg.fit(X,y)
print(X.shape)
print(y.shape)
y_pred = linreg.predict(X)

df.loc[[42]]
#Testing the model...

print('Predicted income score:', linreg.predict([[0.294, 0.367, 0.396]]))
#prediction is 0.354; the actual income score is 0.359, so very close
import math
from sklearn.metrics import mean_squared_error
y1 = [0.359]
y_pred1 = [0.354]
error = mean_squared_error(y1, y_pred1)
print('MSE:', error)
print('Accuarcy:', 1-error)
#The MSE is small, suggesting that the accuracy is good. However, we are using data that the model has already been trained on

df.loc[[101]]

print(df.loc[[101]])
print('Predicted income score:', linreg.predict([[0.192, 0.371, 0.49]]))
#prediction is 0.273; the actual income score is 0.295
y2 = [0.295]
y_pred2 = [0.273]
print('MSE:', mean_squared_error(y2, y_pred2))
print('Accuracy:', 1-mean_squared_error(y2, y_pred2))

#Evaluating the model:

import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

MSE = mean_squared_error(y, y_pred)
MAE = mean_absolute_error(y, y_pred)
RMSE = math.sqrt(MSE)

print("MSE: ", round(MSE,5))
print("MAE: ", round(MAE,5))
print("RMSE: ", round(RMSE,5))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

linreg.fit(X_train, y_train)
linreg.score(X_test, y_test)

#using train-test-split to evaluate the model, suggests an accuracy sore of 0.96

#Although the relationship is not quite as clear, an attempt to find the Index of Multiple Deprivation Rank given the education, health and crime ranks

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Index of Multiple Deprivation Rank', y='Crime Rank', data=df )
#homoscedasticity is not so great here

#removing outliers, so that the data can better fit the model
a = df['Crime Rank'] > 27000
b = df['Index of Multiple Deprivation Rank'] < 10000
df[a & b]
df= df.drop([112,113,114,458,556,892,893,960,973])

a = df['Crime Rank'] > 32000
b = df['Index of Multiple Deprivation Rank'] < 20000
df[a & b]
df = df.drop([986, 1025, 1324, 1380,1390, 1824 , 1825, 1826 , 1827 , 1828, 1829, 1830 , 1831, 1832 , 1833, 1834, 1835, 1836, 1837])

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Index of Multiple Deprivation Rank', y='Education and Skills Rank', data=df )

a = df['Education and Skills Rank'] < 15000
b = df['Index of Multiple Deprivation Rank'] > 27000
df[a & b]
df= df.drop([1265,1266,1711, 1949])

a = df['Education and Skills Rank'] > 30000
b = df['Index of Multiple Deprivation Rank'] < 14000
df[a & b]
df= df.drop([432,660,661,662,811,981])

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Index of Multiple Deprivation Rank', y='Health and Disability Rank', data=df )

a = df['Health and Disability Rank'] > 31000
b = df['Index of Multiple Deprivation Rank'] < 14000
df[a & b]
df= df.drop([1337,1437,1438])

a = df['Health and Disability Rank'] < 8000
b = df['Index of Multiple Deprivation Rank'] > 18000
df[a & b]
df= df.drop([1194,1195,1196,1238,1239])

import numpy as np
from sklearn.linear_model import LinearRegression

X4 = df[['Health and Disability Rank', 'Education and Skills Rank', 'Crime Rank']]
y4 = df[['Index of Multiple Deprivation Rank']]

y=np.array(y4)

linreg = LinearRegression()
linreg.fit(X4,y4)
print(X4.shape)
print(y4.shape)
y_pred4 = linreg.predict(X4)

df.loc[[607]]

print('Predicted Index of Multiple Deprivation Rank:', linreg.predict([[8016, 20644, 5122]]))
#prediction is 9965.26; the actual deprivation rank is 10276; this results in a large MSE
import math
from sklearn.metrics import mean_squared_error
y5 = [10276]
y_pred5 = [9982.21]
error = mean_squared_error(y5, y_pred5)
print('MSE:', error)

import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


MSE = mean_squared_error(y4, y_pred4)
MAE = mean_absolute_error(y4, y_pred4)
RMSE = math.sqrt(MSE)

print("MSE: ", round(MSE,2))
print("MAE: ", round(MAE,2))
print("RMSE: ", round(RMSE,2))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X4, y4, test_size=0.4, random_state=4)

linreg.fit(X_train, y_train)
linreg.score(X_test, y_test)
#Although the MSE is high, using train-text-split suggests the model has an accuracy of 0.80