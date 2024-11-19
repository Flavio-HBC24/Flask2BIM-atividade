from flask import Blueprint, render_template, request, redirect, flash
from models import Empresa
from database import db

bp_empresa = Blueprint('empresa', __name__, template_folder='templates')

@bp_empresa.route('/')
def index():
    dados = Empresa.query.all()
    return render_template('empresa.html', empresa = dados)

@bp_empresa.route('/add')
def add():
    return render_template('empresa_add.html')

@bp_empresa.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if nome and cidade:
        bd_empresa = Empresa(nome, cidade)
        db.session.add(bd_empresa)
        db.session.commit()
        flash('Empresa salva com sucesso!!!')
        return redirect('/empresa')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/empresa/add')
