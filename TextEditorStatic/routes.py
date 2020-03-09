import os
from flask import redirect
from TextEditorStatic import app
from TextEditorStatic.lib.flaskcode.views import resource_data
import Helper
from Configuration import Configuration
import Database
import webbrowser

@app.route('/', methods=['GET','POST'])
def index():
    return redirect('/flaskcode')


@app.route('/runScript',methods=['GET', 'POST'])
def runScript():
    cmd = "python runtest.py -t " + os.path.join(Configuration.get_instance().get_project_path(), resource_data.file_path)
    test_result = Helper.run_command(cmd)

    test_name = Helper.get_filename(resource_data.file_path)
    Database.DatabaseResultsHandler.set(test_name, test_result)

    return redirect('flaskcode')


@app.route('/generateUML',methods=['GET', 'POST'])
def generateUML():
    generator_script = os.path.join(Configuration.get_instance().get_external_path(), "SequenceGenerator", "Application.py")
    Helper.run_command("python " + generator_script + " 1 " + resource_data.file_path + " ./")
    webbrowser.open_new_tab(Helper.get_file_without_extension(resource_data.file_path) + ".png")
    return redirect('flaskcode')


@app.route('/generatePython',methods=['GET', 'POST'])
def generatePython():
    generator_script = os.path.join(Configuration.get_instance().get_external_path(), "SequenceGenerator", "Application.py")
    Helper.run_command("python " + generator_script + " 2 " + resource_data.file_path + " ./")
    return redirect('flaskcode')