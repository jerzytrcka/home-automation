from PyP100 import PyP100

from hardware_interfaces.init_decorator import verify_initialized
from hardware_interfaces.interfaces import Heater

class TapoSmartPlug(Heater):
    ''' Class to interface with the tapo P110 smart plug '''
    def __init__(self, fallback_method):
        self.p110 = None
        self.initialized = False
        self.fallback_method = fallback_method
    

    def initialize(self, data):
        try:
            self.p110 = PyP100.P100(data['ip'], data['email'], data['password'])
            self.p110.handshake()
            self.initialized = True
        except:
            self.initialized = False


    @verify_initialized
    def turn_on(self):
        print("Turning heater on")
        self.p110.turnOn()


    @verify_initialized
    def turn_off(self):
        print("Turning heater off")
        self.p110.turnOff()

    def get_initialized(self):
        return self.initialized
