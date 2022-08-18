import numpy as np
import pandas as pd

purchase_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_02_PDDE.csv", low_memory = False)
goods_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_04_PD_CLAC.csv",low_memory = False)

# pd_c에 맞는 카테고리 병합
purchase = pd.merge(left=purchase_info, right=goods_info, how='inner', on='pd_c')
# de_dt칼럼을 str로 변경
purchase['de_dt'] = purchase['de_dt'].astype('str')
# de_dt칼럼의 dtype을 datetime으로 변경
purchase['de_dt'] = pd.to_datetime(purchase['de_dt'])
# 날짜별로 정렬
purchase.sort_values(by=['de_dt', 'de_hr'], inplace=True)
purchase.to_pickle('./purchase.pickle')

