import numpy as np
import pandas as pd

#데이터 로드
purchase = pd.read_pickle("./purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)

# 여성인 데이터만 가져옴
w_val = person_info.loc[(person_info['ma_fem_dv'] == '여성')]['cust'].values
w = purchase[purchase['cust'].isin(w_val)]

annual_purchase = w[['de_dt','buy_ct']]
annual_purchase.columns = ['날짜','구매수량']
# 날짜로 그룹화
annual_purchase = annual_purchase[['날짜','구매수량']].groupby('날짜').sum()
annual_purchase.to_pickle('../data/women_purchase.pickle')