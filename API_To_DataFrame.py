import pandas as pd
import json
import requests
#test nwe

r = requests.get('https://jsonmock.hackerrank.com/api/articles?page=2')
x = r.json()
df = pd.DataFrame(x['data'])
df['com_len'] = df['title'].apply(len) 
dfnew =df.sort_values(by=['num_comments','com_len'], ascending=[False,True])


#print top two records from df
print(dfnew[['title','num_comments','com_len']].head(2))
