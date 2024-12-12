from PyP100 import PyP100

from hardware_interfaces.init_decorator import verify_initialized

class SmartPlug():
    ''' Class to interface with the tapo P110 smart plug '''
    def __init__(self, fallback_method):
        self.p110 = None
        self.initialized = False
        self.fallback_method = fallback_method
    

    def initialize(self, data):
        ''' Initializes the smart plug and configures it '''
        try:
            self.p110 = PyP100.P100(data['ip'], data['email'], data['password'])
            self.p110.handshake()
            self.initialized = True
        except:
            self.initialized = False


    @verify_initialized
    def turn_on(self):
        ''' Turns on the smart plug. '''
        print("Turning on")
        self.p110.turnOn()


    @verify_initialized
    def turn_off(self):
        ''' Turns off the smart plug '''
        print("Turning off")
        self.p110.turnOff()