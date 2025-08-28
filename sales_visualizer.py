import pandas
from dash import Dash, html, dcc
from plotly.express import line

# Read and prepare the data
df = pandas.read_csv('formatted_sales_data.csv')
df['Date'] = pandas.to_datetime(df['Date'])
df = df.sort_values('Date')

# Group by date and sum sales for the line chart
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1('Pink Morsel Sales Analysis'),
    html.H2('Impact of Price Increase on January 15, 2021'),
    html.P('This dashboard shows daily sales of Pink Morsels across all regions.'),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=line(
            daily_sales,
            x='Date',
            y='Sales',
            title='Pink Morsel Daily Sales Trend'
        )
    ),
    
    html.P('Note: Pink Morsel price increased on January 15, 2021')
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)