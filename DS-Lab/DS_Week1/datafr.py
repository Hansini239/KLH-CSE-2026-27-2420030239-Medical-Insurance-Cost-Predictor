import pandas as pd
data = { 'apples':[3,2,0,1],'oranges': [0,3,7,2] }
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index = ['ahmad','ali','rashed','hamza'])
print(df)
# df.loc['ali']
print(df.loc['ali'])
data = { 'col1':[3,2,1,0],'col2':['a','b','c','d']}
print(pd.DataFrame.from_dict(data))
print()
print(pd.DataFrame.from_dict(data,orient='index'))
print()
print(pd.DataFrame.from_dict(data,orient='index',columns=['A','B','C','D']))
print()