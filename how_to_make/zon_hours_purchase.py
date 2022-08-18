import numpy as np
import pandas as pd

purchase = pd.read_pickle("./purchase.pkl")
local_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_05_BR.csv", low_memory = False)
person_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_01_DEMO.csv", low_memory = False)

local = pd.merge(left=purchase, right=local_info, how='inner', on=['br_c', 'cop_c'])[['de_hr','buy_ct','zon_hlv']]
local.rename(columns={'buy_ct': '구매수량', 'de_hr': '시간'}, inplace=True)

z10 = local[local['zon_hlv'] == 'Z10'].groupby('시간').sum()
z16 = local[local['zon_hlv'] == 'Z16'].groupby('시간').sum()
z08 = local[local['zon_hlv'] == 'Z08'].groupby('시간').sum()
z11 = local[local['zon_hlv'] == 'Z11'].groupby('시간').sum()
z01 = local[local['zon_hlv'] == 'Z01'].groupby('시간').sum()
z12 = local[local['zon_hlv'] == 'Z12'].groupby('시간').sum()
z17 = local[local['zon_hlv'] == 'Z17'].groupby('시간').sum()
z07 = local[local['zon_hlv'] == 'Z07'].groupby('시간').sum()
z15 = local[local['zon_hlv'] == 'Z15'].groupby('시간').sum()
z14 = local[local['zon_hlv'] == 'Z14'].groupby('시간').sum()
z13 = local[local['zon_hlv'] == 'Z13'].groupby('시간').sum()
z04 = local[local['zon_hlv'] == 'Z04'].groupby('시간').sum()
z06 = local[local['zon_hlv'] == 'Z06'].groupby('시간').sum()
z03 = local[local['zon_hlv'] == 'Z03'].groupby('시간').sum()
z09 = local[local['zon_hlv'] == 'Z09'].groupby('시간').sum()
z05 = local[local['zon_hlv'] == 'Z05'].groupby('시간').sum()
z02 = local[local['zon_hlv'] == 'Z02'].groupby('시간').sum()

df = pd.concat([z01,z02,z03,z04,z05,z06,z07,z08,z09,z10,z11,z12,z13,z14,z15,z16,z17], axis=1)
df.columns = ['Z01','Z02','Z03','Z04','Z05','Z06','Z07','Z08','Z09','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17']
df.to_pickle('../data/zon_hours_purchase.pickle')