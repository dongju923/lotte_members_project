import numpy as np
import pandas as pd

purchase = pd.read_pickle("./purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)


w20_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '20대')]['cust'].values
w30_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '30대')]['cust'].values
w40_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '40대')]['cust'].values
w50_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '50대')]['cust'].values
w60_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '60대')]['cust'].values
w70_value = person_info.loc[(person_info['ma_fem_dv'] == '여성') & (person_info['ages'] == '70대')]['cust'].values

w20 = purchase[purchase['cust'].isin(w20_value)]
w30 = purchase[purchase['cust'].isin(w30_value)]
w40 = purchase[purchase['cust'].isin(w40_value)]
w50 = purchase[purchase['cust'].isin(w50_value)]
w60 = purchase[purchase['cust'].isin(w60_value)]
w70 = purchase[purchase['cust'].isin(w70_value)]

g20 = w20[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g30 = w30[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g40 = w40[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g50 = w50[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g60 = w60[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
g70 = w70[['de_hr','buy_ct']].groupby('de_hr').sum().sort_values('buy_ct', ascending=False)
df = pd.concat([g20,g30,g40,g50,g60,g70],axis=1)
df.columns = ['20대','30대','40대','50대','60대','70대']
df.to_pickle('../data/age_women_hours_purchase.pickle')