import numpy as np
import pandas as pd

purchase = pd.read_pickle("./purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)


m20_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '20대')]['cust'].values
m30_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '30대')]['cust'].values
m40_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '40대')]['cust'].values
m50_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '50대')]['cust'].values
m60_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '60대')]['cust'].values
m70_value = person_info.loc[(person_info['ma_fem_dv'] == '남성') & (person_info['ages'] == '70대')]['cust'].values

m20 = purchase[purchase['cust'].isin(m20_value)]
m30 = purchase[purchase['cust'].isin(m30_value)]
m40 = purchase[purchase['cust'].isin(m40_value)]
m50 = purchase[purchase['cust'].isin(m50_value)]
m60 = purchase[purchase['cust'].isin(m60_value)]
m70 = purchase[purchase['cust'].isin(m70_value)]

g20 = m20[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g30 = m30[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g40 = m40[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g50 = m50[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g60 = m60[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g70 = m70[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
df = pd.concat([g20,g30,g40,g50,g60,g70],axis=1)
df.columns = ['20대','30대','40대','50대','60대','70대']
df.to_pickle('../data/age_man_hours_purchase.pickle')