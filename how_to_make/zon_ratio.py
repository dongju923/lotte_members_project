import numpy as np
import pandas as pd

purchase = pd.read_pickle("./purchase.pkl")
local_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_05_BR.csv", low_memory = False)

local = pd.merge(left=purchase, right=local_info, how='inner', on=['br_c', 'cop_c'])[['zon_hlv']]
# 지역별 인구수
z07 = local.loc[(local['zon_hlv'] == 'Z07')]['cust'].values
z12 = local.loc[(local['zon_hlv'] == 'Z12')]['cust'].values
z11 = local.loc[(local['zon_hlv'] == 'Z11')]['cust'].values
z17 = local.loc[(local['zon_hlv'] == 'Z17')]['cust'].values
z10 = local.loc[(local['zon_hlv'] == 'Z10')]['cust'].values
z05 = local.loc[(local['zon_hlv'] == 'Z05')]['cust'].values
z16 = local.loc[(local['zon_hlv'] == 'Z16')]['cust'].values
z03 = local.loc[(local['zon_hlv'] == 'Z03')]['cust'].values
z06 = local.loc[(local['zon_hlv'] == 'Z06')]['cust'].values
z14 = local.loc[(local['zon_hlv'] == 'Z14')]['cust'].values
z01 = local.loc[(local['zon_hlv'] == 'Z01')]['cust'].values
z04 = local.loc[(local['zon_hlv'] == 'Z04')]['cust'].values
z09 = local.loc[(local['zon_hlv'] == 'Z09')]['cust'].values
z15 = local.loc[(local['zon_hlv'] == 'Z15')]['cust'].values
z08 = local.loc[(local['zon_hlv'] == 'Z08')]['cust'].values
z13 = local.loc[(local['zon_hlv'] == 'Z13')]['cust'].values
z02 = local.loc[(local['zon_hlv'] == 'Z02')]['cust'].values
# 지역별 인구수를 리스트에 저장
lst = [z01, z02, z03, z04, z05, z06, z07, z08, z09, z10, z11, z12, z13, z14, z15, z16, z17]
# 중복되지 않은 값만 저장
data = []
for i in lst:
    a = len(set(i))
    data.append(a)
# 지역종류 리스트에 저장
value = local['zon_hlv'].unique()

# 데이터프레임으로 저장
df = pd.DataFrame({'Local': [l for l in value],
              'value': [d for d in data]})

df.to_pickle('../data/zon_ratio.pickle')