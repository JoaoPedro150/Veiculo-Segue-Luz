import controle

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/connect", methods=["POST"])
def connect():
   return ('', 200) if controle.iniciar() else ('', 503)

@app.route("/mover", methods=["POST"])
def mover():
   return ('', 200) if movimento(request.headers['mov']) else ('', 503)

def movimento(movimento):
   if(movimento == 'F'):
      return controle.mover_frente()
   elif(movimento == 'B'):
      return controle.mover_atras()
   elif(movimento == 'E'):
      return controle.mover_esquerda()
   elif(movimento == 'D'): 
      return controle.mover_direita()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
