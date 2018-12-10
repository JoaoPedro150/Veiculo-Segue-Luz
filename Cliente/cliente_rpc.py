import requests
from criptografia import crypt
from criptografia import key
import json

class Cliente:
    def __init__(self, host, port):
        self.__server_addr = (host, port)
        self.__crypt = crypt.Crypt(key.KEY)
    
    def __send(self, movimento):
        return requests.post('http://%s:%d' % 
        (self.__server_addr[0], self.__server_addr[1]), 
        data=self.__crypt.criptografar(json.dumps({'op': movimento}))).text

    def iniciar(self):
        return self.__send('conect')

    def mover_frente(self):
        return self.__send('frente')

    def mover_atras(self):
        return self.__send('atras')

    def mover_esquerda(self):
        return self.__send('esq')

    def mover_direita(self):
        return self.__send('dir')