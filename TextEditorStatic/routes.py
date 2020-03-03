import os
import secrets
from flask import render_template, url_for, flash, redirect, request, g , jsonify
from TextEditorStatic import app, db
from TextEditorStatic.forms import TextForm, UploadForm, Filepath
from TextEditorStatic.models import Results
from TextEditorStatic.lib.flaskcode.views import resource_data
import ntpath

@app.route('/', methods=['GET','POST'])

def index():

	return redirect('/flaskcode')   

@app.route('/runScript',methods=['GET','POST'] )
def runScript():
    path = "C:\\Users\\AOprescu\\Desktop\\Texas_Tool\\TestFolder\\test_script.py"
    cmd = "python "
    cmd += resource_data.file_path

    head, tail = ntpath.split(resource_data.file_path)
    file_name = tail or ntpath.basename(head)

    returned_value = os.system(cmd) 
    db.session.add(Results(test_result=returned_value,test_name=file_name))
    db.session.commit() 
    return redirect('flaskcode')

@app.route('/generateUML',methods=['GET','POST'] )
def generateUML():
    path = "C:/Users/AOprescu/Desktop/Texas_Tool/Doris/TextEditorStatic/lib/Conversion_App/conversion_app.py "
    cmd = "python "
    cmd += path
    cmd += "1 "
    cmd += resource_data.file_path
    cmd += " C:/Users/AOprescu/Desktop/Texas_Tool/Doris/TextEditorStatic/lib"
    returned_value = os.system(cmd)  
    return redirect('flaskcode')

@app.route('/generatePython',methods=['GET','POST'] )
def generatePython():
    path = "C:/Users/AOprescu/Desktop/Texas_Tool/Doris/TextEditorStatic/lib/Conversion_App/conversion_app.py "
    cmd = "python "
    cmd += path
    cmd += "2 "
    cmd += resource_data.file_path
    cmd += " C:/Users/AOprescu/Desktop/Texas_Tool/Doris/TextEditorStatic/lib"
    returned_value = os.system(cmd)  
    return redirect('flaskcode')

