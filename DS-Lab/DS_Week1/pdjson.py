import pandas as pd
df = pd.reas_json('sample1.json')


#convert csv to json
df.to_csv('new_dataset.csv')

#convert json to csv
df.to_json('new_dataset.json')

temp_df.drop_duplicates(inplace=True)
