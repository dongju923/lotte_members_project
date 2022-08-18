import numpy as np
import pandas as pd

# 데이터 로드
purchase = pd.read_pickle("./purchase.pkl")
# 오프라인
offline_purchase = purchase[purchase['chnl_dv'] == 1]

offline_purchase.rename(columns={"de_dt":"날짜", "buy_ct":"수량"}, inplace=True)
annual_offline_purchase = offline_purchase[["날짜","수량"]].groupby('날짜').sum()
annual_offline_purchase.to_pickle('../data/offline_purchase.pickle')