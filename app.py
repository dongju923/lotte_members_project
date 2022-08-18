from re import template
from attr import assoc
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from matplotlib.pyplot import bar
import pandas as pd
import plotly.express as px
import flask
import pandas as pd
import numpy as np

server = flask.Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

main_style = {'textAlign': 'center', 'color': 'black', 'fontSize': '50px', 'fontWeight': 'bold'}
sub_style = {'textAlign': 'center', 'color': 'black', 'fontSize': '25px', 'fontWeight': 'bold'}

"############################### Dash APP ################################"
goods_gender = dash.Dash(__name__, server=server, url_base_pathname='/goods/gender/')
goods_age = dash.Dash(__name__, server=server, url_base_pathname='/goods/age/')
goods_local = dash.Dash(__name__, server=server, url_base_pathname='/goods/local/')
associate_sales = dash.Dash(__name__, server=server, url_base_pathname='/associate/sales/')
associate_uses = dash.Dash(__name__, server=server, url_base_pathname='/associate/uses/')
lpay = dash.Dash(__name__, server=server, url_base_pathname='/lpay/info/')
onoff = dash.Dash(__name__, server=server, url_base_pathname='/goods/onoff/')

"###############################  UTILS ################################"
def make_line_figure(data, template='gridon'):
    return px.line(data, template = template)

def make_bar_figure(data, barmode, template='gridon'):
    return px.bar(data, barmode=barmode, template = template)

def make_pie_figure(data, values, names, template='gridon'):
    return px.pie(data, values=values, names=names, template=template)
"###############################   DATA   ##############################"
# ratio
man_women_ratio = pd.DataFrame({
    "Sex": ["남성", "여성"],
    "Amount": [9830, 20083]
})
# purchase
man_anuual_purchase = pd.read_pickle('./data/man_purchase.pickle')
women_anuual_purchase = pd.read_pickle('./data/women_purchase.pickle')
# hour_purchase
man_hour_purchase = pd.read_pickle('./data/man_hours_purchase.pickle')
women_hour_purchase = pd.read_pickle('./data/women_hours_purchase.pickle')
# goods
man_goods = pd.read_pickle('./data/man_goods.pickle')
women_goods = pd.read_pickle('./data/women_goods.pickle')
# age_ratio
age_ratio = pd.DataFrame({
    "Age": ["20대남성", "30대남성",'40대남성','50대남성','60대남성','70대남성','20대여성','30대여성','40대여성','50대여성','60대여성','70대여성'],
    "Amount": [1340,2696,3187,1718,636,253,2696,5040,6676,3915,1479,460]
})
# age_hour_purchase
age_man_hour_purchase = pd.read_pickle('./data/age_man_hours_purchase.pickle')
age_women_hour_purchase = pd.read_pickle('./data/age_women_hours_purchase.pickle')
# age_purchase
age_man_purchase = pd.read_pickle('./data/age_man_purchase.pickle')
age_women_purchase = pd.read_pickle('./data/age_women_purchase.pickle')
# age_goods
age_man_goods = pd.read_pickle('./data/age_man_goods.pickle')
age_women_goods = pd.read_pickle('./data/age_women_goods.pickle')
# age_sales
age20_sales = pd.read_pickle('./data/age20_sales.pickle')
age30_sales = pd.read_pickle('./data/age30_sales.pickle')
age40_sales = pd.read_pickle('./data/age40_sales.pickle')
age50_sales = pd.read_pickle('./data/age50_sales.pickle')
age60_sales = pd.read_pickle('./data/age60_sales.pickle')
age70_sales = pd.read_pickle('./data/age70_sales.pickle')
# zon_ratio
zon_ratio = pd.read_pickle('./data/zon_ratio.pickle')
# zon_hour_purchase
zon_hour_purchase = pd.read_pickle('./data/zon_hours_purchase.pickle')
# zon_purchase
zon_purchase = pd.read_pickle('./data/zon_purchase.pickle')
# zon_goods
zon_goods = pd.read_pickle('./data/zon_goods.pickle')
# zon_sales
zon_sales = pd.read_pickle('./data/zon_sales.pickle')
# associate_ratio
associate_ratio = pd.DataFrame({
    "Associate": ['엔터테인먼트1','렌탈업종','F&B1','F&B2','숙박업종','엔터테인먼트2'],
    "Amount": [9885,941,15106,10311,2199,4790]
})
# associate_sales
associate_s = pd.read_pickle('./data/associate_sales.pickle')
# associate_uses
associate_uses_1 = pd.read_pickle('./data/associate_uses_1.pickle')
associate_uses_2 = pd.read_pickle('./data/associate_uses_2.pickle')
associate_uses_3 = pd.read_pickle('./data/associate_uses_3.pickle')
associate_uses_4 = pd.read_pickle('./data/associate_uses_4.pickle')
associate_uses_5 = pd.read_pickle('./data/associate_uses_5.pickle')
associate_uses_6 = pd.read_pickle('./data/associate_uses_6.pickle')
associate_uses_7 = pd.read_pickle('./data/associate_uses_7.pickle')
associate_uses_8 = pd.read_pickle('./data/associate_uses_8.pickle')
associate_uses_9 = pd.read_pickle('./data/associate_uses_9.pickle')
associate_uses_10 = pd.read_pickle('./data/associate_uses_10.pickle')
associate_uses_11 = pd.read_pickle('./data/associate_uses_11.pickle')
associate_uses_12 = pd.read_pickle('./data/associate_uses_12.pickle')
# lpay_ratio
lpay_ratio = pd.read_pickle('./data/lpay_ratio.pickle')
# lapy_onoff_ratio
lapy_onoff_ratio = pd.DataFrame({"Info": ["온라인","오프라인"],
                   "Amount": [203174, 150010]})
# goods_onoff
goods_onoff_ratio = pd.DataFrame({"Info": ["온라인","오프라인"],
                   "Amount": [428501, 3953242]})
# online_purchase
online_purchase = pd.read_pickle('./data/online_purchase.pickle')
# offline_purchase
offline_purchase = pd.read_pickle('./data/offline_purchase.pickle')
# offline_hours_purchase
offline_hours_purchase = pd.read_pickle('./data/offline_hours_purchase.pickle')
# online_hours_purchase
online_hours_purchase = pd.read_pickle('./data/online_hours_purchase.pickle')
"###############################  FIGURE  ##############################"
# ratio
man_women_ratio_fig = make_pie_figure(man_women_ratio, values ="Amount", names='Sex')
# purchase
man_anuual_purchase_fig = make_line_figure(man_anuual_purchase)
women_anuual_purchase_fig = make_line_figure(women_anuual_purchase)
# hour_purchase
man_hour_purchase_fig = make_line_figure(women_hour_purchase)
women_hour_purchase_fig = make_line_figure(women_hour_purchase)
# goods
man_goods_fig = make_line_figure(man_goods)
women_goods_fig = make_line_figure(women_goods)
# age_ratio
age_ratio_fig = make_pie_figure(age_ratio, values ="Amount", names='Age')
# age_hour_purchase
age_man_hour_purchase_fig = make_line_figure(age_man_hour_purchase)
age_women_hour_purchase_fig = make_line_figure(age_women_hour_purchase)
# age_purchase
age_man_purchase_fig = make_line_figure(age_man_purchase)
age_women_purchase_fig = make_line_figure(age_women_purchase)
# age_goods
age_man_goods_fig = make_bar_figure(age_man_goods, "stack")
age_women_goods_fig = make_bar_figure(age_man_goods, "stack")
# age_sales
age20_sales_fig = make_bar_figure(age20_sales, "group")
age30_sales_fig = make_bar_figure(age30_sales, "group")
age40_sales_fig = make_bar_figure(age40_sales, "group")
age50_sales_fig = make_bar_figure(age50_sales, "group")
age60_sales_fig = make_bar_figure(age60_sales, "group")
age70_sales_fig = make_bar_figure(age70_sales, "group")
# zon_ratio
zon_ratio_fig = make_pie_figure(zon_ratio, values='value', names='Local')
# zon_hour_purchase
zon_hour_purchase_fig = make_line_figure(zon_hour_purchase)
# zon_purchase
zon_purchase_fig = make_line_figure(zon_purchase)
# zon_goods
zon_goods_fig = make_line_figure(zon_goods)
# zon_sales
zon_sales_fig = make_line_figure(zon_sales)
# associate_ratio
associate_ratio_fig = make_pie_figure(associate_ratio, values='Amount', names='Associate')
# associate_sales
associate_sales_fig = make_line_figure(associate_s)
# associate_uses
associate_uses_fig1 = px.line(associate_uses_1, x=associate_uses_1.index, y=associate_uses_1.columns)
associate_uses_fig2 = px.line(associate_uses_2, x=associate_uses_2.index, y=associate_uses_2.columns)
associate_uses_fig3 = px.line(associate_uses_3, x=associate_uses_3.index, y=associate_uses_3.columns)
associate_uses_fig4 = px.line(associate_uses_4, x=associate_uses_4.index, y=associate_uses_4.columns)
associate_uses_fig5 = px.line(associate_uses_5, x=associate_uses_5.index, y=associate_uses_5.columns)
associate_uses_fig6 = px.line(associate_uses_6, x=associate_uses_6.index, y=associate_uses_6.columns)
associate_uses_fig7 = px.line(associate_uses_7, x=associate_uses_7.index, y=associate_uses_7.columns)
associate_uses_fig8 = px.line(associate_uses_8, x=associate_uses_8.index, y=associate_uses_8.columns)
associate_uses_fig9 = px.line(associate_uses_9, x=associate_uses_9.index, y=associate_uses_9.columns)
associate_uses_fig10 = px.line(associate_uses_10, x=associate_uses_10.index, y=associate_uses_10.columns)
associate_uses_fig11 = px.line(associate_uses_11, x=associate_uses_11.index, y=associate_uses_11.columns)
associate_uses_fig12 = px.line(associate_uses_12, x=associate_uses_12.index, y=associate_uses_12.columns)
# lpay_ratio
lpay_ratio_fig = make_pie_figure(lpay_ratio, values="Amount", names="Info")
# lapy_onoff_ratio
lapy_onoff_ratio_fig = make_pie_figure(lapy_onoff_ratio, values="Amount", names="Info")
# goods_onoff
goods_onoff_ratio_fig = make_pie_figure(goods_onoff_ratio, values="Amount", names="Info")
# online_purchase
online_purchase_fig = make_line_figure(online_purchase)
# offline_purchase
offline_purchase_fig = make_line_figure(offline_purchase)
# offline_hours_purchase
offline_hours_purchase_fig = make_line_figure(offline_hours_purchase)
# online_hours_purchase
online_hours_purchase_fig = make_line_figure(online_hours_purchase)
"###############################  UPDATE LAYOUT  ##############################"
#goods
man_anuual_purchase_fig.update_traces(line_color='yellowgreen')
women_anuual_purchase_fig['data'][0]['line']['color']='rgb(204, 204, 204)'
man_goods_fig.update_yaxes(tickformat=',')
women_goods_fig.update_yaxes(tickformat=',')
age_man_goods_fig.update_yaxes(tickformat=',')
age_women_goods_fig.update_yaxes(tickformat=',')
age20_sales_fig.update_yaxes(tickformat=',')
age30_sales_fig.update_yaxes(tickformat=',')
age40_sales_fig.update_yaxes(tickformat=',')
age50_sales_fig.update_yaxes(tickformat=',')
age60_sales_fig.update_yaxes(tickformat=',')
age70_sales_fig.update_yaxes(tickformat=',')
associate_sales_fig.update_yaxes(tickformat=',')
zon_sales_fig.update_yaxes(tickformat=',')
man_goods_fig.update_xaxes(range=[-1, 50])
women_goods_fig.update_xaxes(range=[-1, 50])
age_man_goods_fig.update_xaxes(range=[-1, 50])
age_women_goods_fig.update_xaxes(range=[-1, 50])
age20_sales_fig.update_xaxes(range=[-1, 50])
age30_sales_fig.update_xaxes(range=[-1, 50])
age40_sales_fig.update_xaxes(range=[-1, 50])
age50_sales_fig.update_xaxes(range=[-1, 50])
age60_sales_fig.update_xaxes(range=[-1, 50])
age70_sales_fig.update_xaxes(range=[-1, 50])
zon_goods_fig.update_xaxes(range=[-1, 50])
zon_sales_fig.update_xaxes(range=[-1, 50])
"###############################  PLOT  ##############################"
# flask app
@server.route('/')
def index():
    return '''<!DOCTYPE HTML><html>
  <head>
    <title>Demo</title>
    <script>
    
    </script>
  </head>
  <body style = "background-color: beige;">
    <h1 style="text-align:center; color: #7FDBFF; font-weight: bold; text-shadow: 6px 2px 2px gray;">제7회 롯데멤버스 빅데이터 경진대회</h1>
    <h2 style="text-align:center; color: #000000; font-weight: bold;">참가자 : 안동주</h2>
    <br>
    <br>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/goods/gender/" style="color: gray; font-size: 25px; font-weight: bold">성별에 따른 상품 구매 분류</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/goods/age/" style="color: gray; font-size: 25px; font-weight: bold">연령에 따른 상품 구매 분류</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/goods/local/" style="color: gray; font-size: 25px; font-weight: bold">거주지에 따른 상품 구매 분류</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/goods/onoff/" style="color: gray; font-size: 25px; font-weight: bold">온라인/오프라인에 따른 상품 구매 분류</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/associate/sales/" style="color: gray; font-size: 25px; font-weight: bold">제휴사별 매출</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/associate/uses/" style="color: gray; font-size: 25px; font-weight: bold">제휴사별 이용횟수</a>
    <div>
    <br>
    <div style="text-align:center;">
        <a href="http://localhost:5000/lpay/info/" style="color: gray; font-size: 25px; font-weight: bold">Lpay</a>
    <div>
    <br>
  </body>
</html>'''
goods_gender.layout = html.Div(children=[
    #성별
    html.Div([
        html.H1(children='성별 분석', style=main_style),
        html.H3(children='성비', style=sub_style),
        dcc.Graph(
            id='graph1',
            figure=man_women_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='시간별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph3',
                figure=man_hour_purchase_fig
            ),  
        ], className='goods_hour_purchase'),
        html.Div([
            html.H1(children='시간별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph4',
                figure=women_hour_purchase_fig
            ),  
        ], className='goods_hour_purchase'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='기간별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph5',
                figure=man_anuual_purchase_fig
            ),  
        ], className='goods_anuual_purchase'),
        html.Div([
            html.H1(children='기간별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph6',
                figure=women_anuual_purchase_fig
            ),  
        ], className='goods_anuual_purchase'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph7',
                figure=man_goods_fig
            ),  
        ], className='goods'),
        html.Div([
            html.H1(children='품목별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph8',
                figure=women_goods_fig
            ),  
        ], className='goods'),
    ]),
])

goods_age.layout = html.Div(children=[
html.Div([
        html.H1(children='연령대 분석', style=main_style),
        html.H3(children='성비', style=sub_style),
        dcc.Graph(
            id='graph9',
            figure=age_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='시간대별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph10',
                figure=age_man_hour_purchase_fig
            ),  
        ], className='age_hour_purchase'),
        html.Div([
            html.H1(children='시간대별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph11',
                figure=age_women_hour_purchase_fig
            ),  
        ], className='age_hour_purchase'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='기간별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph12',
                figure=age_man_purchase_fig
            ),  
        ], className='age_purchase'),
        html.Div([
            html.H1(children='기간별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph13',
                figure=age_women_purchase_fig
            ),  
        ], className='age_purchase')
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 구매수(남성)', style=sub_style),
            dcc.Graph(
                id='graph14',
                figure=age_man_goods_fig
            ),  
        ], className='age_goods'),
        html.Div([
            html.H1(children='품목별 상품 구매수(여성)', style=sub_style),
            dcc.Graph(
                id='graph15',
                figure=age_women_goods_fig
            ),  
        ], className='age_goods')
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 매출(20대)', style=sub_style),
            dcc.Graph(
                id='graph16',
                figure=age20_sales_fig
            ),  
        ], className='age_sales'),
        html.Div([
            html.H1(children='품목별 상품 매출(30대)', style=sub_style),
            dcc.Graph(
                id='graph17',
                figure=age30_sales_fig
            ),  
        ], className='age_sales')
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 매출(40대)', style=sub_style),
            dcc.Graph(
                id='graph18',
                figure=age40_sales_fig
            ),  
        ], className='age_sales'),
        html.Div([
            html.H1(children='품목별 상품 매출(50대)', style=sub_style),
            dcc.Graph(
                id='graph19',
                figure=age50_sales_fig
            ),  
        ], className='age_sales')
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 매출(60대)', style=sub_style),
            dcc.Graph(
                id='graph20',
                figure=age60_sales_fig
            ),  
        ], className='age_sales'),
        html.Div([
            html.H1(children='품목별 상품 매출(70대)', style=sub_style),
            dcc.Graph(
                id='graph21',
                figure=age70_sales_fig
            ),  
        ], className='age_sales')
    ]),
])

goods_local.layout = html.Div(children=[
    html.Div([
        html.H1(children='지역별 분석', style=main_style),
        html.H3(children='인구비율', style=sub_style),
        dcc.Graph(
            id='graph22',
            figure=zon_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='시간대별 상품 구매수', style=sub_style),
            dcc.Graph(
                id='graph23',
                figure=zon_hour_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='총 상품 구매수', style=sub_style),
            dcc.Graph(
                id='graph24',
                figure=zon_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 상품 구매수', style=sub_style),
            dcc.Graph(
                id='graph25',
                figure=zon_goods_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='품목별 매출 총액', style=sub_style),
            dcc.Graph(
                id='graph28',
                figure=zon_sales_fig
            ),  
        ], className='age_sales'),
    ])
])


associate_sales.layout = html.Div(children=[
    html.Div([
        html.H1(children='제휴사 분석', style=main_style),
        html.H3(children='제휴사별 이용비율', style=sub_style),
        dcc.Graph(
            id='graph26',
            figure=associate_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='제휴사별 매출', style=sub_style),
            dcc.Graph(
                id='graph27',
                figure=associate_sales_fig
            ),  
        ], className='age_sales'),
    ]),
])

associate_uses.layout = html.Div(children=[
    html.H1(children='월별 제휴사 이용횟수', style=main_style),

    html.Div([
        html.Label(['월 선택:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': '1월', 'value': 'graph1'},
                {'label': '2월', 'value': 'graph2'},
                {'label': '3월', 'value': 'graph3'},
                {'label': '4월', 'value': 'graph4'},
                {'label': '5월', 'value': 'graph5'},
                {'label': '6월', 'value': 'graph6'},
                {'label': '7월', 'value': 'graph7'},
                {'label': '8월', 'value': 'graph8'},
                {'label': '9월', 'value': 'graph9'},
                {'label': '10월', 'value': 'graph10'},
                {'label': '11월', 'value': 'graph11'},
                {'label': '12월', 'value': 'graph12'},
                    ],
            value='graph1',
            style={"width": "35%"}),
        
    html.Div(dcc.Graph(id='graph')),        
        ]),
])
@associate_uses.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def select_graph(value):
    if value == 'graph1':
        return associate_uses_fig1
    elif value == 'graph2':
        return associate_uses_fig2
    elif value == 'graph3':
        return associate_uses_fig3
    elif value == 'graph4':
        return associate_uses_fig4
    elif value == 'graph5':
        return associate_uses_fig5
    elif value == 'graph6':
        return associate_uses_fig6
    elif value == 'graph7':
        return associate_uses_fig7
    elif value == 'graph8':
        return associate_uses_fig8
    elif value == 'graph9':
        return associate_uses_fig9
    elif value == 'graph10':
        return associate_uses_fig10
    elif value == 'graph11':
        return associate_uses_fig11
    elif value == 'graph12':
        return associate_uses_fig12
    
lpay.layout = html.Div(children=[
    html.Div([
        html.H1(children='Lpay 분석', style=main_style),
        html.H3(children='Lpay사용 비율', style=sub_style),
        dcc.Graph(
            id='graph29',
            figure=lpay_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='온라인/오프라인 비율', style=sub_style),
            dcc.Graph(
                id='graph30',
                figure=lapy_onoff_ratio_fig
            ),  
        ], className='age_sales'),
    ]),
])

onoff.layout = html.Div(children=[
    html.Div([
        html.H1(children='온라인/오프라인 분석', style=main_style),
        html.H3(children='온라인/오프라인 구매 비율', style=sub_style),
        dcc.Graph(
            id='graph31',
            figure=goods_onoff_ratio_fig
        ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='온라인 구매', style=sub_style),
            dcc.Graph(
                id='graph32',
                figure=online_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='오프라인 구매', style=sub_style),
            dcc.Graph(
                id='graph33',
                figure=offline_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='시간별 온라인 구매', style=sub_style),
            dcc.Graph(
                id='graph34',
                figure=online_hours_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
    html.Div([
        html.Div([
            html.H1(children='시간별 오프라인 구매', style=sub_style),
            dcc.Graph(
                id='graph35',
                figure=offline_hours_purchase_fig
            ),  
        ], className='age_sales'),
    ]),
])

   
if __name__ == "__main__":
    server.debug = True
    server.run()