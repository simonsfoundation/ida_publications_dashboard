
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc



# Create a template DASH app instance with a barplot 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create a barplot
fig = px.bar(x=[1, 2, 3], y=[1, 3, 2])

# Create a DASH layout with a barplot
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# Path: Procfile
web: gunicorn app:server

# Path: requirements.txt
dash
dash-bootstrap-components
plotly
gunicorn