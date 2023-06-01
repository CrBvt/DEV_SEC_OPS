from flask import Flask
from config import Config

app_highcharts = Flask(__name__)
app_highcharts.config.from_object(Config)

from app_highcharts import routes
