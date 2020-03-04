from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from TextEditorStatic.lib import flaskcode
from TextEditorStatic.config import File_path

app = Flask(__name__)





app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = File_path.dict_obj["project_path"]
app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')
db = SQLAlchemy(app)
app.path = flaskcode


from TextEditorStatic import routes