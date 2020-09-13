
import os
import sys

now_path = os.path.abspath('.')
project_name = sys.argv[1]
print(project_name)

init_text = '''from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('%s')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from %s import views, errors, commands''' % (project_name ,project_name)


commands_text = '''import click

from %s import app, db
from %s.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created some fake messages.' ) ''' % (project_name ,project_name)



error_text = '''from flask import render_template

from %s import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500''' % project_name

forms_text = '''from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()'''

models_text = '''from datetime import datetime

from %s import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)''' % project_name

settings_text = '''import os
import sys

from %s import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
''' % project_name


views_text = '''from flask import flash, redirect, url_for, render_template

from %s import app, db
from %s.forms import HelloForm
from %s.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)''' % (project_name,project_name,project_name)


def make_all(project_name):
    
    # print(now_path)
    os.mkdir(project_name)
    project_path = now_path + '/' + project_name
    # print(project_path)
  
    os.system("touch  %s/__init__.py" % project_name)
    os.system("mkdir  %s/templates" % project_name) 
    os.system("mkdir  %s/static" % project_name) 
    os.system("touch  %s/views.py" % project_name)
    os.system("touch  %s/forms.py" % project_name)
    os.system("touch  %s/errors.py" % project_name)
    os.system("touch  %s/models.py" % project_name)
    os.system("touch  %s/commands.py" % project_name)
    os.system("touch  %s/settings.py" % project_name)

    os.system("cp -r static %s/" % project_name)
    os.system("cp -r templates %s/" % project_name)
    
    
    file_handle=open(project_path+'/__init__.py',mode='w')
    file_handle.write(init_text)
    file_handle.close()

    file_handle=open(project_path+'/commands.py',mode='w')
    file_handle.write(commands_text)
    file_handle.close()

    file_handle=open(project_path+'/errors.py',mode='w')
    file_handle.write(error_text)
    file_handle.close()

    file_handle=open(project_path+'/forms.py',mode='w')
    file_handle.write(forms_text)
    file_handle.close()

    file_handle=open(project_path+'/models.py',mode='w')
    file_handle.write(models_text)
    file_handle.close()

    file_handle=open(project_path+'/settings.py',mode='w')
    file_handle.write(settings_text)
    file_handle.close()


    file_handle=open(project_path+'/views.py',mode='w')
    file_handle.write(views_text)
    file_handle.close()

isExists=os.path.exists(now_path+'/'+project_name)

if not isExists:
    make_all(project_name)

else:
    print('The project name is exist')
 





