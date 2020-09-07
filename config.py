import os

class Config():
    CSRF_ENABLE =True
    SECRET = '7#30205211AGR%'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva2:de_m7jBG^WZ=@localhost:3306/dashboard_prof'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:30205212agr=@localhost:3308/dashboard_python'
app_config = {
    'development': DevelopmentConfig(),
    'testing': None
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'