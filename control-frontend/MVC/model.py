class DataModel:
    # TODO - figure out what data needs to be stored in the model and how to do it
    def __init__(self):
        # TODO replace this with data from json
        self.__temperature_prefs = {'min': 22, 'max': 23, 'freqency': 3}
        self.__heater_data = {'ip': "192.168.88.236", 'email': "email@gmail.com", 'password': "Password123"}

    def read_json(self):
        # TODO read json from file  
        pass

    def get_min(self):
        return self.__temperature_prefs['min']

    def get_max(self):
        return self.__temperature_prefs['max']

    def get_frequency(self):
        return self.__temperature_prefs['frequency']
    
    def get_heater_data(self):
        # TODO read json from file
        return self.__heater_data
    
    def set_password(self, password):
        self.__heater_data['password'] = password

    def set_email(self, email):
        self.__heater_data['email'] = email