import json
from flask import Blueprint, render_template, abort, jsonify, request

from model import *
from utils import *

settings_module = Blueprint('settings_module', __name__)


@settings_module.route('/settings/')
def settings():
    settings = {}
    for setting in Settings.select():
        settings[setting.name] = setting.value
    return jsonify(settings)


@settings_module.route('/settings/update', methods=['POST', 'GET'])
def settings_update():
    if request.method == 'POST':
        for setting_name in request.form:
            print setting_name, request.form[setting_name]
            setting = Settings.get(Settings.name == setting_name)
            setting.value = request.form[setting_name]
            setting.save()
        return 'done'
    else:
        return 'This is a useless GET'

@settings_module.route('/settings/<setting_name>')
def get_setting(setting_name):
    try:
        setting = Settings.get(Settings.name == setting_name)
    except Exception, e:
        print e , '--> Setting not found'
        return 'Setting %s not found' % setting_name

    # a = json.loads(setting['value'])
    # print a

    return setting.value