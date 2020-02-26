from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import flaskcode

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = 'C:/Users/AOprescu/Desktop/flaskcode'
app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')
db = SQLAlchemy(app)



from TextEditorStatic import routes