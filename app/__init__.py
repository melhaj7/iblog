from flask import Flask  # pylint: disable=import-error
from config import Config
from flask_sqlalchemy import SQLAlchemy # pylint: disable=import-error
from flask_migrate import Migrate # pylint: disable=import-error

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models