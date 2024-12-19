import serial

import serial.serialutil
from hardware_interfaces.init_decorator import verify_initialized
from hardware_interfaces.interfaces import Thermometer

class SerialThermometer(Thermometer):
    def __init__(self, fallback_method):
        """
            Initialize the SerialManager object.
            :param fallback_method: The method to call if the serial connection is not available upon sending a message.
        """
        self.initialized = False 

        self.serial_end_char = b"\\n" # used to indicate end of serial transmission
        self.msg_end_char = '\\' # used to indicate end of message string
        self.start_char = 'b' # used to indicate start of message
        self.listen_frequency = 1000 # in milliseconds
        self.fallback_method = fallback_method

        # For now hardcode initialization here, change this for GUI mode
        self.initialize()


    @verify_initialized    
    def send_serial(self, message):
        message = message.encode()
        message += self.end_char
        self.ser.write(message)

    @verify_initialized
    def read_serial(self):
        # TODO consider adding pre processing here or in a helper function
        message = self.ser.read_until(self.serial_end_char)
        message = message.decode()
        if message == '':
            return None
        
        return message
    
    def get_temperature(self):
        """
            Read and extract the temperature from the serial port. If the temperature is not recieved correctly, returns None.
        """
        message = self.read_serial()
        if message is None:
            return None
        
        # Compute the start and end indices of the temperature
        start_index = message.find(self.start_char) + 1
        end_index = message.find(self.msg_end_char) - 1

        # Extract the temperature from the message
        temperature = message[start_index:end_index]

        # If the circuit malfunctions, this returns an error
        try:
            temperature = float(temperature)
        except ValueError:
            print('Error: Received invalid temperature value. Check the circuit.')
            return None
        
        return temperature


    def initialize(self):
        ''' Initializes the serial connection, hardcoded on COM3 for now. Robust against serial exceptions. '''
        try:
            self.ser = serial.Serial('COM3', 9600, timeout=1)
            self.initialized = True

        except serial.serialutil.SerialException:
            self.initialized = False

    def get_initialized(self):
        return self.initialized
