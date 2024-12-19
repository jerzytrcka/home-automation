from abc import abstractmethod, ABC

class Thermometer(ABC):
    @abstractmethod
    def get_temperature(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_initialized(self) -> bool:
        raise NotImplementedError
    
    def initialize(self):
        raise NotImplementedError

class Heater(ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError
    
    @abstractmethod
    def turn_off(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def get_initialized(self) -> bool:
        raise NotImplementedError
    
    def initialize(self):
        raise NotImplementedError
