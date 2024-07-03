from device import Device, Light, Thermostat


class Controller:

    def __init__(self, controller_id, name):
        self.controller_id = controller_id
        self.name = name
        self.devices = []

    def add_device(self, device: Device):
        self.devices.append(device)

    def get_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def control_device(self, device_id, action):
        device = self.get_device(device_id)
        if device:
            if action == "on":
                return device.turn_on()
            elif action == "off":
                return device.turn_off()
            else:
                print(f"Unknown action '{action}' for device '{device.name}'")
        else:
            print(f"No device found with ID {device_id}")

    def monitor_devices(self):
        for device in self.devices:
            print(device)


class LightingController(Controller):

    colors = ['warm white', 'neutral white', 'cool white']

    def __init__(self, controller_id, name):
        super().__init__(controller_id, name)

    def adjust_lighting(self, brightness, color):
        for device in self.devices:
            if isinstance(device, Light):
                device.brightness = brightness
                if color in self.colors:
                    device.color = color
                    print(f"{self.name}: Adjusted {device.name} to brightness {brightness} and color {color}")
                else:
                    print(f"Unknown color '{color}' for device '{device.name}'")


class TemperatureController(Controller):

    def __init__(self, controller_id, name):
        super().__init__(controller_id, name)
        self.target_temperature = None

    def maintain_temperature(self):
        for device in self.devices:
            if isinstance(device, Thermostat):
                current_temp = device.current_temp
                target_temp = device.target_temp
                if target_temp is not None:
                    if current_temp < target_temp - 1:
                        print(f"{device.name} start to warming temperature to {target_temp}")
                    elif current_temp > target_temp:
                        print(f"{device.name} start cooling down to {target_temp}")
                    else:
                        print(f"{device.name}'s temperature is maintained at {device.current_temp}°C")
                else:
                    print(f"{device.name} has no target temperature set")
            else:
                print(f"{device.name} is not a thermostat")

    def set_target_temperature(self, thermostat_id, target_temp):
        thermostat = self.get_device(thermostat_id)
        if isinstance(thermostat, Thermostat):
            thermostat.target_temp = target_temp
            print(f"{self.name}: Set {thermostat.name}'s target temperature to {target_temp}°C")
        else:
            print(f"{self.name}: No thermostat found with ID {thermostat_id}")

    def get_current_temperature(self, device: Thermostat):
        print(f"{device.name} current temperature is {device.current_temp}°C")
