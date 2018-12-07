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
    'mysql+pymysql://root:123456@192.168.4.107:3306/crawl_manage?charset=utf8'


config = {
    'developmemt': DevelopmentConfig,
    'default': DevelopmentConfig,
}
