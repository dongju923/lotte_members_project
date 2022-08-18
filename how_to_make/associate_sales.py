import numpy as np
import pandas as pd

associate = pd.read_pickle('./associate.pickle')
# 그룹사별 매출 총액
C01 = associate[associate['cop_c'] == 'C01'][['vst_dt','buy_am']].groupby('vst_dt').sum()
E01 = associate[associate['cop_c'] == 'E01'][['vst_dt','buy_am']].groupby('vst_dt').sum()
D01 = associate[associate['cop_c'] == 'D01'][['vst_dt','buy_am']].groupby('vst_dt').sum()
D02 = associate[associate['cop_c'] == 'D02'][['vst_dt','buy_am']].groupby('vst_dt').sum()
B01 = associate[associate['cop_c'] == 'B01'][['vst_dt','buy_am']].groupby('vst_dt').sum()
C02 = associate[associate['cop_c'] == 'C02'][['vst_dt','buy_am']].groupby('vst_dt').sum()

df = pd.concat([C01,E01,D01,D02,B01,C02],axis=1)
df.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']
df.drop(['2020-12-31'])
df.to_pickle('../data/associate_sales.pickle')