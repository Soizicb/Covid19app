import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # read data
    df = pd.read_csv('data/owid-covid-data.csv')
    
    # first chart plots covid cases in Canada as a line chart
    
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = df[df['location'] == 'Canada']['date'],
      y = df[df['location'] == 'Canada']['total_cases_per_million'],
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'COVID-19 cases per million in Canada',
                xaxis = dict(title = 'date'),
                yaxis = dict(title = 'total cases per million'),
                )

# second chart plots new covid cases per million    
    graph_two = []

    graph_two.append(
      go.Bar(
      x = df[df['location'] == 'Canada']['date'],
      y = df[df['location'] == 'Canada']['new_cases_per_million'],
      )
    )

    layout_two = dict(title = 'New COVID-19 cases per million in Canada',
                xaxis = dict(title = 'date'),
                yaxis = dict(title = 'new cases per million'),
                )


# third chart plots number of death per cases in Canada
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = df[df['location'] == 'Canada']['total_cases'],
      y = df[df['location'] == 'Canada']['total_deaths'],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Number of death per total number of cases in Canada',
                xaxis = dict(title = 'total number of cases'),
                yaxis = dict(title = 'total number of deaths')
                       )
    
# fourth chart shows new deaths per million in Canada
    graph_four = []
    
    graph_four.append(
      go.Bar(
      x = df[df['location'] == 'Canada']['date'],
      y = df[df['location'] == 'Canada']['new_deaths_per_million'],
      )
    )

    layout_four = dict(title = 'new deaths per million in Canada',
                xaxis = dict(title = 'date'),
                yaxis = dict(title = 'new deaths per million'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures