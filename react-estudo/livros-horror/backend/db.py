from app import app
from flask_sqlalchemy import SQLAlchemy


# Configuração da URI de conexão ao banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)