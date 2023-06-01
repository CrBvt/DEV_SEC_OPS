from random import randint

from app_highcharts import app_highcharts
from flask import render_template
from app_highcharts.highcharts_example.basic_line import get_highcharts_basic_line

import pandas as pd


###################################


@app_highcharts.route('/')
def root():

    container = "chartContainer"

    hc_basic_line = get_highcharts_basic_line(container_id=container, variable_name="chart")

    js_literal = hc_basic_line.to_js_literal()

    return render_template("highcharts.html", highcharts_js=js_literal, div_id=container)
