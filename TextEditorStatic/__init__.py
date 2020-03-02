from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from TextEditorStatic.lib import flaskcode
import os

app = Flask(__name__)


project_root_path=os.path.dirname(os.path.dirname(__file__))
config_file_path = project_root_path+'\\config.json'
f = open(config_file_path, "r")
imported_path = f.read()


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = imported_path
app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')
db = SQLAlchemy(app)
app.path = flaskcode





from TextEditorStatic import routes