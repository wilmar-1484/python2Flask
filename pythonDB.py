from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#Instancia de la aplicacion
app = Flask(__name__)

#Configuracion de string de conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#Instancia de la conexion a la base de datos asociada a esta aplicacion
db = SQLAlchemy(app)

#Modelo de base de datos
# internamente se termina convirtiendo en una tabla
class Persona(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(100))

	def __init__(self, nombre):
		self.nombre = nombre

	def __repr__(self):
		return '<Persona: {}>'.format(self.nombre)

	def __str__(self):
		return self.nombre

#Esta instruccion crea el esquema de la base de datos
db.create_all()

### insertar
nombre="Juan"

db.session.query(Persona).delete()
db.session.add(Persona("Pedro"))
db.session.add(Persona("Pablo"))
db.session.add(Persona("Ana"))

db.session.commit()


@app.route('/')
#Funcion/controlador asociado a la ruta
def index():
	personas = Persona.query.all()
	return render_template('nombres.html',personas=personas)

if __name__ == "__main__":
	app.run(debug=True)