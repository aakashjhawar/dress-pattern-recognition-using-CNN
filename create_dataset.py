import numpy as np
import pandas as pd
import requests
import os

dress_patterns_df = pd.read_csv('dress_patterns.csv')
dress_patterns = dress_patterns_df .values

# category
category = set(dress_patterns_df['category'])
print(category)

#create a folder dataset and nested folder of category
print(os.listdir())
os.mkdir('dataset_category')

for cat in category:
    print(cat)
    os.mkdir('dataset_category/'+cat)

print(os.listdir('dataset_category'))



# save image in respective category folder.

for i in range(len(dress_patterns)):
  if i%5 == 0:
    print(i, '/', len(dress_patterns))
  pattern = dress_patterns[i]
  url = pattern[3]
  unit_id = pattern[0]
  category = pattern[1]
  try:
    r = requests.get(url, allow_redirects=True)
    open('dataset_category/'+category+'/'+str(unit_id)+'.jpg', 'wb').write(r.content)
  except:
    print('ERROR at: ', i)

