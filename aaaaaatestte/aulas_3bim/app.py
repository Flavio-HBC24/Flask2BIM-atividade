from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stringqueninguémsabe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Empresa, Funcionarios
db.init_app(app)
migrate = Migrate(app, db)

from modulos.empresa.empresa import bp_empresa
app.register_blueprint(bp_empresa, url_prefix='/empresa')

from modulos.funcionarios.funcionarios import bp_funcionarios
app.register_blueprint(bp_funcionarios, url_prefix='/funcionarios')

@app.route('/')
def index():
    return render_template("ola.html")