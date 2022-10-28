import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

import json


app = dash.Dash(__name__)

dfv = pd.read_csv('.data/USvideos.csv')
with open(".data/US_category_id.json") as data_file:    
    data = json.load(data_file)  

dfCategory = pd.json_normalize(data, 'items', record_prefix='category_')
dfCategory.rename(columns={'category_snippet.title': 'category_title', 
                           'category_snippet.channelId':'category_channelId',
                           'category_snippet.assignable':'category_assignable'}, 
                inplace=True)

dfCategory["category_id"]=dfCategory["category_id"].astype(int)

dfVideoCat = pd.merge(dfv, dfCategory,on="category_id")

dfVideoCat = dfVideoCat[["title","channel_title","category_title","views","likes","dislikes","comment_count","description"]]


app.layout = html.Div(children=[
    html.Img(
        src='assets\\yt-analytics-1.png',
        style={'width': '720px', 'height':'200px', 'border': '1px solid red'},
        alt='image'),
    html.H1(children='Caso de estudio YouTube', style={'color': 'blue'}),
    dcc.Graph(id="grafico",style={'width':'700px'}),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label':i, 'value':i} for i in dfVideoCat['category_title'].unique()],
        value= 'People & Blogs',
        style={'width':'700px'}
        ),
])


@app.callback(
    Output('grafico', 'figure'),
    Input('dropdown', 'value')
)
def update_figure(selected):

    filtered_df = dfVideoCat[dfVideoCat.category_title == selected]
    
    fig= px.scatter(filtered_df, y="dislikes", x="likes",color="likes",trendline="ols",log_x=True,log_y=True)
    
    fig.update_layout(transition_duration=500)
    
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)