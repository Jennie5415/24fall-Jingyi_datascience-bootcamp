import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df['year'] = df['hour_beginning'].dt.year
brooklyn_2019_df = df[(df['location'] == 'Brooklyn Bridge') & (df['year'] == 2019)]
brooklyn_2019_df[['weather_summary', 'Pedestrians']].dropna()
weather_grouped = brooklyn_2019_df.groupby('weather_summary')['Pedestrians'].sum()
numeric_cols = brooklyn_2019_df[['Pedestrians', 'temperature', 'precipitation']].dropna()
correlation_matrix = numeric_cols.corr()
print(correlation_matrix)
