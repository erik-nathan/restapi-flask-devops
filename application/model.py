from .db import db


class UserModel(db.Document):
    '''Declarando a classe que vai se conectar com o banco.'''
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)
