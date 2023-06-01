from highcharts_core.chart import Chart
from highcharts_core.options import HighchartsOptions
from highcharts_core.options.plot_options import PlotOptions
from highcharts_core.options.axes.x_axis import XAxis
from highcharts_core.options.axes.y_axis import YAxis
from highcharts_core.options.axes.accessibility import AxisAccessibility
from highcharts_core.options.axes.title import AxisTitle
from highcharts_core.options.title import Title
from highcharts_core.options.subtitle import Subtitle
from highcharts_core.options.legend import Legend
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.options.series.area import LineSeries
from highcharts_core.options.series.labels import SeriesLabel
from highcharts_core.options.responsive import Responsive, ResponsiveRules, Condition
from highcharts_core.constants import EnforcedNull


def get_highcharts_basic_line(container_id=None, variable_name=None):

    chart_options = HighchartsOptions(
        title=Title(
            text='U.S Solar Employment Growth by Job Category, 2010-2020',
            align='left'
        ),
        subtitle=Subtitle(
            text='Source: <a href="https://irecusa.org/programs/solar-jobs-census/" target="_blank">IREC</a>',
            align='left'),

        y_axis=YAxis(title=AxisTitle(text='Number of Employees')),

        x_axis=XAxis(
            accessibility=AxisAccessibility(range_description='Range: 2010 to 2020')
        ),

        legend=Legend(
            layout='vertical',
            align='right',
            vertical_align='middle'
        ),

        plot_options=PlotOptions(
            series=SeriesOptions(
                point_start=2010,
                label=SeriesLabel(connector_allowed=False)
            )
        )
    )

    override_options = HighchartsOptions(
        legend=Legend(
            layout='horizontal',
            align='center',
            vertical_align='bottom')
    )

    responsive_config = Responsive(
        rules=[
            ResponsiveRules(
                chart_options=override_options,
                condition=Condition(max_width=500)
            )
        ]
    )

    chart_options.responsive = responsive_config

    series1 = LineSeries(
        name='Installation & Developers',
        data=[43934, 48656, 65165, 81827, 112143, 142383, 171533, 165174, 155157, 161454, 154610]
    )

    series2 = LineSeries(
        name='Manufacturing',
        data=[24916, 37941, 29742, 29851, 32490, 30282, 38121, 36885, 33726, 34243, 31050]
    )

    series3 = LineSeries(
        name='Sales & Distribution',
        data=[11744, 30000, 16005, 19771, 20185, 24377, 32147, 30912, 29243, 29213, 25663]
    )

    series4 = LineSeries(
        name='Operations & Maintenance',
        data=[
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            EnforcedNull,
            11164,
            11218,
            10077]
    )

    series5 = LineSeries(
        name='Other',
        data=[21908, 5548, 8105, 11248, 8989, 11816, 18274, 17300, 13053, 11906, 10073]
    )

    chart_options.add_series(series1, series2, series3, series4, series5)

    chart = Chart.from_options(
        chart_options,
        chart_kwargs={
            'container': container_id,
            'variable_name': variable_name
        }
    )

    return chart
