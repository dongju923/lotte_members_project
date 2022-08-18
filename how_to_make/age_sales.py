import numpy as np
import pandas as pd

purchase = pd.read_pickle("./how_to_make/purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)

# 매출액 데이터프레임 만드는 함수
def make_df(gender, age):
    value = person_info.loc[(person_info['ma_fem_dv'] == gender) & (person_info['ages'] == age)]['cust'].values
    data = purchase[purchase['cust'].isin(value)][['pd_nm','buy_ct', 'buy_am']]
    data['total_am'] = (data['buy_am'] * data['buy_ct']).astype('int')
    data.rename(columns={'total_am': '매출액', 'pd_nm': '품목'}, inplace=True)
    df = data[['품목','매출액']].groupby('품목').sum().sort_values('매출액', ascending=False)
    return df

# concat하는 함수
def concat(*args):
    df = pd.concat(args,axis=1)
    df.columns = ["남자","여자"]
    return df

m20 = make_df("남성", "20대")
w20 = make_df("여성", "20대")
m30 = make_df("남성", "30대")
w30 = make_df("여성", "30대")
m40 = make_df("남성", "40대")
w40 = make_df("여성", "40대")
m50 = make_df("남성", "50대")
w50 = make_df("여성", "50대")
m60 = make_df("남성", "60대")
w60 = make_df("여성", "60대")
m70 = make_df("남성", "70대")
w70 = make_df("여성", "70대")

age20 = concat(m20,w20)
age30 = concat(m30,w30)
age40 = concat(m40,w40)
age50 = concat(m50,w50)
age60 = concat(m60,w60)
age70 = concat(m70,w70)

age20.to_pickle("../data/age20_sales.pickle")
age30.to_pickle("../data/age30_sales.pickle")
age40.to_pickle("../data/age40_sales.pickle")
age50.to_pickle("../data/age50_sales.pickle")
age60.to_pickle("../data/age60_sales.pickle")
age70.to_pickle("../data/age70_sales.pickle")