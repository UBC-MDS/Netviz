from pickletools import int4
from dash import Dash, html, dcc, Input, Output, dash_table
import altair as alt
import pandas as pd
from vega_datasets import data
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

# Set up app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "NetViz"
server = app.server

# Read in global data
df = pd.read_csv("data/processed/netflix_movies_genres.csv")

def plot_rating(genre):
    # Add the missing rating to keep every genre have all rating types
    all_ratings = df['rating'].unique().tolist()
    group_df = df[df.genre == genre].groupby(by=['rating']).count()['show_id'].reset_index()
    group_df = group_df.rename(columns={'show_id': 'count'})
    sub_ratings = group_df['rating'].tolist()
    for rating in all_ratings:
        if rating not in sub_ratings:
            group_df = pd.concat([group_df, pd.DataFrame.from_dict({'rating': [rating], 'count': [0]})])
    # Plot the chart
    chart = alt.Chart(group_df, title=f"Maturity rating distribution of {genre}").mark_bar().encode(
              y=alt.Y('rating', title="Rating", sort='x'),
              x=alt.X('count', title="Number of movies", axis=alt.Axis(format='.0f')),
              tooltip='count'
              ).interactive()
    return chart.to_html()

def plot_time(genre):
    group_df = df[df.genre == genre].groupby(by=['release_year']).count()['show_id'].reset_index()
    group_df = group_df.rename(columns={'show_id': 'count'})
    chart = alt.Chart(group_df, title=f"Release year plot of {genre}").mark_line(
        point={"filled": False,"fill": "white"}
        ).encode(
            y=alt.Y('count', title="Number of movies", 
                axis=alt.Axis(values=list(range(0, 300, 5)), format='.0f'),
                scale=alt.Scale(domain=(0, 100))),
            x=alt.X('release_year', title="Year", axis=alt.Axis(format='.0f'),
                scale=alt.Scale(domain=(1940, 2022))),
            tooltip=['count', 'release_year']
        ).interactive()
    return chart.to_html()

def plot_country(genre):
    # explode on the country column
    country_df = df[df.genre == genre]
    # silence the warning for chained assigment
    pd.options.mode.chained_assignment = None
    country_df['country'] = country_df['country'].apply(lambda x: x.split(', '))
    country_df = country_df.explode('country')
    # find the id based on the country name
    
    
    country_id = pd.read_csv("data/processed/country_ids.csv")
    
        
    country_df = country_df.groupby(by=['country']).count().show_id.reset_index().rename(columns={'show_id':'count', 'country':'name'})
    country_df = country_df.merge(country_id, on='name')
    # plot the world map
    source = alt.topo_feature(data.world_110m.url, "countries")

    background = alt.Chart(source).mark_geoshape(fill="lightgray")

    foreground = (
        alt.Chart(source, title=f"Total number of {genre} type Netflix movies by country")
        .mark_geoshape(stroke="black", strokeWidth=0.15)
        .encode(
            color=alt.Color(
                "count:Q", scale=alt.Scale(scheme='orangered'),
            ),
            tooltip=[
                alt.Tooltip("name:N", title="Country"),
                alt.Tooltip("count:Q", title="Count"),
            ],
        )
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(country_df, "id", ["name", "count"]),
        )
    )

    final_map = (
        (background + foreground)
        .configure_view(strokeWidth=0)
        .properties(width=1100, height=400)
        .project("equalEarth")
    )
    return final_map.to_html()

# layout/frontend

app.layout = dbc.Container([
    html.H1(children='NetViz - Netflix Movies Visualization Dashboard', 
            style={'font-size': "360%", 'color':'#bd1818'}),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div(children=[
                html.Label(['Genre of the movie:'],
                style={'font-weight': 'bold', "text-align": "center", 'font-size': "120%", 'color':'#5a9c39'}),
                dcc.Dropdown(
                    id='genre', 
                    value='Comedies',  # REQUIRED to show the plot on the first page load
                    clearable=False,
                    options=[{'label': i, 'value': i} for i in df['genre'].unique()]
                )
            ])
        ], md=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(html.H5('Maturity Rating', 
                            style = {'text-align': 'center', 'font-size': "120%", 'color': '#E50914'})
                        ),
                        color='#221F1F'
                    ),
                    html.Iframe(
                        id='rating',
                        style={'border-width': '0', 'width': '700px', 'height': '500px'},
                        srcDoc=plot_rating(genre='Comedies')
                    )
                ], md=6),
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(html.H5('Netflix Movies over Time', 
                            style = {'text-align': 'center', 'font-size': "120%", 'color': '#E50914'})
                        ),
                        color='#221F1F'
                    ),
                    html.Iframe(
                        id='time',
                        style={'border-width': '0', 'width': '700px', 'height': '500px'},
                        srcDoc=plot_time(genre='Comedies')
                    )
                ], md=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(html.H5('World Map of Netflix Movies', 
                            style = {'text-align': 'center', 'font-size': "120%", 'color': '#E50914'})
                        ),
                        color='#221F1F'
                    ),
                    html.Iframe(
                        id='country',
                        style={'border-width': '0', 'width': '1400px', 'height': '500px'},
                        srcDoc=plot_country(genre='Comedies')
                    )
                ])]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(html.H5('Table of Netflix Movies', 
                            style = {'text-align': 'center', 'font-size': "120%", 'color': '#E50914'})
                        ),
                        color='#221F1F'
                    ),
                    dash_table.DataTable(
                        style_cell={
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 0,
                        },
                        tooltip_duration=None,
                        id='table', page_size=10
                    ),
                ])
            ])
            
        ])
    ])
])


# Set up callbacks/backend
@app.callback(
    [Output('rating', 'srcDoc'),
    Output('time', 'srcDoc'),
    Output('country', 'srcDoc'),
    Output('table', 'data'),
    Output('table', 'columns'),
    Output('table', 'tooltip_data')],
    Input('genre', 'value'))

def multi_output(genre):
    selected_df = df[df.genre == genre].sort_values(by=['release_year'], ascending=False)
    selected_df.rename(columns={'title': 'Title', 'description': 'Description',
                                'director': 'Director', 'release_year': 'Release Year', 
                                'duration': 'Duration(min)'}, inplace=True)
    cols = ["Title", "Description", "Director", "Release Year", "Duration(min)"]
    columns = [{"name": col, "id": col} for col in cols]
    data = selected_df[cols].to_dict('records')
    tooltip_data = [{
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                    } for row in selected_df.to_dict('records')
    ]
    return plot_rating(genre), plot_time(genre), plot_country(genre), data, columns, tooltip_data

if __name__ == '__main__':
    app.run_server(debug=True)
    
