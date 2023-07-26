from flask import Flask
from IndicatorsData.routes.indicators import indicators
from RespData.routes.respData import respData
from config import config

app = Flask(__name__)


app.register_blueprint(indicators)
app.register_blueprint(respData)
app.config.from_object(config['development'])


if __name__ == "__main__":
    app.run(debug=True)