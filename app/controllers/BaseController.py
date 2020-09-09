# -*- coding: utf-8 -*-

from app import app
from flask import g, request, jsonify
import logging
from app.config.Config import Config as config_app
logger = logging.getLogger(config_app().data['import_name'])
from app.models.DefaultModel import Default as model_default


@app.before_request
def before_request():
    try:
        secret = request.path.split('/')[2]
    except:
        return stop(412, 'The parameter secret is empty or missing')
    model = model_default.get_by_secret(secret)
    if model is not None:
        if config_app().data['limit'].get(model.limit, None) is None:
            return stop(501, 'The requested functionality is not supported')
    if model is not None:
        counter = model_default.get_usage(model)
        if counter >= config_app().data['limit'][model.limit]:
            return stop(429, 'The usage limit has been reached')
    else:
        return stop(401, 'The secret used is not authorized')


@app.after_request
def after_request(f):
    if not hasattr(g, 'after_request_callbacks'):
        g.after_request_callbacks = []
    g.after_request_callbacks.append(f)
    try:
        secret = request.path.split('/')[2]
        model = model_default.get_by_secret(secret)
        model_default.update_usage(model)
    except:
        pass
    return f


def stop(status, msg, logger=True):
    response = {
        'status': status,
        'message': msg
    }
    if logger:
        log(response)
    response = jsonify(response)
    response.status_code = status
    return response


def err(status, msg=None, logger=False):
    response = {
        'status': status
    }
    if msg is not None:
        response['message'] = msg
    if logger:
        log(response)
    return response


def log(response):
    import time, traceback
    data = {
        'time': time.strftime('%m%d%y'),
        'status': response['status'],
        'remote_addr': request.remote_addr,
        'method': request.method,
        'full_path': request.full_path,
        'message': response['message']
    }
    try:
        data['traceback'] = traceback.format_exc()
    except:
        pass
    logger.error(data)
