# -*- coding: utf-8 -*-


import os
from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/redirect_uri', methods=('GET', 'POST'))
    def redirect_uri():
        """
        授权回调URI
        :param code: 授权码
        :param state: 请求状态码
        """
        if request.method == 'GET':
            if 200 == request.args['state']:
                code = request.args['code']
                return 'ok'
            else:
                return 'false'

    return app
