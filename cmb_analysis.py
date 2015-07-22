import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bagels-all.csv')

df
df.columns
df.dtypes
df.describe()


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
###


df[['Age_Num','CountI']]

###

df['Age'].values
e_age = df['Age'].values
n_ages = []
for e in e_age:
    n_ages.append(int(e.split(' ')[0]))
df['Age_Num'] = pd.Series(n_ages)
len(n_ages)

df['CountI'] = pd.Series([1] * 99)

int(df['Height'].values[0].split("\'")[0])*12
int(df['Height'].values[0].split("\'")[1].replace('\"',''))

n_heights = []
e_heights = df['Height'].values
for e in e_heights:
    f_inches = int(e.split("\'")[0])*12
    i_inches = int(e.split("\'")[1].replace('\"',''))
    n_heights.append(f_inches + i_inches)
df['Height_N'] = pd.Series(n_heights)

###


plt.figure()
df['Age_Num'].describe()
df['Age_Num'].mean()
df['Age_Num'].diff().hist()
# df['Age_Num'].plot(kind='bar')
df['Age_Num'].hist()
# df.Age_Num.hist()

df['Height_N'].describe()
df['Height_N'].diff().hist()

df.groupby('Age_Num').CountI.sum()

df.groupby('Nationality').CountI.sum().plot(kind='bar')
df.groupby('Religion').CountI.sum().plot(kind='bar')
df.groupby('Religion').CountI.sum().plot(kind='pie')


# df.groupby('Age_Num').agg([np.sum])

# pd.Series.plot(df['Age_Num'],kind='bar')

### Report

df['Age_Num'].describe()
plt.figure()
df.groupby('Age_Num').CountI.sum().plot(kind='bar')
plt.show()
plt.figure()
df['Age_Num'].diff().hist()
plt.show()


df.groupby('Nationality').CountI.sum().plot(kind='bar');
plt.tight_layout()
plt.show();

df.groupby('Religion').CountI.sum().plot(kind='bar');
plt.tight_layout()
plt.show();

df.groupby('Religion').CountI.sum().plot(kind='pie'); plt.show();


plt.figure()
# df.groupby('Age_Num').CountI.sum().plot(kind='bar')
df.groupby('Height').CountI.sum().plot(kind='bar')
plt.show()


df['Height_N'].describe()
df['Height_N'].diff().hist()
plt.show()


###
# import matplotlib.pyplot as plt
# import numpy as np
#
# #mu, sigma = 100, 15
# #x = mu + sigma * np.random.randn(10000)
# hist, bins = np.histogram(n_ages, bins=10)
# width = 0.7 * (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# plt.bar(center, hist, align='center', width=width)
# plt.show()