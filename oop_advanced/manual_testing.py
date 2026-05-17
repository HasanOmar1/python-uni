from smart_home import Light,Thermostat,SecurityCamera,SmartHomeController

def main():

    home = SmartHomeController()

    my_light = Light(brightness=50)
    my_heat = Thermostat(temperature=21)
    my_cam = SecurityCamera()

    home.add_device(my_light)
    home.add_device(my_heat)
    home.add_device(my_cam)

    my_light.set_brightness(70)
    my_light.set_brightness(311)

    my_heat.device_status()
    my_heat.turn_on()
    my_heat.device_status()

    my_cam.device_status()
    my_cam.start_recording()
    my_cam.stop_recording()
    my_cam.turn_on()
    my_cam.device_status()
    my_cam.start_recording()
    my_cam.stop_recording()


if __name__ == '__main__':
    main()