import dash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Read and prepare the data
df = pd.read_csv('formatted_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Group by date and sum sales for the line chart
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    # Header section
    html.Div([
        html.H1(
            'Pink Morsel Sales Analysis',
            style={
                'textAlign': 'center',
                'color': '#2c3e50',
                'marginBottom': '10px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),
        html.H2(
            'Impact of Price Increase on January 15, 2021',
            style={
                'textAlign': 'center',
                'color': '#7f8c8d',
                'marginBottom': '30px',
                'fontSize': '18px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),
        html.P(
            'This interactive dashboard visualizes the daily sales of Pink Morsels across all regions. '
            'The red vertical line marks the price increase date. Use the interactive features to explore the data.',
            style={
                'textAlign': 'center',
                'marginBottom': '20px',
                'fontSize': '16px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'lineHeight': '1.6'
            }
        )
    ], style={'padding': '20px', 'backgroundColor': '#f8f9fa'}),

    # Main content
    html.Div([
        dcc.Graph(
            id='sales-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=daily_sales['Date'],
                        y=daily_sales['Sales'],
                        mode='lines+markers',
                        name='Daily Sales',
                        line={'color': '#3498db', 'width': 3},
                        marker={'size': 6, 'color': '#3498db'},
                        hovertemplate='<b>Date:</b> %{x}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>'
                    )
                ],
                'layout': go.Layout(
                    title={
                        'text': 'Pink Morsel Daily Sales Trend',
                        'x': 0.5,
                        'xanchor': 'center',
                        'font': {'size': 20, 'color': '#2c3e50'}
                    },
                    xaxis={
                        'title': 'Date',
                        'type': 'date',
                        'showgrid': True,
                        'gridcolor': '#ecf0f1',
                        'tickformat': '%Y-%m-%d'
                    },
                    yaxis={
                        'title': 'Total Sales ($)',
                        'showgrid': True,
                        'gridcolor': '#ecf0f1',
                        'tickformat': '$,.0f'
                    },
                    showlegend=True,
                    hovermode='x unified',
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    shapes=[
                        # Vertical line for price increase
                        {
                            'type': 'line',
                            'x0': '2021-01-15',
                            'y0': 0,
                            'x1': '2021-01-15',
                            'y1': daily_sales['Sales'].max(),
                            'line': {
                                'color': '#e74c3c',
                                'width': 2,
                                'dash': 'dash'
                            }
                        }
                    ],
                    annotations=[
                        {
                            'x': '2021-01-15',
                            'y': daily_sales['Sales'].max() * 0.85,
                            'xref': 'x',
                            'yref': 'y',
                            'text': 'Price Increase<br>Jan 15, 2021',
                            'showarrow': True,
                            'arrowhead': 2,
                            'ax': 0,
                            'ay': -40,
                            'font': {'color': '#e74c3c', 'size': 12},
                            'bgcolor': 'rgba(255, 255, 255, 0.8)',
                            'bordercolor': '#e74c3c',
                            'borderwidth': 1
                        }
                    ],
                    margin={'l': 60, 'r': 60, 't': 80, 'b': 60}
                )
            },
            style={'height': '600px'}
        )
    ], style={'padding': '20px'}),

    # Footer
    html.Div([
        html.P(
            'Data source: Soul Foods transaction data | Analysis: Quantium Data Analytics',
            style={
                'textAlign': 'center',
                'color': '#95a5a6',
                'fontSize': '14px',
                'marginTop': '20px'
            }
        )
    ])
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#ffffff'})

# Define callback for interactivity (if needed in future)
# @app.callback(
#     Output('sales-line-chart', 'figure'),
#     Input('some-input', 'value')
# )
# def update_chart(value):
#     # Future enhancement: add filters or interactive features
#     pass

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)