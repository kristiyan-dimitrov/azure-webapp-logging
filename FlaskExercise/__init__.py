import logging
import logging.config
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes

logging.basicConfig(level=logging.WARNING)



import FlaskExercise.views