import bluetooth

class Bluetooth:
    BREAK_LINE = '@'

    def __init__(self, addr_bluetooth):
        try:
            self.__addr_bluetooth = addr_bluetooth
            self.__sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.conectar()
        except Exception as e:
            print(e)
            self.__is_connect = False

    def conectar(self):
        try:
            self.__sock.connect((self.__addr_bluetooth, 1))
            print("Connected ", self.__sock.getpeername())
            self.__is_connect = True
        except Exception as e:
            self.__is_connect = False
        
        return self.__is_connect

    def enviar(self, msg):
        try:
            sock.send(msg + BREAK_LINE)
        except Exception as e:
            self.__is_connect = False
        
        return self.__is_connect