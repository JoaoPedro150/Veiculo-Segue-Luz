import cliente_rpc

client = cliente_rpc.Cliente('127.0.0.1', 5000)

def iniciar():
    return client.iniciar()

def mover_frente():
    return client.mover_frente()

def mover_atras():
    return client.mover_atras()

def mover_esquerda():
    return client.mover_esquerda()

def mover_direita():
    return client.mover_direita()