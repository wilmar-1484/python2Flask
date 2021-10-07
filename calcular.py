
from flask import Flask, render_template, abort,request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route("/calculadora", methods=["get","post"])
def calculadora():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		operador=request.form.get("operador")
	
		try:
			resultado=eval(num1+operador+num2)
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		return render_template("calculadora.html")

app.run(host='0.0.0.0', port=5000, debug=True)