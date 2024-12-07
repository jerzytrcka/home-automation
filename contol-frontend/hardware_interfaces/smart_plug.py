from PyP100 import PyP100

class SmartPlug():
    ''' Class to interface with the tapo P110 smart plug '''

    def __init__(self):
        self.p110 = None
        self.initialized = False

    def configure(self, data):
        ''' Initializes the smart plug and configures it '''
        self.p110 = PyP100.P100(data['ip'], data['email'], data['password'])
        self.p110.handshake()
        self.p110.login()
        self.initialized = True

    def turn_on(self):
        ''' Turns on the smart plug. '''
        if not self.initialized:
            raise Exception("Smart plug not initialized")
        print("Turning on")
        self.p110.turnOn()

    def turn_off(self):
        ''' Turns off the smart plug '''
        if not self.initialized:
            raise Exception("Smart plug not initialized")
        print("Turning off")
        self.p110.turnOff()