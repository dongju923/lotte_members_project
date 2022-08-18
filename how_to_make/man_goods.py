import numpy as np
import pandas as pd

# 데이터 로드
purchase = pd.read_pickle("./purchase.pkl")
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)

# 남성인 데이터만 가져옴
m_val = person_info.loc[(person_info['ma_fem_dv'] == '남성')]['cust'].values
m = purchase[purchase['cust'].isin(m_val)]
# 3개의 칼럼만 사용하고 de_dt를 인덱스로 설정
goods = m[['pd_nm','buy_ct', 'de_dt']]
goods.set_index('de_dt', inplace=True)
# 월별 상품 판매수 
m1_goods = goods['2021-01-01' : '2021-01-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m2_goods = goods['2021-02-01' : '2021-02-28'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m3_goods = goods['2021-03-01' : '2021-03-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m4_goods = goods['2021-04-01' : '2021-04-30'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m5_goods = goods['2021-05-01' : '2021-05-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m6_goods = goods['2021-06-01' : '2021-06-30'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m7_goods = goods['2021-07-01' : '2021-07-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m8_goods = goods['2021-08-01' : '2021-08-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m9_goods = goods['2021-09-01' : '2021-09-30'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m10_goods = goods['2021-10-01' : '2021-10-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m11_goods = goods['2021-11-01' : '2021-11-30'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
m12_goods = goods['2021-12-01' : '2021-12-31'].groupby('pd_nm').sum().sort_values('buy_ct', ascending=False)
# 데이터를 합침
df = pd.concat([m1_goods,m2_goods,m3_goods,m4_goods,m5_goods,m6_goods,m7_goods,m8_goods,m9_goods,m10_goods,m11_goods,m12_goods], axis=1)
# 칼럼명 변경
df.columns = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
# 데이터 저장
df.to_pickle('../data/man_goods.pickle')