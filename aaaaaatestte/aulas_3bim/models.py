from database import db


class Empresa(db.Model):
    __tablename__='empresa'
    id_empresa = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
    
    def __repr__(self):
        return "<Empresa {}>".format(self.nome)
    
class Funcionarios(db.Model):
    __tablename__='funcionarios'
    id_funcionario = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresa.id_empresa'))
    

    def __init__(self, nome, cargo, id_empresa):
        self.nome = nome
        self.cargo = cargo
        self.id_empresa = id_empresa

    
    def __repr__(self):
        return "<Empresa {}>".format(self.nome)
    
