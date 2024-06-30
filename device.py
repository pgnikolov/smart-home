def check_status_before_action(func):
    def wrapper(*args, **kwargs):
        device = args[0]
        action = func.__name__
        if isinstance(device, DoorLock):
            current_status = device.status
            if action == 'turn_on' and current_status:
                return f'{device.name} is already unlocked.'
            if action == 'turn_off' and not current_status:
                return f'{device.name} is already locked.'
        else:
            current_status = device.status
            if action == 'turn_on' and current_status:
                return f'{device.name} is already on.'
            if action == 'turn_off' and not current_status:
                return f'{device.name} is already off.'
        return func(*args, **kwargs)
    return wrapper


class Device:

    def __init__(self, device_id, name, status=False):
        self.device_id = device_id
        self.name = name
        self.status = status

    @check_status_before_action
    def turn_on(self):
        self.status = True

    @check_status_before_action
    def turn_off(self):
        self.status = False

    def get_status(self):
        if self.status:
            return 'on'
        else:
            return 'off'


class Light(Device):

    def __init__(self, device_id, name, brightness, status=False):
        super().__init__(device_id, name, status)
        self.brightness = brightness
        self.color = None


class Thermostat(Device):

    def __init__(self, device_id, name, current_temp, status=False):
        super().__init__(device_id, name, status)
        self.current_temp = current_temp
        self.target_temp = None


class DoorLock(Device):

    def __init__(self, device_id, name, status=False):
        super().__init__(device_id, name, status)

    def get_status(self):
        if self.status:
            return "unlocked"
        else:
            return "locked"


