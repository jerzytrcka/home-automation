# home-automation
## About the project
This repository contains code to control and automatic heater controller, like a thermostat. Currently compatible with an arduino-based ciruit for measuring temperature and Tapo smart plug for controling the heater, but this can be changed for other hardware (see 'contributing' section for how to do this).
## Getting started
### Dependencies
To run, install python, then the following libraries:
1. pyserial (for communication with an arduino)
```python
pip install pyserial
```
2. TapoP100 (for tapo smart plugs)
```python
pip install git+https://github.com/almottier/TapoP100.git@main
```

### Hardware
For the default heater controler you need a tapo smart plug, such as the P100 or P110. The program asks you for a user and password, which it needs to control the plug. This is the same as the password for the tapo smart plug. 

For the thermometer, by default you need an arduino connected via serial. It should be running the code found in the folder ```/arduino-code```. This has a dependency which you can install in the arduino IDE. The circuit for an AM2320 thermometer can be found under this [link](https://lastminuteengineers.com/am2320-temperature-humidity-sensor-arduino-tutorial/#google_vignette), however any thermometer compatible with an arduino can be used as long as your code sends messages in the same way as currently done.
### Running the program
1. Clone this repository or download and extract the .zip file. 
2. Go to the folder control-frontend. This contains the main file.
3. Run ```main.py```. Double click on the file, or open the terminal and execute:
```
python main.py
```

## Future changes
I am planning to add a simple GUI which will fix the problem of several values being hardcoded. This is mostly relevant for desired temperature and the IP of the smart plug which are hardcoded.