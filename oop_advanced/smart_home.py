
from abc import ABC, abstractmethod

# Smart device class
class SmartDevice(ABC):

    def __init__(self,device_name):
        self.device_name = device_name
        self._power_state = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_status(self):
        if self._power_state:
            print(f"{self.device_name} is currently On.")
        else:
            print(f"{self.device_name} is currently Off.")


# Light Class
class Light(SmartDevice):
    def __init__(self,brightness = 0):
        super().__init__("Light Device")
        # minimum : 0
        # maximum : 100
        self._brightness = 100 if brightness > 100 else (0 if brightness < 0 else brightness)

    def turn_on(self):
        self._power_state = True
        print(f"{self.device_name} has been turned on.")


    def turn_off(self):
        self._power_state = False
        print(f"{self.device_name} has been turned off.")

    def set_brightness(self,value):
        if value < 0:
            self._brightness = 0
        elif value > 100:
            self._brightness = 100
        else:
            self._brightness = value

        print(f"{self.device_name} Brightness updated to: {self._brightness}")


# Thermostat class
class Thermostat(SmartDevice):
    def __init__(self,temperature):
        super().__init__("Thermostat")
        # minimum : 10
        # maximum : 35
        self._temperature = 10 if temperature < 10 else (35 if temperature > 35 else temperature)

    def turn_on(self):
        self._power_state = True
        print(f"{self.device_name} has been turned on.")

    def turn_off(self):
        self._power_state = False
        print(f"{self.device_name} has been turned off.")


# Security Camera Class
class SecurityCamera(SmartDevice):
    def __init__(self):
        super().__init__("Security Camera")
        self._recording_state = False

    def turn_on(self):
        self._power_state = True
        print(f"{self.device_name} has been turned on.")

    def turn_off(self):
        self._power_state = False
        print(f"{self.device_name} has been turned off.")

    def start_recording(self):
        if not self._power_state:
            print(f"{self.device_name} is currently off, turn it on first to start recording")
            return False

        self._recording_state = True
        print(f"{self.device_name} has started recording.")
        return True

    def  stop_recording(self):
        if not self._power_state:
            print(f"{self.device_name} is currently off, failed to stop recording because its not on (nothing happened)")
            return False

        self._recording_state = False
        print(f"{self.device_name} has stopped recording.")
        return True


# SmartHome controller class
class SmartHomeController():
    def __init__(self):
       self.list_of_devices = []

    def add_device(self,device):
        self.list_of_devices.append(device)

    def turn_all_on(self):
        for device in self.list_of_devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.list_of_devices:
            device.turn_off()

    def show_all_status(self):
        for device in self.list_of_devices:
            device.device_status()