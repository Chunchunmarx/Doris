import os
import secrets
from flask import render_template, url_for, flash, redirect, request, g , jsonify
from TextEditorStatic import app
from TextEditorStatic.forms import TextForm, UploadForm, Filepath
from TextEditorStatic.lib.flaskcode.views import resource_data

nume_fisier = ""

@app.route('/', methods=['GET','POST'])
  
def index():
	
	form = TextForm()
	if form.validate_on_submit():
		text_write = open(index.nume_fisier, 'w')
		text_write.write(form.text_box.data)
		text_write.close()
	if request.args.get('messages') is not None:
		index.nume_fisier = request.args.get('messages')
		
		text_read = open(index.nume_fisier, 'r')
		path = text_read.read()
		text_read.close()
		form.text_box.data = path
		app.config['FLASKCODE_RESOURCE_BASEPATH'] = path

	return redirect('/flaskcode')    #render_template('index.html', form=form, dtree=dtree)

@app.route('/success', methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		f = request.files['config_file']
		#print(f.read())
	
		
		path="C:\\Users\\AOprescu\\Desktop\\Texas Tool\\TestFolder"
		app.config['FLASKCODE_RESOURCE_BASEPATH'] = path

	return redirect('/flaskcode')


@app.route('/runScript',methods=['GET','POST'] )
def runScript():
    path = "C:\\Users\\AOprescu\\Desktop\\Texas_Tool\\TestFolder\\test_script.py"
    cmd = "python "
    cmd += resource_data.file_path
    returned_value = os.system(cmd)  
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

