from flask import Blueprint, render_template, request, redirect, flash
from models import Funcionarios
from models import Empresa
from database import db

bp_funcionarios = Blueprint('funcionarios', __name__, template_folder='templates')

@bp_funcionarios.route('/')
def index():
    dados = Funcionarios.query.all()
    return render_template('funcionarios.html', funcionarios = dados)

@bp_funcionarios.route('/add')
def add():
    dados = Empresa.query.all()
    return render_template('funcionarios_add.html', empresa = dados)

@bp_funcionarios.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cargo = request.form.get('cargo')
    id_empresa = request.form.get('id_empresa')
    if nome and cargo and id_empresa:
        bd_pedido = Funcionarios(nome, cargo, id_empresa)
        db.session.add(bd_pedido)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/funcionarios')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/funcionarios/add')





