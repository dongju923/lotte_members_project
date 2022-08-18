import numpy as np
import pandas as pd

# 데이터 로드
purchase = pd.read_pickle("./purchase.pkl")
# 오프라인
online_purchase = purchase[purchase['chnl_dv'] == 2]

online_purchase.rename(columns={"de_dt":"날짜", "buy_ct":"수량"}, inplace=True)
annual_online_purchase = online_purchase[["날짜","수량"]].groupby('날짜').sum()
annual_online_purchase.to_pickle('../data/online_purchase.pickle')