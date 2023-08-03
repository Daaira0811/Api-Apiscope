from flask import Flask
from IndicatorsData.routes.indicators import indicators
from RespData.routes.respData import respData
from config import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(indicators)
app.register_blueprint(respData)
app.config.from_object(config['development'])


if __name__ == "__main__":
    app.run(debug=True)