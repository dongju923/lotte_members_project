import numpy as np
import pandas as pd


purchase = pd.read_pickle("./how_to_make/purchase.pkl")
local_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_05_BR.csv", low_memory = False)
local = pd.merge(left=purchase, right=local_info, how='inner', on=['br_c', 'cop_c'])[['pd_nm','buy_ct', 'zon_hlv', 'buy_am']]

# 가격과 수량을 곱해서 매출 칼럼을 생성
local['total_am'] = (local['buy_am'] * local['buy_ct']).astype('int')
local.rename(columns={'total_am': '매출액', 'pd_nm': '품목'}, inplace=True)

# 지역에 맞게 품목으로 그룹화 한후 매출액으로 정렬
def make_df(zon):
    value = local[local['zon_hlv'] == zon].drop(['buy_am', 'buy_ct'], axis=1).groupby('품목').sum().sort_values('매출액', ascending=False)
    return value

z01 = make_df("Z01")
z02 = make_df("Z02")
z03 = make_df("Z03")
z04 = make_df("Z04")
z05 = make_df("Z05")
z06 = make_df("Z06")
z07 = make_df("Z07")
z08 = make_df("Z08")
z09 = make_df("Z09")
z10 = make_df("Z10")
z11 = make_df("Z11")
z12 = make_df("Z12")
z13 = make_df("Z13")
z14 = make_df("Z14")
z15 = make_df("Z15")
z16 = make_df("Z16")
z17 = make_df("Z17")

df = pd.concat([z01,z02,z03,z04,z05,z06,z07,z08,z09,z10,z11,z12,z13,z14,z15,z16,z17], axis=1)
df.columns = ['Z01','Z02','Z03','Z04','Z05','Z06','Z07','Z08','Z09','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17']

df.to_pickle("../data/zon_sales.pickle")