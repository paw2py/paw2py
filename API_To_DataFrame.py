import pandas as pd
import json
import requests


r = requests.get('rest api url')
x = r.json()
df = pd.DataFrame(x['data'])
#
print(df.head(5))