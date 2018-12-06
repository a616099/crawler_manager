from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models import Config, Tasks


class ConfigForm(FlaskForm):
    name = StringField('程序名称', validators=[DataRequired(), Length(1, 64)])
    owner = StringField('采集负责人', validators=[DataRequired(), Length(1, 64)])
    cycle = StringField('采集周期', validators=[DataRequired(), Length(1, 64)])
    detail_time = StringField('具体采集时间', validators=[DataRequired(), Length(1, 64)])
    task_table_name = StringField('任务表名', validators=[DataRequired(), Length(1, 64)])
    task_table_time = StringField('任务表时间字段', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('确定')
