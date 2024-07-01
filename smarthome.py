from device import Light, Thermostat, DoorLock
from controller import LightingController, TemperatureController

class SmartHome:
    def __init__(self):
        self.devices = []
        self.controllers = []

    def add_device(self, device):

    def add_controller(self, controller):

    def get_device_status(self, device_id):

    def get_controller_devices(self, controller_id):


smart_home = SmartHome()

# Adding devices
light1 = Light("L001", "Living Room Light", brightness=50)
thermostat1 = Thermostat("T001", "Hallway Thermostat", current_temp=19)
doorlock1 = DoorLock("D001", "Front Door Lock")

smart_home.add_device(light1)
smart_home.add_device(thermostat1)
smart_home.add_device(doorlock1)

# Adding controllers
temp_controller = TemperatureController("C001", "Main Temperature Controller")
lighting_controller = LightingController("C002", "Main Lighting Controller")

smart_home.add_controller(temp_controller)
smart_home.add_controller(lighting_controller)

# Assign devices to controllers
temp_controller.add_device(thermostat1)
lighting_controller.add_device(light1)

# Control devices
temp_controller.maintain_temperature()
lighting_controller.adjust_lighting(75, "warm white")

print(smart_home.get_device_status("L001"))  # True
print(smart_home.get_device_status("T001"))  # True
print(smart_home.get_controller_devices("C002"))  # ["Living Room Light"]
