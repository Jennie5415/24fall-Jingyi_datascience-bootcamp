import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df=df.loc[::20,['Manufacturer', 'Model', 'Type']]
print(filtered_df)
