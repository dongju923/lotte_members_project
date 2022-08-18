import numpy as np
import pandas as pd

purchase = pd.read_pickle("./purchase.pkl")

off = purchase[purchase['chnl_dv'] == 1]
on = purchase[purchase['chnl_dv'] == 2]
off.rename(columns={"de_hr":"시간", "buy_ct":"구매수량"}, inplace=True)
on.rename(columns={"de_hr":"시간", "buy_ct":"구매수량"}, inplace=True)

off_hours = off[['시간','구매수량']].groupby("시간").sum()
on_hours = on[['시간','구매수량']].groupby("시간").sum()
off_hours.to_pickle("..data/offline_hours_purchase.pickle")
on_hours.to_pickle("../data/online_hours_purchase.pickle")