import unittest
from smart_home import SmartHomeController,Thermostat,SecurityCamera,Light

class TestLightDevice(unittest.TestCase):
    def test_valid_constructor_brightness(self):
        light = Light(brightness=30)
        self.assertEqual(light._brightness, 30)

    def test_update_brightness(self):
        light = Light(brightness=30)
        self.assertEqual(light._brightness, 30)
        light.set_brightness(70)
        self.assertEqual(light._brightness, 70)

    def test_invalid_update_brightness(self):
        light = Light(brightness=30)
        self.assertEqual(light._brightness, 30)
        light.set_brightness(312)
        self.assertEqual(light._brightness, 100)

class TestThermostatDevice(unittest.TestCase):
    def test_valid_constructor(self):
        thermostat = Thermostat(25)
        self.assertEqual(thermostat._temperature, 25)

    def test_invalid_constructor_high_temp(self):
        thermostat = Thermostat(100)
        self.assertEqual(thermostat._temperature, 35)

    def test_invalid_constructor_low_temp(self):
        thermostat = Thermostat(-51)
        self.assertEqual(thermostat._temperature, 10)

class TestSecurityCameraDevice(unittest.TestCase):
    def test_camera_recording_off_constructor(self):
        camera = SecurityCamera()
        self.assertFalse(camera._recording_state)

    def test_recording_on(self):
        camera = SecurityCamera()
        camera.turn_on()
        camera.start_recording()
        self.assertTrue(camera._recording_state)


class TestSmartHomeController(unittest.TestCase):
    def test_turn_all_on(self):
        home = SmartHomeController()
        my_light = Light(brightness=50)
        my_heat = Thermostat(temperature=21)
        my_cam = SecurityCamera()

        home.add_device(my_light)
        home.add_device(my_heat)
        home.add_device(my_cam)

        home.turn_all_on()
        for device in home.list_of_devices:
            self.assertTrue(device._power_state)

    def test_turn_all_off(self):
        home = SmartHomeController()
        my_light = Light(brightness=50)
        my_heat = Thermostat(temperature=21)
        my_cam = SecurityCamera()

        home.add_device(my_light)
        home.add_device(my_heat)
        home.add_device(my_cam)

        home.turn_all_on()
        for device in home.list_of_devices:
            self.assertTrue(device._power_state)

        home.turn_all_off()
        for device in home.list_of_devices:
            self.assertFalse(device._power_state)