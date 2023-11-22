import pandas as pd
import numpy as np

speed_test = {
'time' : [10.40, 10.51, 11.16],
'download_speed' : [ 10.35, 41.48, 4.48],
'upload_speed' : [7.38, 7.60, 7.34],
'idle_latency' : [8, 9, 11]
}

# df=pd.DataFrame(speed_test)
# print(df)
# #this has created a data frame with mobile speed activity.

df=pd.DataFrame(speed_test)
print(df)
#this has created a data frame with mobile speed activity.

#Append the dataframe with Mean, Mode & Median - of the 3 measurements over every attempt
## 1 - create DataFrame with each; Mean, Mode & Median
mean_row = pd.DataFrame({
    "download_mean_speed" :[df['download_speed'].mean()],
    "upload_mean_speed" : [df['upload_speed'].mean()],
    "idle_latency_mean_speed" : [df['idle_latency'].mean()]
})

mode_row = pd.DataFrame({
    "download_mode_speed" : [df['download_speed'].mode()],
    "upload_mode_speed" : [df['upload_speed'].mode()],
    "idle_mode_latency" : [df['idle_latency'].mode()]
})

median_row = pd.DataFrame({
    "download_median_speed" : [df['download_speed'].median()],
    "upload_median_speed" : [df['upload_speed'].median()],
    "idle_median_latency" : [df['idle_latency'].median()]
})

print(df)

# 2 - then need to add them as a new row:
df.loc[4] = ['mean row', mean_row['download_mean_speed'].values[0], mean_row['upload_mean_speed'].values[0], mean_row['idle_latency_mean_speed'].values[0]]
df.loc[5] = ['mode row', mode_row['download_mode_speed'].values[0], mode_row['upload_mode_speed'].values[0], mode_row['idle_mode_latency'].values[0]]
df.loc[6] = ['median row', median_row['download_median_speed'].values[0], median_row['upload_median_speed'].values[0], median_row['idle_median_latency'].values[0]]
print(df)




