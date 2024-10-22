import pandas as pd
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'
df['hour'] = df['hour_beginning'].dt.hour
df['time_of_day'] = df['hour'].apply(categorize_time_of_day)
time_of_day_grouped = df.groupby('time_of_day')['Pedestrians'].sum()
plt.figure(figsize=(10, 6))
plt.bar(time_of_day_grouped.index, time_of_day_grouped.values, color='skyblue')
plt.title('Pedestrian Activity Patterns Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrian Counts')
plt.grid(True)
plt.show()
