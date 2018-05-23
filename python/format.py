import pandas as pd
import numpy as np 

df = pd.read_csv('result.csv', header=None)
df.columns = ['x1','y1','x2','y2','dist','score','dir']
print(df.head())
df['dir'] = df['dir'].map({'right':0,'left':1,'up':2,'down':3})
print(df.head())
print(df.tail())
print(df['dir'])
df.to_json('data.json')