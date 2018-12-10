import bluetooth_
import json

from criptografia import crypt
from criptografia import key
from flask import Flask
from flask import request

app = Flask(__name__)
bluetooth = bluetooth_.Bluetooth('20:16:10:25:29:97')
crypt = crypt.Crypt(key.KEY)

@app.route("/", methods=["POST"])
def listen():
   solicitacao = json.loads(crypt.decriptografar(request.data))['op']

   if solicitacao == 'conect':
      return ('', 200) if bluetooth.conectar() else ('', 503)
   elif solicitacao == 'frente':
      return ('', 200) if bluetooth.enviar('F') else ('', 503)
   elif solicitacao == 'atras':
      return ('', 200) if bluetooth.enviar('B') else ('', 503)
   elif solicitacao == 'dir':
      return ('', 200) if bluetooth.enviar('D') else ('', 503)
   elif solicitacao == 'esq':
      return ('', 200) if bluetooth.enviar('E') else ('', 503)

if __name__ == '__main__':
    app.run(debug=True)
