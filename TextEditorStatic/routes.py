import os
from flask import redirect
from TextEditorStatic import app, db
from TextEditorStatic.config import File_path
from TextEditorStatic.models import Results
from TextEditorStatic.lib.flaskcode.views import resource_data
import ntpath

@app.route('/', methods=['GET','POST'])

def index():

	return redirect('/flaskcode')   

@app.route('/runScript',methods=['GET','POST'] )
def runScript():
    
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
    #to be modified when Robert attaches his UML magic
    path = File_path.conversion_app_path
    cmd = "python "
    cmd += path
    cmd += " 1 "
    cmd += resource_data.file_path
    cmd += " String de test"
    returned_value = os.system(cmd)  
    return redirect('flaskcode')

@app.route('/generatePython',methods=['GET','POST'] )
def generatePython():
    #to be modified when Robert attaches his UML magic
    path = File_path.conversion_app_path
    cmd = "python "
    cmd += path
    cmd += " 2 "
    cmd += resource_data.file_path
    cmd += " String de test"
    returned_value = os.system(cmd)  
    return redirect('flaskcode')

