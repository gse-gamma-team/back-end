import os
import json
import subprocess

from flask import Flask, request, send_image

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
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
    
    @app.route('/train_model')
    def train_model():
        result = {
            "status": "Success",
            "message": ""
        }

        split = request.args.get('split', 'Fri')
        location = request.args.get('location', 'Shiga')
        preprocess = request.args.get('preprocess', 'None')
        model = request.args.get('model', 'XG')
        scoring = request.args.get('scoring', 'f1_macro')

        subprocess_result = subprocess.run(f'python app\model\main.py --mode train-grid --split {split} --location {location} --preprocess {preprocess} --model {model} --scoring {scoring}')

        if subprocess_result.returncode == 1:
            result["status"] = "Error"
            result["message"] = "Please see the console for details."

        return result
    
    @app.route('/get_chart')
    def get_chart():
        result = {
            "status": "Success",
            "message": ""
        }

        path = request.args.get('path', None)
        day = request.args.get('day', 'Mon')

        if path is None:
            result["status"] = "Error"
            result["message"] = "No path provided."

        subprocess_result = subprocess.run(f'python main.py --mode plot --path {path} --day {day}')

        if subprocess_result.returncode == 1:
            result["status"] = "Error"
            result["message"] = "Please see the console for details."

        return send_file(path, mimetype='image/gif')

    return app