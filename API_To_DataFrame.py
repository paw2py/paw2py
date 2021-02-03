import pandas as pd
import json
import requests


r = requests.get('rest api url')
x = r.json()
df = pd.DataFrame(x['data'])
df['com_len'] = df['title'].apply(len) #length of each titile in the data frame added a new column to df
dfnew =df.sort_values(by=['num_comments','com_len'], ascending=[False,True])


#print top two records from df
print(dfnew[['title','num_comments','com_len']].head(2))