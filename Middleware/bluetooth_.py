import bluetooth

class Bluetooth:
    BREAK_LINE = '@'

    def __init__(self, addr_bluetooth):
        try:
            self.__addr_bluetooth = addr_bluetooth
        except Exception as e:
            print('INIT ->')
            print(e)

        self.__is_connect = False

    def conectar(self):
        if self.__is_connect:
            return True
        try:
            self.__sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.__sock.connect((self.__addr_bluetooth, 1))
            print("Connected ", self.__sock.getpeername())
            self.__is_connect = True
        except Exception as e:
            print('CONECTAR ->')
            print(e)
            self.__is_connect = False
        
        return self.__is_connect

    def __is_connect(self):
        return self.__is_connect

    def enviar(self, msg):
        try:
            if not self.__sock:
                self.conectar()

            self.__sock.send(msg + self.BREAK_LINE)
        except Exception as e:
            
            import traceback
            print('SEND ->')
            traceback.print_exc()
            self.__is_connect = False
        
        return self.__is_connect