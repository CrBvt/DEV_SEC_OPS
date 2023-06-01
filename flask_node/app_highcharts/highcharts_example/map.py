from highcharts_maps import constants
from highcharts_maps.chart import Chart
from highcharts_maps.options.series.heatmap import HeatmapSeries
import pandas
import datetime

def get_highchart_map(container):
    options_kwargs = {
        'chart': {
            'type': 'heatmap',
            'inverted': True
        },

        'accessibility': {
            'description': 'We see how temperatures are warmer during the day, especially from around 9am to 9pm. May 8th through 11th are also overall colder days compared to the rest. Overall the temperatures range from around -1 degrees C to around 23 degrees C.'
        },

        'title': {
            'text': 'Highcharts Heat Map',
            'align': 'left'
        },

        'subtitle': {
            'text': 'Temperature variation by day and hour through May 2017',
            'align': 'left'
        },

        'xAxis': {
            'tickPixelInterval': 50,
            'min': datetime.date(2017, 5, 1),
            'max': datetime.date(2017, 5, 31),
            'labels': {
                'enabled': True,
                'format': '{value:%Y-%m-%d}'
            }
        },

        'yAxis': {
            'accessibility': {
                'description': 'Hours in the day'
            },
            'title': {
                'text': constants.EnforcedNull
            },
            'labels': {
                'format': '{value}:00'
            },
            'minPadding': 0,
            'maxPadding': 0,
            'startOnTick': False,
            'endOnTick': False,
            'tickPositions': [0, 6, 12, 18, 24],
            'tickWidth': 1,
            'min': 0,
            'max': 23
        },

        'colorAxis': {
            'stops': [
                [0, '#3060cf'],
                [0.5, '#fffbbc'],
                [0.9, '#c4463a']
            ],
            'min': -5
        }
    }

    df = pandas.read_csv('app_highcharts/static/temperatures.csv')

    series = HeatmapSeries.from_pandas(df,
                                       property_map={'x': 'Date', 'y': 'Time', 'value': 'Temperature'},
                                       series_kwargs={
                                           'name': 'Temperature',
                                           'borderWidth': 0,
                                           'colsize': 24 * 36e5,
                                           'tooltip': {
                                               'headerFormat': 'Temperature<br/>',
                                               'pointFormat': '{point.x:%e %b, %Y} {point.y}:00: <b>{point.value} ℃</b>'
                                           },
                                           'accessibility': {
                                               'enabled': False
                                           },

                                       })

    chart = Chart.from_options(
        options_kwargs,
        chart_kwargs={
            'container': container,
        }
    )

    # chart = Chart(options=options_kwargs)

    chart.is_maps_chart = True
    chart.add_series(series)

    return chart
