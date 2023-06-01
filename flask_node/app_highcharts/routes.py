from random import randint

from app_highcharts import app_highcharts
from flask import render_template
from app_highcharts.highcharts_example import \
    get_highcharts_dynamic, \
    get_highcharts_basic_line, \
    get_highcharts_basic_area, \
    get_highcharts_pie_drill_down


switch_chart_type = {
        'Basic Line': get_highcharts_basic_line,
        'Basic Area': get_highcharts_basic_area,
        'Dynamic Chart': get_highcharts_dynamic,
        'Pie Chart': get_highcharts_pie_drill_down
    }

@app_highcharts.route('/charts/<chart_type>')
def charts(chart_type=None):

    container = "chartContainer"
    js_literal = ""

    if chart_type is not None:
        hc = switch_chart_type.get(chart_type, lambda x: "")(container)
        js_literal = hc.to_js_literal()

    return render_template(
        "highcharts.html",
        highcharts_js=js_literal,
        div_id=container,
        nav_bar_items=list(switch_chart_type.keys())
    )

@app_highcharts.route('/')
@app_highcharts.route('/home')
def home():
    return render_template(
        'welcome.html',
        nav_bar_items=list(switch_chart_type.keys())
    )