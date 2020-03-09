from flask import Flask
from TextEditorStatic.lib import flaskcode
from Configuration import Configuration
from Database import db
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['FLASKCODE_RESOURCE_BASEPATH'] = Configuration.get_instance().get_project_path()
app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')
app.path = flaskcode


# database settings
project_dir = os.path.dirname(os.path.abspath(__file__))
db_metadata = "sqlite:///{}".format(os.path.join(project_dir, "metadata.db"))
db_results = "sqlite:///{}".format(os.path.join(project_dir, "results.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = db_results

app.config["SQLALCHEMY_BINDS"] = {
    'sql_metadata': db_metadata,
    'sql_results': db_results
}

with app.app_context():
    db.init_app(app)


from TextEditorStatic import routes