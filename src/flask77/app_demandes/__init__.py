from flask import Flask
from app_demandes.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app_demandes import routes
