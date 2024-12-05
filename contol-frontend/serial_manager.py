import serial, time

class SerialManager:
    ser = serial.Serial(None, 9600, timeout=1)
    end_char = b"\\\\n" # used to indicate end of message

    def send_serial(self, message):
        message = message.encode()
        message += self.end_char
        #self.ser.write(message)

        # for testing
        print("Sent message: ", message)

    def read_serial(self):
        # TODO consider adding pre processing here or in a helper function
        message = self.ser.read_until(self.end_char)
        return message
    
    def check_connection(self):
        # TODO implement this
        pass