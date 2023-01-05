import pandas as pd
import numpy as np
import json
from datetime import datetime

date = datetime.today().strftime("%Y%m%d")

# 레시피 관련 모든 크롤링 raw data 불러오기
with open(f'crawling_result/{date}_bbcgoodfood_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df1 = pd.DataFrame(raw_data["bbcgoodfood"])
df1 = df1[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_feastingathome_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df2 = pd.DataFrame(raw_data["feastingathome"])
df2 = df2[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_lazycatkitchen_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df3 = pd.DataFrame(raw_data["lazycatkitchen"])
df3 = df3[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_lovingitvegan_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df4 = pd.DataFrame(raw_data["lovingitvegan"])
df4 = df4[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_minimalistbaker_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df5 = pd.DataFrame(raw_data['minimalistbaker'])
df5 = df5[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_myplate_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df6 = pd.DataFrame(raw_data["myplate"])
df6 = df6[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_pickuplimes_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df7 = pd.DataFrame(raw_data["pickuplimes"])
df7 = df7[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_skinnytaste_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df8 = pd.DataFrame(raw_data["skinnytaste"])
df8 = df8[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]

with open(f'crawling_result/{date}_thecuriouschickpea_all.json', 'r', encoding='utf-8-sig') as file:
    raw_data = json.load(file)
df9 = pd.DataFrame(raw_data["thecuriouschickpea"])
df9 = df9[['site', 'title', 'ingredients', 'time', 'serving', 'recipe', 'calories', 'carbs', 'protein', 'total_fat', 'image']]


# 모든 데이터셋 합치기
# ignore_index를 사용하지 않으면 기존에 사용하는 인덱스 정보를 가져온다
df_all = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True)

# null 값 지우기 (기준은 'title', 'ingredients', 'recipe')
df_all = df_all.dropna(subset=['title', 'ingredients', 'recipe'])

# json 저장
df_all.to_json(r'C:\Users\Lenovo\Desktop\raw_data\vegan_recipe_all.json', orient='records')

# csv 저장
# df_all.to_csv(r'C:\Users\Lenovo\Desktop\raw_data\vegan_recipe_all.csv', encoding='utf-8-sig')
