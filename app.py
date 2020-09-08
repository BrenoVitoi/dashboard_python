from flask import Flask, request, redirect, render_template, Response, json, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user
from functools import wraps
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
import datetime
import controllers as ctrl



def create_app(config):
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper' #Admin
    db = SQLAlchemy(app) #Database
    start_views(app, db) #Admin
    Bootstrap(app) #Admin


    db.init_app(app) #Database
    config.APP = app

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/report', methods=['POST'])
    def report():
        state = request.form['state']
        disease = request.form['disease']
        estadoSaude = request.form['estadoSaude']
        patients = ctrl.reportByState(state, disease)
        return Response(json.dumps(patients, ensure_ascii=False), mimetype='application/json'), 200, {}