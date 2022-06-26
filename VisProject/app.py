import pandas as pd
import dash
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from dash import dcc
import base64


'''
Definitions:
'''
dict_labels = {"pts": "Points", "reb": "Rebounds", "gp": "Game Played",
               "ast": "Assists", "net_rating": "Net Rating"}

dict_labels2 = {"pts": "Points", "reb": "Rebounds", "gp": "Game Played",
                "ast": "Assists", "net_rating": "Net Rating","oreb_pct":"Offensive Rebound (%)",
                "dreb_pct":"Defensive Rebound (%)", "usg_pct": "Usage (%)",
                "ts_pct":"Shooting Efficiency (%)", "ast_pct":"Field Goals Assisted (%)",
                "mean_score":"Mean Score", "median_score":"Median Score",
                "player_height":"Player Height","player_weight":"Player Weight"}

BackgroundColor = "#fffaf6"

df = pd.read_csv('data/df.csv')
df = df.drop('Unnamed: 0', axis=1)

image_filename = 'assets/NBAdraftlogo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename2 = 'assets/basketball.png'
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

image_filename3 = 'assets/logos.png'
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())


'''
Build App:
'''
app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([

    # Header Div:
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),
                 style={'height':'6%', 'width':'6%', 'display': 'inline-block', 'margin-right': '30px'}),
        html.H1(' NBA DRAFT STATS ',
                style={'display': 'inline-block',
                       'font-family': 'Oswald',
                       'font-size': '8rem',
                       "color": "#1d428a", 'margin': '1rem'
                       },
                ),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),
                 style={'height': '6%', 'width': '6%', 'display': 'inline-block', 'margin-left': '30px'}),
    ], style={'textAlign': 'center'},
    ),

    # Image Div:
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),
                 style={'height': '25%', 'width': '25%', 'display': 'inline-block'}),

        html.Br(),html.Br(),

        html.H1('What is the NBA Draft?',
                style={'font-family': 'Oswald', 'font-size': '60px', 'width':'80%','color': "#1d428a",
                       'margin': 0, 'textAlign': 'center', 'display': 'inline-block'},
                ),
        html.H1('The NBA draft is an annual event dating back to 1947 in which the teams from NBA can draft players who\
         are eligible and wish to join the league. These are typically college basketball players, but international\
          players are also eligible to be drafted.',
                style={'font-family': 'Oswald', 'font-size': '30px', 'width':'50%','color': "#c8102e",
                       'textAlign': 'left', 'display': 'inline-block'},
                ),

        html.Br(),html.Br(),html.Br(),

        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                 style={'height': '25%', 'width': '25%', 'border-radius': '90px', 'display': 'inline-block'}),

        html.Br(), html.Br(),

        html.H1('What is the NBA Draft Lottery?',
                style={'font-family': 'Oswald', 'font-size': '60px', 'width': '80%', 'color': "#1d428a",
                       'margin': 0, 'textAlign': 'center', 'display': 'inline-block'},
                ),
        html.H1('The NBA Draft Lottery is an annual event held by the NBA, where the teams who did not make the \
         playoffs in the past year participate in a state-lottery style process in order to determine the first three \
         picks of the draft, until 2018. The team with the worst record receives the best odds of receiving the \
                first pick.',
                style={'font-family': 'Oswald', 'font-size': '30px', 'width': '50%', 'color': "#c8102e",
                       'textAlign': 'left', 'display': 'inline-block'},
                ),
    ], style={'textAlign': 'center'}),

    html.Br(),html.Br(),
    html.Hr(style={'width': '65%', 'borderColor':'#1d428a'}),
    html.Br(),

    # Slider Div:
    html.Div([
        html.H1('~ STATS DASHBOARD ~',
                style={'display': 'inline-block',
                       'font-family': 'Oswald',
                       'font-size': '90px',
                       "color": "#1d428a", 'margin': '0.5rem'
                       },
                ),
        html.H4('Select number of draft picks to show:',
                style={'font-family': 'Oswald', 'font-size': '22px'}),
        html.P(
            dcc.Slider(1, 60, 1,
            id="my-slider",
            value=20,
            marks={
                    str(num): {}
                    for num in range(0, 60, 10)
                },
            tooltip={"always_visible": True}
            ),
            style={"width": "25%", 'display': 'inline-block', 'height': 10}),
    ], style={'textAlign': 'center'},
    ),

    html.Br(),

    # Left-side Div:
    html.Div([
        html.Div([
        html.H4("Bar Plot",
                style={'font-family': 'Oswald', 'font-size': '45px', 'color': '#1d428a', 'margin': 0},
                ),
        html.H1('Comparing between picks over one of the metrics',
                style={'font-family': 'Oswald', 'font-size': '25px', 'width': '85%', 'color': "#c8102e",
                       'textAlign': 'center', 'display': 'inline-block', 'margin': 0}),
                ],),
        html.H4("Select metric:",
                style={'font-family': 'Oswald', 'font-size': '22px',
                       'display': 'inline-block', 'margin-right': '10px'},
                ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {
                    "label": "Points",
                    "value": "pts",
                }, {
                    "label": "Assists",
                    "value": "ast",
                }, {
                    "label": "Rebounds",
                    "value": "reb",
                }, {
                    "label": "Game Played",
                    "value": "gp",
                },
            ],
            value="pts",
            clearable=False,
            style={'border-color': "#1d428a", 'font-size': 18, 'margin-right': '2.5rem', 'color': '#1d428a',
                   'width': '8rem', 'display': 'inline-block', 'verticalAlign': 'middle'}
        ),
        html.H4("Sort by metric value:",
                style={'font-family': 'Oswald', 'font-size': '22px', 'margin-right': '10px',
                       'display': 'inline-block'},
                ),
        dcc.RadioItems([
            'Sorted', 'Unsorted'], 'Sorted', id="radio",
            style={'display': 'inline-block', 'font-family': 'sans-serif','font-size': 18}),
        dcc.Graph(id="graph"),
    ], style={'width': '48%', 'float': 'left', 'display': 'inline-block',
              'margin-right': '1%', 'margin-left': '1%', 'textAlign': 'center'}),

    # Right-side Div:
    html.Div([
        html.H4("Scatter Plot",
                style={'font-family': 'Oswald', 'font-size': '45px', 'color': '#1d428a', 'textAlign': 'center', 'margin': 0},
                ),
        html.Div([
            html.H1('Comparing between the different metrics',
                    style={'font-family': 'Oswald', 'font-size': '25px', 'width': '85%', 'color': "#c8102e",
                            'textAlign': 'center', 'display': 'inline-block', 'margin': 0})
            ,],),
        html.H4("Select x-axis metric:",
                style={'font-family': 'Oswald', 'font-size': '22px',
                       'display': 'inline-block', 'margin-right': '10px'},
                ),
        dcc.Dropdown(
            id="dropdown2",
            options=[
                {
                    "label": "Points",
                    "value": "pts",
                }, {
                    "label": "Assists",
                    "value": "ast",
                }, {
                    "label": "Rebounds",
                    "value": "reb",
                }, {
                    "label": "Net Rating",
                    "value": "net_rating",
                }, {
                    "label": "Game Played",
                    "value": "gp",
                },
            ],
            value="pts",
            clearable=False,
            style={'margin-right': '1rem', 'border-color': "#1d428a", 'font-size': 18, 'margin-right': '2.5rem',
                   'width': '8rem', 'display': 'inline-block', 'verticalAlign': 'middle', 'color': '#1d428a'},
        ),
        html.H3("Select y-axis metric:",
                style={'font-family': 'Oswald', 'font-size': '22px',
                       'display': 'inline-block', 'margin-right': '10px'},
                ),
        dcc.Dropdown(
            id="dropdown3",
            options=[
                {
                    "label": "Points",
                    "value": "pts",
                }, {
                    "label": "Assists",
                    "value": "ast",
                }, {
                    "label": "Rebounds",
                    "value": "reb",
                }, {
                    "label": "Net Rating",
                    "value": "net_rating",
                }, {
                    "label": "Game Played",
                    "value": "gp",
                },
            ],
            value="ast",
            clearable=False,
            style={'margin': '0px', 'border-color': "#1d428a", 'font-size': 18 , 'color': '#1d428a',
                   'width': '8rem', 'display': 'inline-block', 'verticalAlign': 'middle'},
        ),
        dcc.Graph(id="graph2"),
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block',
              'margin-right': '1%', 'margin-left': '1%', 'textAlign': 'center'}),

    # Line Chart:
    html.Div([
        html.H4("Line Plot",
                style={'font-family': "Oswald", 'font-size': '45px', 'color': '#1d428a', 'margin': 0},
                ),
        html.Div([
            html.H1('Comparing between picks over normal/percentage metrics',
                    style={'font-family': 'Oswald', 'font-size': '25px', 'width': '85%', 'color': "#c8102e",
                            'textAlign': 'center', 'display': 'inline-block'})
            ,],),
        html.H3("Select scala:",
                style={'font-family': 'Oswald', 'font-size': '22px',
                       'display': 'inline-block', 'margin-right': '10px', 'margin-left': '20rem'},
                ),
        dcc.RadioItems([
            'Normal', 'Percentage'], 'Normal', id="radio2",
            style={'display': 'inline-block', 'font-family': 'sans-serif','font-size': 18, 'margin-right': '20rem'}),
        dcc.Graph(id="graph3", style={'width': '70%', 'display': 'inline-block'}),
    ], style={'textAlign': 'center', 'backgroundColor': BackgroundColor, 'display': 'inline-block'},
        ),

    # Circle plot:
    # html.Div([
    #     html.H4("Scatter Polar:",
    #             style={'font-family': 'Oswald', 'font-size': '45px', 'color': '#1d428a'},
    #             ),
    #
    #     dcc.Graph(id="graph4"),
    # ], style={'width': '30%', 'display': 'inline-block',
    #           'margin': '1.5rem',},
    #     ),

    html.Br(),

    html.Div([
        html.P('Ⓒ Peleg Gitnik & Etay Lorberboym', style={'font-size': '20px', 'backgroundColor': '#c8102e',
                                                          'width': '18%',  'display': 'inline-block',
                                                          'color': BackgroundColor, 'font-family': 'Oswald'},),
            ], style={'textAlign': 'center'}),
    ], style={ 'top': '0%', 'left': '0%', 'margin': '0',
          'max-width': '100%', 'width': '100%'}, )



'''
Callbacks Section:
'''
# Bar Chart:
@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"),
    Input("my-slider", "value"),
    Input("radio", "value"))
def update_bar_chart(metric, num, sort):
    if sort == 'Unsorted':
        data_use = df.sort_values(by=['draft_number'], ascending=True)
    elif sort == 'Sorted':
        data_use = df.sort_values(by=[metric], ascending=False)
    fig = px.bar(data_use[:num], x="draft_number", y=metric,
                 labels={
                     'draft_number': 'Pick Number', metric: dict_labels[metric]
                     })
    fig.update_xaxes(type='category')
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), paper_bgcolor=BackgroundColor,
                      plot_bgcolor=BackgroundColor, height=500)
    fig.update_traces(marker_color="#b60823", marker_line_color="#45030b",
                      marker_line_width=2, opacity=0.7)
    fig.update_xaxes(title_font=dict(size=25, family='sans-serif'))
    fig.update_yaxes(title_font=dict(size=25, family='sans-serif'))
    return fig


# Scatter plot:
@app.callback(
    Output("graph2", "figure"),
    Input("dropdown2", "value"),
    Input("dropdown3", "value"),
    Input("my-slider", "value"))
def update_scatter_plt(metric1, metric2, num):
    data_use = df.sort_values(by=[metric1, metric2], ascending=False)
    data_use['dummy_for_size'] = 1
    fig = px.scatter(data_use[:num], x=metric1, y=metric2, size='dummy_for_size',
                     text="draft_number", trendline="ols", hover_data={'dummy_for_size': False},
                     labels={'draft_number': 'Pick Number', metric1: dict_labels[metric1], metric2: dict_labels[metric2]})
    fig.update_traces(marker=dict(size=60, line=dict(width=2)), selector=dict(mode='markers'),
                      )
    fig.update_traces(marker_color="#2f69ce", marker_line_color="#0e3272",
                      marker_line_width=2)
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), paper_bgcolor=BackgroundColor,
                      plot_bgcolor=BackgroundColor, height=500)
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    fig.update_xaxes(title_font=dict(size=25, family='sans-serif'))
    fig.update_yaxes(title_font=dict(size=25, family='sans-serif'))
    return fig


# Line plot:
@app.callback(
    Output("graph3", "figure"),
    Input("my-slider", "value"),
    Input("radio2", "value"))
def line_plt(num, scala):
    data_use = df.sort_values(by=['draft_number'])
    norm_cols = ['draft_number', 'pts', 'gp', 'reb', 'ast', 'net_rating',
                 'mean_score', 'median_score']
    perc_cols = ['draft_number', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']
    if scala == "Normal":
        cols = norm_cols
    elif scala == "Percentage":
        cols = perc_cols
    fig = px.line(data_use[:num][cols], x='draft_number', y=cols, labels={'draft_number': 'Pick Number', 'value': 'Value'},
                  )
    fig.update_layout(template="plotly_white", xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    fig.update_layout(paper_bgcolor=BackgroundColor, plot_bgcolor=BackgroundColor, height=500, legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title_font_family="sans-serif",
        font=dict(family="sans-serif", size=18), bordercolor="#1d428a", borderwidth=2), legend_title_text="Metric:")
    fig.update_xaxes(type='category')
    fig.update_xaxes(title_font=dict(size=25, family='sans-serif'))
    fig.update_yaxes(title_font=dict(size=25, family='sans-serif'))
    fig.for_each_trace(lambda t: t.update(name=dict_labels2[t.name],
                                          legendgroup=dict_labels2[t.name],
                                          hovertemplate=t.hovertemplate.replace(t.name, dict_labels2[t.name])
                                          ))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
