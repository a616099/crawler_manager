import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abc.123'

    #staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql+pymysql://nprice:ways369@192.168.1.56:3306/npriceDB?charset=utf8'


config = {
    'developmemt': DevelopmentConfig,
    'default': DevelopmentConfig,
}
