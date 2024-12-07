import serial, time

class SerialManager:
    def __init__(self):
        self.ser = serial.Serial('COM3', 9600, timeout=1)
        self.serial_end_char = b"\\n" # used to indicate end of serial transmission
        
        self.msg_end_char = '\\' # used to indicate end of message string
        self.start_char = 'b' # used to indicate start of message
        self.listen_frequency = 1000 # in milliseconds

    def send_serial(self, message):
        message = message.encode()
        message += self.end_char
        #self.ser.write(message)

        # for testing
        print("Sent message: ", message)

    def read_serial(self):
        # TODO consider adding pre processing here or in a helper function
        message = self.ser.read_until(self.serial_end_char)
        message = message.decode()
        if message == '':
            return None
        
        return message
    
    def get_temperature(self):
        message = self.read_serial()
        if message is None:
            return None
        
        # Compute the start and end indices of the temperature
        start_index = message.find(self.start_char) + 1
        end_index = message.find(self.msg_end_char) - 1

        # Extract the temperature from the message
        temperature = message[start_index:end_index]
        temperature = float(temperature)
        return temperature

    def check_connection(self):
        # TODO implement this
        pass
