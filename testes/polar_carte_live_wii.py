# -*- coding: utf-8 -*-
import dash
import numpy as np
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from wiimote_py.setup_wiimote import setup_wiimote
from PnP_py.parametros_base_wii import parametros_base_wii
from PNP_wii_func import pts_wii
from PNP_wii_func import set_wii

f, d_ij, P_ref, cop = parametros_base_wii()
wm = setup_wiimote()

wii_set = set_wii(wm,f, d_ij, P_ref, cop )
Pts = pts_wii(wm,f, d_ij, P_ref, cop ,wii_set["fator_escala"],wii_set["origem"],wii_set["ang_origem"])

a = np.array(Pts["x"])
b = np.array(Pts["y"])

hip = np.array([0,5])
ang = np.array([0,Pts["alfa"]])

initial_trace = go.Scatterpolar(
                                r=hip,
                                theta=ang,
                                name='Scatter_polar',
                                mode='markers'
                                )

initial_trace_2 = go.Scatter(
                             x=a,
                             y=b,
                             name='Scatter',
                             mode='markers'
                            )

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph',
                  animate=True,
                  figure={'data': [initial_trace,initial_trace_2],
                          'layout': go.Layout(
                                              autosize=True,
                                              width=600,
                                              height=600,
                                              xaxis=dict(range=[-25, 25]),
                                              yaxis=dict(range=[-25, 25],
                                              scaleanchor = "x",
                                              scaleratio = 1,
                                              domain=[0,1]),
                                              polar=dict(radialaxis =dict(range=[0,25]))
                                             ),
                      
                         }),
        dcc.Interval(
                     id='graph-update',
                     interval=2*1000
                    ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
             [Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):
    
    Pts = pts_wii(wm,f, d_ij, P_ref, cop ,wii_set["fator_escala"],wii_set["origem"],wii_set["ang_origem"])
    
    a = np.array(Pts["x"])
    b = np.array(Pts["y"])
    
    hip = np.array([0,5])
    ang = np.array([0,Pts["alfa"]])

    trace = go.Scatterpolar(
                            r=hip,
                            theta=ang,
                            name='Scatter',
                            mode='markers',
                           )
    
    trace_2 = go.Scatter(
                         x=a,
                         y=b,
                         name='Scatter',
                         mode='markers',
                        )

    return {'data': [trace,trace_2 ],
            'layout': go.Layout(
                                autosize=True,
                                width=1000,
                                height=500,
                                margin=go.layout.Margin(l=100),
                                xaxis=dict(range=[-60, 60],
                                scaleanchor = "x",
                                scaleratio = 1,
                                domain=[0,1]),
                                yaxis=dict(range=[-25, 25],
                                scaleanchor = "y",
                                scaleratio = 1,
                                domain=[0,1]),
                                polar=dict(radialaxis =dict(range=[0,25]))
                               )
            }


if __name__ == '__main__':
    app.run_server(debug=False,port=8050,host='0.0.0.0')

