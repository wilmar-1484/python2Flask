
from flask import Flask, render_template, abort,request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/validar', methods=["get","post"])
def validar():
    if request.method=="POST":
        usuario=request.form.get("usuario")
        clave=request.form.get("clave")
        
	
    return "el usuario es:{}".format(usuario)

app.run(host='0.0.0.0', port=5000, debug=True)
