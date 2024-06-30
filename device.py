def actoins_print(func):
    def wrapper(*args, **kwargs):
        device = args[0]
        if device.status:
            status = 'on'
        else:
            status = 'off'
        print(f'Action: {func.__name__}, Device: {device.name}, Status: {status}')
        return func(*args, **kwargs)
    return wrapper


class Device:

    def __init__(self, device_id, name, status=False):
        self.device_id = device_id
        self.name = name
        self.status = status

    @actoins_print
    def turn_on(self):
        self.status = True

    @actoins_print
    def turn_off(self):
        self.status = False

    def get_status(self):
        if self.status:
            return 'on'
        else:
            return 'off'


class Light(Device):

    def __init__(self, device_id, name, brightness, color, status=False):
        super().__init__(device_id, name, status)
        self.brightness = brightness
        self.color = color


class Thermostat(Device):

    def __init__(self, device_id, name, current_temperature, target_temperature, status=False):
        super().__init__(device_id, name, status)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature


