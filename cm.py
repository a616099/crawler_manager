import os
from app import create_app, db
from app.models import Config, Tasks
from flask_migrate import Migrate


app = create_app(os.getenv.get('FLASK_CONFIG') or 'default')
#app = create_app('default')

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Config=Config, Tasks=Tasks)


