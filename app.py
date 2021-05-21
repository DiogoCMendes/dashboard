# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:48:11 2021

@author: Diogo
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.io as io

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Img(src=app.get_asset_url('IST_logo.png')),
    html.H2('Dashboard  for the forecast electricity consumption in the Civil Pavilion'),
    html.H3('Diogo Caneira Mendes,90541'),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Data Exploration', value='tab-1'),
        dcc.Tab(label='Clustering', value='tab-2'),
        dcc.Tab(label='Feature Selection', value='tab-3'),
        dcc.Tab(label='Regression', value='tab-4'),
        ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))

 ######################## Data Exploration ################################


def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Data Exploration'),
            html.H5('Distribution of the power for all the hours data along the years of 2017 and 2018'),
            html.Img(src=app.get_asset_url('data_vis.png')),
        ])
              
 ##################################CLUSTERING################################

    elif tab == 'tab-2':
        return html.Div([
            html.H3('Clustering'),
            dcc.RadioItems(
        id='radio_cluster',
        options=[
            {'label': 'Cluster', 'value': 1},
            {'label': 'Power along the month', 'value': 2},
            {'label': 'Power for different hours ', 'value': 3},
            {'label': 'Power for various temperatures', 'value': 4},
            {'label': 'Consumption Pattern', 'value': 5},
            ],
        value = 1
        ),
           html.Div(id='cluster_type'),
           ])
    

     
    ##########################FEATURE SELECTION################################
    
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Feature Selection'),
            html.H4('The feature selection started with the following parameters:'),
            html.H5('Variables available in the data:'),
            html.H6('Date Temp_C HR windSpeed_m/s windGust_m/s pres_mbar solarRad_W/m2 rain_mm/h rain_day Date_tot Power_kW'),
            html.H5('Variables chosen:'),
            html.H6('Temperature(Celsius) Solar Radiation(W/m^2) Power(kW) Hours Month Day'),
            html.H5('Indexes: 0 1 2 3 4 5'),
            html.Img(src=app.get_asset_url('feature selection.png')),
            ])
            

    
        ##########################REGRESSION################################
    
    
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Regression'),
            dcc.Dropdown(
                id='reg_dropdown',
                options=[
                    {'label':'Decision tree regression', 'value': 1},
                    {'label':'Gradient Boosting','value': 2},
                    {'label':'Neuro Network','value':3},
                    {'label':'Random Forest','value':4},
                    {'label':'Random Forest Uniformized','value':5},
                    {'label':'Support Vector Regression','value':6},
                    {'label':'Linear Regression','value':7},
            ],
        value = 1
        ),
        html.Div(id = 'reg_plot'),
        
        ])
    
    ##########################DROPDOWN CALLBACK###########################
@app.callback(Output('reg_plot', 'children'),
              Input('reg_dropdown', 'value'))

def render_figure_png(reg_dropdown):
    if reg_dropdown == 1:
        return html.Div([
                html.Img(src=app.get_asset_url('decision_tree_regressor.png')),
                html.Img(src=app.get_asset_url('decision_tree_regressor2.png')),
                html.H4('This model presents an error of: 0.57978411777558'),
            
            ])
    
    elif reg_dropdown == 2:
        return html.Div([
                html.Img(src=app.get_asset_url('gradient_boosting.png')),
                html.Img(src=app.get_asset_url('gradient_boosting_2.png')),
                html.H4('This model presents an error of:0.5370243828785416'),
            ])
    
    elif reg_dropdown == 3:
        return html.Div([
                html.Img(src=app.get_asset_url('neuro_network.png')),
                html.Img(src=app.get_asset_url('neuro_network_2.png')),
                html.H4('This model presents an error of: 0.5702711827473899'),
            ])
    
    elif reg_dropdown == 4:
        return html.Div([
                html.Img(src=app.get_asset_url('random_forest.png')),
                html.Img(src=app.get_asset_url('random_forest_2.png')),
                html.H4('This model presents an error of:0.46836150617089195'),
            ])
    
    elif reg_dropdown == 5:
        return html.Div([
                html.Img(src=app.get_asset_url('random_forest_uniformized.png')),
                html.Img(src=app.get_asset_url('random_forest_uniformized_2.png')),
                html.H4('This model presents an error of:0.4976308134643125'),
            ])
    
    elif reg_dropdown == 6:
        return html.Div([
                html.Img(src=app.get_asset_url('sup_vec_reg.png')),
                html.Img(src=app.get_asset_url('sup_vec_reg_2.png')),
                html.H4('This model presents an error of:0.5713999388862249'),
            ])
    
    elif reg_dropdown == 7:
        return html.Div([
                html.Img(src=app.get_asset_url('linear regression.png')),
                html.Img(src=app.get_asset_url('linear regression_2.png')),
                html.H3('This model presents an error of:0.6086430505048671'),
            ])
    
    ################################# RADIO CALLBACK ######################3

@app.callback(Output('cluster_type', 'children'), 
              Input('radio_cluster', 'value'))

def render_figure_html(radio_cluster):
    
     if radio_cluster == 1:
         return html.Div([html.Img(src=app.get_asset_url('cluster_kmeans.png')),])
     
     elif radio_cluster == 2:
        return html.Div([html.Img(src=app.get_asset_url('cluster_days.png')),])
    
     elif radio_cluster == 3:
         return html.Div([html.Img(src=app.get_asset_url('cluster_hour.png')),])
     
     elif radio_cluster == 4:
         return html.Div([html.Img(src=app.get_asset_url('cluster_temp.png')),])
     
     elif radio_cluster == 5:
         return html.Div([
                 html.Img(src=app.get_asset_url('consumption_pattern.png')),
                 html.Img(src=app.get_asset_url('Killowatt hour power pattern.png')),])
     

if __name__ == '__main__':
    app.run_server(debug=True)

