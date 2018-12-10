import time, json
import base64
from Crypto.Cipher import AES
from Crypto import Random

class Crypt:
    def __init__( self, chave ):
        self.__chave = chave.ljust(16)

    def criptografar( self, conteudo):
        iv = Random.new().read( AES.block_size )
        cifra = AES.new( self.__chave, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cifra.encrypt( conteudo.ljust(16) ) ) 
    
    def decriptografar( self, conteudo):
        conteudo = base64.b64decode(conteudo)
        iv = conteudo[:16]
        cifra = AES.new(self.__chave, AES.MODE_CBC, iv )
        return cifra.decrypt( conteudo[16:] ).strip().decode()