import plotly.graph.objects as go
import pandas as pd 

df = pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig = go.Figure(data=go.Choropleth(
    location=df['code'],
    z = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'darkmint',
    colorbar_title 'most to least visted states'
))

fig.update_layout(
    geo_scope='usa',
    title_text="Map of visited staets"
)

fig.show()