from device import Device, Light, Thermostat


def check_device_status(func):
    def wrapper(controller, device, *args, **kwargs):
        if device.get_status() == 'off':
            print(f"Device '{device.name}' is currently off. Action '{func.__name__}' not allowed.")
        return func(controller, device, *args, **kwargs)
    return wrapper


class Controller:

    def __init__(self, controller_id, name):
        self.controller_id = controller_id
        self.name = name
        self.devices = []

    def add_device(self, device: Device):
        self.devices.append(device)


class LightingController(Controller):

    def __init__(self, controller_id, name):
        super().__init__(controller_id, name)

    @check_device_status
    def adjust_lighting(self, light: Light, brightness, color):
        light.brightness = brightness
        light.color = color


class TemperatureController(Controller):

    def __init__(self, controller_id, name):
        super().__init__(controller_id, name)

    @check_device_status
    def maintain_temperature(self, device: Thermostat, target_temp):
        device.target_temp = target_temp

    @check_device_status
    def get_current_temperature(self, device: Thermostat):
        print(f"{device.name} current temperature is {device.current_temp}°C")

