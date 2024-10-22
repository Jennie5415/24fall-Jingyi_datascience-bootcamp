import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
import matplotlib.pyplot as plt
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df['day_of_week'] = df['hour_beginning'].dt.day_name()
weekday_df = df[df['day_of_week'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]
weekday_grouped = weekday_df.groupby('day_of_week')['Pedestrians'].sum()
weekday_grouped = weekday_grouped.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
plt.figure(figsize=(10, 6))
plt.plot(weekday_grouped.index, weekday_grouped.values, marker='o')
plt.title('Pedestrian Counts for Each Weekday')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Counts')
plt.grid(True)
plt.show()
