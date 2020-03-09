# -*- coding: utf-8 -*-
"""flaskcode Flask Blueprint"""
import os
from flask import Blueprint, g, abort
from . import __pkginfo__
from Configuration import Configuration


__title__ = __pkginfo__.title
__version__ = __pkginfo__.version
__author__ = __pkginfo__.author
__email__ = __pkginfo__.email
__uri__ = __pkginfo__.uri
__description__ = __pkginfo__.description
__license__ = __pkginfo__.license
__copyright__ = __pkginfo__.copyright
__status__ = __pkginfo__.status


blueprint = Blueprint(
    'flaskcode',
    __name__,
    static_folder='static',
    template_folder='templates',
)


@blueprint.url_value_preprocessor
def manipulate_url_values(endpoint, values):
    if endpoint != 'flaskcode.static':
        resource_basepath = Configuration.get_instance().get_project_path()
        if not (resource_basepath and os.path.isdir(resource_basepath)):
            abort(500, '`FLASKCODE_RESOURCE_BASEPATH` is not a valid directory path')
        else:
            g.flaskcode_resource_basepath = os.path.abspath(resource_basepath).rstrip('/\\')


@blueprint.context_processor
def process_template_context():
    return dict(
        app_version=__version__,
        app_title=Configuration.get_instance().get_app_name(),
        editor_theme=Configuration.get_instance().get_editor_theme()
    )


from . import views
