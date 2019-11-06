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

t = np.arange(0.0, 2*np.pi, 0.1)

x =  60*np.cos(t)
y =  10*np.sin(t)

x_max = 60
x_min = -60
y_max = 25
y_min = -25

px = np.array(Pts["x"])
py = np.array(Pts["y"])

xsec = x[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]
ysec = y[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]

gama = Pts["alfa"]*((2*np.pi)/(360))

xsec = xsec - px
ysec = ysec - py

R =  np.array([[np.cos(gama),-np.sin(gama)],[ np.sin(gama),np.cos(gama)]])

for i in range(np.size(xsec)):
    
    a = np.dot(R,np.array([[xsec[i]],[ysec[i]]]))
    
    xsec[i] = a[0][0]
    ysec[i] = a[1][0]
    
raio = 25

xr = xsec[(xsec >= (-raio)) & (xsec <= (raio)) & (ysec >= (-raio)) & (ysec <= (raio)) ]
yr = ysec[(xsec >= (-raio)) & (xsec <= (raio)) & (ysec >= (-raio)) & (ysec <= (raio)) ]

hip = np.sqrt(xr**2 + yr**2)
ang = np.arctan2(yr,xr)*(360/(2*np.pi))

initial_trace = go.Scatterpolar(
                                r=hip,
                                theta=ang,
                                name='Scatter_polar',
                                mode='lines+markers'
                                )

initial_trace_2 = go.Scatter(
                             x=xsec,
                             y=ysec,
                             name='Scatter',
                             mode='lines+markers'
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
    
    #print("x : ",Pts["x"]," y : ",Pts["y"]," z : ",Pts["z"]," alfa : ",Pts["alfa"])
    
    px = np.array(Pts["x"])
    py = np.array(Pts["y"])
    
    xsec = x[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]
    ysec = y[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]
    
    gama = Pts["alfa"]*((2*np.pi)/(360))
    
    xsec = xsec - px
    ysec = ysec - py
    
    R =  np.array([[np.cos(gama),-np.sin(gama)],[ np.sin(gama),np.cos(gama)]])
    
    for i in range(np.size(xsec)):
        
        a = np.dot(R,np.array([[xsec[i]],[ysec[i]]]))
        
        xsec[i] = a[0][0]
        ysec[i] = a[1][0]
        
    raio = 25
    
    xr = xsec[(xsec >= (-raio)) & (xsec <= (raio)) & (ysec >= (-raio)) & (ysec <= (raio)) ]
    yr = ysec[(xsec >= (-raio)) & (xsec <= (raio)) & (ysec >= (-raio)) & (ysec <= (raio)) ]
    
    hip = np.sqrt(xr**2 + yr**2)
    ang = np.arctan2(yr,xr)*(360/(2*np.pi))
    
    print("x : ",xsec," y : ",ysec," z : ",hip," alfa : ",ang)

    trace = go.Scatterpolar(
                            r=hip,
                            theta=ang,
                            name='Scatter',
                            mode='lines+markers',
                           )
    
    trace_2 = go.Scatter(
                         x=xsec,
                         y=ysec,
                         name='Scatter',
                         mode='lines+markers',
                        )

    return {'data': [trace,trace_2 ],
            'layout': go.Layout(
                                autosize=True,
                                width=1000,
                                height=500,
                                margin=go.layout.Margin(l=100),
                                xaxis=dict(range=[-60, 60],
                                showline=True,
                                zeroline=True,
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

