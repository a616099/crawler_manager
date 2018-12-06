from . import db

class Config(db.Model):
    __tablename__ = 'crawler_manager_config'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    owner = db.Column(db.String(64), unique=True)
    cycle = db.Column(db.String(64), unique=True)
    detail_time = db.Column(db.String(64), unique=True)
    task_table_name = db.Column(db.String(64), unique=True)
    task_table_time = db.Column(db.String(64), unique=True)


class Tasks(db.Model):
    __tablename__ = 'crawler_manager_tasks'
    id = db.Column(db.Integer, primary_key=True)
    config_id = db.Column(db.Integer, db.ForeignKey('crawler_manager_config.id'))
    collect_time = db.Column(db.DateTime, unique=True)
    data_count = db.Column(db.Integer, unique=True)
