from highcharts_gantt.chart import Chart
from highcharts_gantt.options.series.gantt import GanttSeries
import datetime


def get_highcharts_gantt(container):
    options_as_dict = {
        'title': {
            'text': 'Gantt Chart with Progress Indicators',
            'align': 'left'
        },

        'xAxis': {
            'min': datetime.date(2014, 10, 17),
            'max': datetime.date(2014, 10, 30)
        },

        'accessibility': {
            'point': {
                'descriptionFormatter': """function (point) {
                    var completedValue = point.completed ?
                            point.completed.amount || point.completed : null,
                        completed = completedValue ?
                            ' Task completed ' + Math.round(completedValue * 1000) / 10 + '%.' :
                            '';
                    return Highcharts.format(
                        '{point.yCategory}.{completed} Start {point.x:%Y-%m-%d}, end {point.x2:%Y-%m-%d}.',
                        { point, completed }
                    );
                }"""
            }
        },

        'lang': {
            'accessibility': {
                'axis': {
                    'xAxisDescriptionPlural': 'The chart has a two-part X axis showing time in both week numbers and days.'
                }
            }
        },

        'series': [{
            'type': 'gantt',
            'name': 'Project 1',
            'data': [{
                'name': 'Start prototype',
                'start': datetime.date(2014, 10, 18),
                'end': datetime.date(2014, 10, 25),
                'completed': 0.25
            }, {
                'name': 'Test prototype',
                'start': datetime.date(2014, 10, 27),
                'end': datetime.date(2014, 10, 29)
            }, {
                'name': 'Develop',
                'start': datetime.date(2014, 10, 20),
                'end': datetime.date(2014, 10, 25),
                'completed': {
                    'amount': 0.12,
                    'fill': '#fa0'
                }
            }, {
                'name': 'Run acceptance tests',
                'start': datetime.date(2014, 10, 23),
                'end': datetime.date(2014, 10, 26)
            }]
        }]
    }

    chart = Chart.from_options(
        options_as_dict,
        chart_kwargs={
            'container': container,
            'is_gantt_chart': True
        }
    )

    return chart