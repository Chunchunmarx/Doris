# -*- coding: utf-8 -*-
import os
import mimetypes
from flask import render_template, abort, jsonify, send_file, g, request
from .utils import write_file, dir_tree, get_file_extension
from . import blueprint
import Database 
import datetime


@blueprint.route('/')
def index():
    dirname = os.path.basename(g.flaskcode_resource_basepath)
    dtree = dir_tree(g.flaskcode_resource_basepath, g.flaskcode_resource_basepath + '/')
    return render_template('flaskcode/index.html', dirname=dirname, dtree=dtree)


@blueprint.route('/reportingview')
def reportingview():
    python_values = []
    columns = ['date', 'test_result'] 
    now = datetime.datetime.now()
    values_1 = [ now.strftime("%Y-%m-%d"), 'Failed']
    values_2 = [ now.strftime("%Y-%m-%d"), 'Success']
    success_list = Database.DatabaseResultsHandler.filter(columns, values_2)
    fail_list = Database.DatabaseResultsHandler.filter(columns, values_1)
    python_values.append(len(success_list))
    python_values.append(len(fail_list))
    return render_template('flaskcode/reporting_view.html',python_values=python_values)


@blueprint.route('/resource-data/<path:file_path>.txt', methods=['GET', 'HEAD'])
def resource_data(file_path):
    file_path = os.path.join(g.flaskcode_resource_basepath, file_path)
    resource_data.file_path = file_path
    if not (os.path.exists(file_path) and os.path.isfile(file_path)):
        abort(404)
    response = send_file(file_path, mimetype='text/plain', cache_timeout=0)
    mimetype, encoding = mimetypes.guess_type(file_path, False)
    if mimetype:
        response.headers.set('X-File-Mimetype', mimetype)
        extension = mimetypes.guess_extension(mimetype, False) or get_file_extension(file_path)
        if extension:
            response.headers.set('X-File-Extension', extension.lower().lstrip('.'))
    if encoding:
        response.headers.set('X-File-Encoding', encoding)
    return response


@blueprint.route('/update-resource-data/<path:file_path>', methods=['POST'])
def update_resource_data(file_path):
    file_path = os.path.join(g.flaskcode_resource_basepath, file_path)
    is_new_resource = bool(int(request.form.get('is_new_resource', 0)))
    if not is_new_resource and not (os.path.exists(file_path) and os.path.isfile(file_path)):
        abort(404)
    success = True
    message = 'File saved successfully'
    resource_data = request.form.get('resource_data', None)
    if resource_data:
        success, message = write_file(resource_data, file_path)
        print(file_path)
    else:
        success = False
        message = 'File data not uploaded'
    return jsonify({'success': success, 'message': message})


