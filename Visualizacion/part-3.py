import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('C:\\Users\\jeramirez\\Documents\\DataTranslator\\Visualizacion\\datasets\\auto-mpg.csv')

app = dash.Dash(__name__)

fig = px.scatter(df, x="displ", y="weight",
                    log_x=True, size_max=55, trendline="ols")

app.layout = html.Div(children=[
    html.H1("Desplazamiento vs Peso"),
    html.Img(
        src='https://c4.wallpaperflare.com/wallpaper/193/556/883/car-neon-chevrolet-corvette-race-cars-hd-wallpaper-preview.jpg',
        style = {'width': '80%'}),
    dcc.Graph(
        figure=fig
    )
])
    

if __name__ == '__main__':
    app.run_server(debug=True)