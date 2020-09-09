# -*- coding: utf-8 -*-


from app import app
from flask import jsonify
import time
from app.config.Config import Config as config_app


###
# The only route of this API.
#
# @method <get>
# @header string <secret>
# @return string <timezone>
# @return integer <posix.timestamp>
# @return integer <posix.millis>
###
@app.route('/secret/<secret>/', methods=['GET'])
def default(secret):
    response = {
        'timezone': config_app().data['timezone'],
        'posix': {
            'timestamp': int(round(time.time())),
            'millis': int(round(time.time() * 1000))
        }
    }
    response = jsonify(response)
    response.status_code = 200
    return response
