import numpy as np
import pandas as pd

#데이터 로드
purchase = pd.read_pickle("./purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)

# 남성인 데이터만 가져옴
m_val = person_info.loc[(person_info['ma_fem_dv'] == '남성')]['cust'].values
m = purchase[purchase['cust'].isin(m_val)]

annual_purchase = m[['de_hr','buy_ct']]
annual_purchase.columns = ['날짜','구매수량']
# 날짜로 그룹화
annual_purchase = annual_purchase[['시간','구매수량']].groupby('시간').sum()
annual_purchase.to_pickle('../data/man_hours_purchase.pickle')
