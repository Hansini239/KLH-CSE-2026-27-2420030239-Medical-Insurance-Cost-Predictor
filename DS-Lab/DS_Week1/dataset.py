import pandas as pd

# df = pd.read_csv('Iris.csv')
# print(df)
# or
df = pd.read_csv('Iris.csv',index_col=0)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.shape)