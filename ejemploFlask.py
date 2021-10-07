
from flask import Flask 
from flask import request

app=Flask(__name__)

@app.route('/')
@app.route('/<nombre>')

def index(nombre='Sin nombre'):
     nombre = request.args.get('nombre', nombre)
     return """
     <body bgcolor=blue>
     <center><b>
     Hola {}
     </b></center>
     </body>
     """.format(nombre)

app.run(host='0.0.0.0', port=5000, debug=True)
