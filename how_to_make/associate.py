import numpy as np
import pandas as pd

cop_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_03_COP_U.csv", low_memory = False)
com_info = pd.read_csv("../dataset/LPOINT_BIG_COMP_05_BR.csv", low_memory = False)

associate = pd.merge(left=cop_info, right=com_info, how='inner', on=['br_c','cop_c'])
# de_dt칼럼을 str로 변경
associate['de_dt'] = associate['de_dt'].astype('str')
associate['vst_dt'] = associate['vst_dt'].astype('str')
# de_dt칼럼의 dtype을 datetime으로 변경
associate['de_dt'] = pd.to_datetime(associate['de_dt'])
associate['vst_dt'] = pd.to_datetime(associate['vst_dt'])
# 날짜별로 정렬
associate.sort_values(by=['de_dt', 'de_hr'], inplace=True)
associate.to_pickle('./associate.pickle')
