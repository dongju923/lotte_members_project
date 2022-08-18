import numpy as np
import pandas as pd


associate = pd.read_pickle('./associate.pickle')

def monthly_use(kind,month):
    B01 = associate[associate['cop_c'] == kind]
    B01 = B01[['vst_dt','de_hr']]
    B01.set_index("vst_dt", inplace=True)
    if month == 2:
        days=[]
        for day in range(1, 29):
            values = B01[f'2021-{month}-{day}':f'2021-{month}-{day}'].shape[0]
            days.append(values)
        data = np.array(days)
        date = pd.date_range(f"2021-{month}-01", f"2021-{month}-28")
        df = pd.DataFrame(data, index=[date], columns=['count'])
        df.reset_index(inplace=True)
        df.columns = ['날짜','이용횟수']
        df.set_index('날짜', inplace=True)
        return df
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days=[]
        for day in range(1, 31):
            values = B01[f'2021-{month}-{day}':f'2021-{month}-{day}'].shape[0]
            days.append(values)
        data = np.array(days)
        date = pd.date_range(f"2021-{month}-01", f"2021-{month}-30")
        df = pd.DataFrame(data, index=[date], columns=['count'])
        df.reset_index(inplace=True)
        df.columns = ['날짜','이용횟수']
        df.set_index('날짜', inplace=True)
        return df
    else:
        days=[]
        for day in range(1, 32):
            values = B01[f'2021-{month}-{day}':f'2021-{month}-{day}'].shape[0]
            days.append(values)
        data = np.array(days)
        date = pd.date_range(f"2021-{month}-01", f"2021-{month}-31")
        df = pd.DataFrame(data, index=[date], columns=['count'])
        df.reset_index(inplace=True)
        df.columns = ['날짜','이용횟수']
        df.set_index('날짜', inplace=True)
        return df

def concat_df(*args):
    df = pd.concat([i for i in args],axis=1)
    return df

c0101 = monthly_use("C01", 1)
e0101 = monthly_use("E01", 1)
d0101 = monthly_use("D01", 1)
d0201 = monthly_use("D02", 1)
b0101 = monthly_use("B01", 1)
c0201 = monthly_use("C02", 1)

c0102 = monthly_use("C01", 2)
e0102 = monthly_use("E01", 2)
d0102 = monthly_use("D01", 2)
d0202 = monthly_use("D02", 2)
b0102 = monthly_use("B01", 2)
c0202 = monthly_use("C02", 2)

c0103 = monthly_use("C01", 3)
e0103 = monthly_use("E01", 3)
d0103 = monthly_use("D01", 3)
d0203 = monthly_use("D02", 3)
b0103 = monthly_use("B01", 3)
c0203 = monthly_use("C02", 3)

c0104 = monthly_use("C01", 4)
e0104 = monthly_use("E01", 4)
d0104 = monthly_use("D01", 4)
d0204 = monthly_use("D02", 4)
b0104 = monthly_use("B01", 4)
c0204 = monthly_use("C02", 4)

c0105 = monthly_use("C01", 5)
e0105 = monthly_use("E01", 5)
d0105 = monthly_use("D01", 5)
d0205 = monthly_use("D02", 5)
b0105 = monthly_use("B01", 5)
c0205 = monthly_use("C02", 5)

c0106 = monthly_use("C01", 6)
e0106 = monthly_use("E01", 6)
d0106 = monthly_use("D01", 6)
d0206 = monthly_use("D02", 6)
b0106 = monthly_use("B01", 6)
c0206 = monthly_use("C02", 6)

c0107 = monthly_use("C01", 7)
e0107 = monthly_use("E01", 7)
d0107 = monthly_use("D01", 7)
d0207 = monthly_use("D02", 7)
b0107 = monthly_use("B01", 7)
c0207 = monthly_use("C02", 7)

c0108 = monthly_use("C01", 8)
e0108 = monthly_use("E01", 8)
d0108 = monthly_use("D01", 8)
d0208 = monthly_use("D02", 8)
b0108 = monthly_use("B01", 8)
c0208 = monthly_use("C02", 8)

c0109 = monthly_use("C01", 9)
e0109 = monthly_use("E01", 9)
d0109 = monthly_use("D01", 9)
d0209 = monthly_use("D02", 9)
b0109 = monthly_use("B01", 9)
c0209 = monthly_use("C02", 9)

c0110 = monthly_use("C01", 10)
e0110 = monthly_use("E01", 10)
d0110 = monthly_use("D01", 10)
d0210 = monthly_use("D02", 10)
b0110 = monthly_use("B01", 10)
c0210 = monthly_use("C02", 10)

c0111 = monthly_use("C01", 11)
e0111 = monthly_use("E01", 11)
d0111 = monthly_use("D01", 11)
d0211 = monthly_use("D02", 11)
b0111 = monthly_use("B01", 11)
c0211 = monthly_use("C02", 11)

c0112 = monthly_use("C01", 12)
e0112 = monthly_use("E01", 12)
d0112 = monthly_use("D01", 12)
d0212 = monthly_use("D02", 12)
b0112 = monthly_use("B01", 12)
c0212 = monthly_use("C02", 12)

df1 = concat_df(c0101,e0101,d0101,d0201,b0101,c0201)
df1.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df2 = concat_df(c0102,e0102,d0102,d0202,b0102,c0202)
df2.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df3 = concat_df(c0103,e0103,d0103,d0203,b0103,c0203)
df3.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df4 = concat_df(c0104,e0104,d0104,d0204,b0104,c0204)
df4.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df5 = concat_df(c0105,e0105,d0105,d0205,b0105,c0205)
df5.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df6 = concat_df(c0106,e0106,d0106,d0206,b0106,c0206)
df6.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df7 = concat_df(c0107,e0107,d0107,d0207,b0107,c0207)
df7.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df8 = concat_df(c0108,e0108,d0108,d0208,b0108,c0208)
df8.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df9 = concat_df(c0109,e0109,d0109,d0209,b0109,c0209)
df9.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df10 = concat_df(c0110,e0110,d0110,d0210,b0110,c0210)
df10.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df11 = concat_df(c0111,e0111,d0111,d0211,b0111,c0211)
df11.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df12 = concat_df(c0112,e0112,d0112,d0212,b0112,c0212)
df12.columns = ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2']

df1.to_pickle('../data/associate_uses_1.pickle')
df2.to_pickle('../data/associate_uses_2.pickle')
df3.to_pickle('../data/associate_uses_3.pickle')
df4.to_pickle('../data/associate_uses_4.pickle')
df5.to_pickle('../data/associate_uses_5.pickle')
df6.to_pickle('../data/associate_uses_6.pickle')
df7.to_pickle('../data/associate_uses_7.pickle')
df8.to_pickle('../data/associate_uses_8.pickle')
df9.to_pickle('../data/associate_uses_9.pickle')
df10.to_pickle('../data/associate_uses_10.pickle')
df11.to_pickle('../data/associate_uses_11.pickle')
df12.to_pickle('../data/associate_uses_12.pickle')