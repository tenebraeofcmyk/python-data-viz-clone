from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Prepare data
    data = pd.DataFrame({
        'State': ['Illinois', 'New York', 'Indiana', 'North Carolina', 'Ohio'],
        'Latitude': [40.0, 43.0, 40.0, 35.5, 40.5],
        'Longitude': [-89.0, -75.0, -86.0, -79.0, -82.5],
        'Sightings': [100, 200, 150, 120, 130]
    })

    # Create the Plotly figure
    fig = px.scatter_geo(data,
                         lat='Latitude',
                         lon='Longitude',
                         size='Sightings',
                         hover_name='State',
                         projection='albers usa',
                         title='Bird Sightings by State in the US')

    # Convert the figure to HTML
    graph_html = fig.to_html(full_html=False)
    
    return render_template('troy.html', plot_div=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
