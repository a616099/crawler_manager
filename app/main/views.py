from flask import render_template, redirect
from .. import db
from . import main
from .forms import ConfigForm
from ..models import Config

@main.route('/config', methods=['GET', 'POST'])
def config():
    form = ConfigForm()
    if form.validate_on_submit():
        config = Config(name=form.name.data,
                        owner=form.owner.data,
                        cycle=form.cycle.data,
                        detail_time=form.detail_time.data,
                        task_table_name=form.task_table_name.data,
                        task_table_time=form.task_table_time.data,)
        db.session.add(config)
        db.seesion.commit()
        return redirect(url_for())
    return render_template('config.html', form=form)

@main.route('/')
def index():
    return 'Hello'
