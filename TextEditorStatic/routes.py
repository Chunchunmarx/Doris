import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from TextEditorStatic import app
from TextEditorStatic.forms import TextForm, UploadForm, Filepath


nume_fisier = ""

def dir_tree(abs_path, abs_root_path):
    tree = dict(
        name=os.path.basename(abs_path),
        path_name=abs_path[len(abs_root_path):].lstrip('/\\'),# TODO: use os.path.relpath
        children=[]
    )
    try:
        dir_entries = os.listdir(abs_path)
    except OSError:
        pass
    else:
        for name in dir_entries:
            new_path = os.path.join(abs_path, name)
            if os.path.isdir(new_path):
                tree['children'].append(dir_tree(new_path, abs_root_path))
            else:
                tree['children'].append(dict(
                    name=os.path.basename(new_path),
                    path_name=new_path[len(abs_root_path):].lstrip('/\\'),# TODO: use os.path.relpath
                    is_file=True,
                ))
    return tree



@app.route('/', methods=['GET','POST'])
  
def index():
	dtree = dir_tree("C:\\Users\\AOprescu\\Desktop\\Tony", "C:\\Users\\AOprescu\\Desktop\\Tony" + '/')
	form = TextForm()
	if form.validate_on_submit():
		text_write = open(index.nume_fisier, 'w')
		text_write.write(form.text_box.data)
		text_write.close()
	if request.args.get('messages') is not None:
		index.nume_fisier = request.args.get('messages')
		
		text_read = open(index.nume_fisier, 'r')
		content = text_read.read()
		text_read.close()
		form.text_box.data = content

	return render_template('index.html', form=form, dtree=dtree)

@app.route('/success', methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		print(request.files)
		f.save(f.filename)

	return redirect(url_for('index', messages=f.filename))

@app.route('/compiled',methods=['GET','POST'] )
def compile():
    path = "C:\\Users\\AOprescu\\Desktop\\Flask\\Workspace\\Script\\script.py"
    cmd = "python "
    cmd += path
    returned_value = os.system(cmd)  
    return redirect(url_for('index'))
