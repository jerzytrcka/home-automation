# Replace these imports with custom files for different hardware
from hardware_interfaces import serial_manager as thermometer 
from hardware_interfaces import smart_plug as heater

class HardwareManager():

    def __init__(self, model, view=None):
        """ Initializes the hardware manager with the given model and view.
        :param view: None by default, if running in GUI mode this should be set to the GUI object.
        """
        # TODO docstring
        self.model = model
        
        self.thermometer = thermometer.SerialManager() 
        # Uncomment this for gui mode
        # self.configure_heater()

    def listen_for_update(self):
        """ Checks for updates from the arduino and calls the appropriate function based on the message received """
        temperature = self.thermometer.get_temperature()
        print("Temperature: ", temperature)
        if temperature is None:
            return
        elif temperature < self.model.get_min():
            self.heater.turn_on()

        elif temperature > self.model.get_max():
            self.heater.turn_off()
        
    def configure_heater(self):
        """ Configures the heater with the given data """
        data = self.model.get_heater_data()
        self.heater = heater.SmartPlug()
        self.heater.configure(data)
        