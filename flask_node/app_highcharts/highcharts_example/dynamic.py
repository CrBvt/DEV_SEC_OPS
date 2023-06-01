from highcharts_core.chart import Chart
from highcharts_core.options import HighchartsOptions


def get_highcharts_dynamic(container):

    as_dict = {
        'chart': {
            'type': 'scatter',
            'margin': [70, 50, 60, 80],
            'events': {
                'click': """function (e) {
                    // find the clicked values and the series
                    var x = Math.round(e.xAxis[0].value),
                        y = Math.round(e.yAxis[0].value),
                        series = this.series[0];

                    // Add it
                    series.addPoint([x, y]);
                }"""
            }
        },
        'title': {
            'text': 'User supplied data',
            'align': 'left'
        },
        'subtitle': {
            'text': 'Click the plot area to add a point. Click a point to remove it.',
            'align': 'left'
        },
        'accessibility': {
            'announceNewData': {
                'enabled': True
            }
        },
        'xAxis': {
            'gridLineWidth': 1,
            'minPadding': 0.2,
            'maxPadding': 0.2,
            'maxZoom': 60
        },
        'yAxis': {
            'title': {
                'text': 'Value'
            },
            'minPadding': 0.2,
            'maxPadding': 0.2,
            'maxZoom': 60,
            'plotLines': [{
                'value': 0,
                'width': 1,
                'color': '#808080'
            }]
        },
        'legend': {
            'enabled': False
        },
        'exporting': {
            'enabled': False
        },
        'plotOptions': {
            'series': {
                'lineWidth': 1,
                'point': {
                    'events': {
                        'click': """function () {
                            if (this.series.data.length > 1) {
                                this.remove();
                            }
                        }"""
                    }
                }
            }
        },
        'series': [{
            'data': [[20, 20], [80, 80]]
        }]
    }

    chart = Chart.from_options(
        as_dict,
        chart_kwargs={
            'container': container,
        }
    )

    return chart