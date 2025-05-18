PRIMARY = 0
class Axis:
    def __init__(self, value=0):
        self.value = value
    def position(self):
        return self.value

class Button:
    def __init__(self, sequence=None):
        self.sequence = list(sequence or [False])
    def pressing(self):
        return self.sequence.pop(0) if self.sequence else False

class Screen:
    def clear_screen(self):
        pass
    def set_cursor(self, row, col):
        pass
    def print(self, msg):
        pass

class Brain:
    def __init__(self):
        self.screen = Screen()
        from types import SimpleNamespace
        self.three_wire_port = SimpleNamespace(a="a", b="b", c="c", d="d", e="e", f="f", g="g", h="h")

class Controller:
    PRIMARY = 0
    def __init__(self, _=None):
        self.axis1 = Axis()
        self.axis3 = Axis()
        self.buttonA = Button()
        self.buttonB = Button()
        self.buttonR1 = Button()
        self.buttonR2 = Button()

class Motor:
    def __init__(self, port, gear_setting=None, reversed=False):
        self.port = port

class MotorGroup:
    def __init__(self, *motors):
        self.motors = motors
    def set_velocity(self, value, unit):
        pass
    def spin(self, direction):
        pass
    def stop(self):
        pass
    def spin_for(self, direction, value, unit):
        pass

class DriveTrain:
    def __init__(self, left_drive, right_drive, wheel_travel, track_width, wheel_base, unit, external_ratio):
        self.left_drive = left_drive
        self.right_drive = right_drive
    def set_turn_velocity(self, value, unit):
        pass
    def turn(self, direction):
        pass
    def stop(self):
        pass
    def set_drive_velocity(self, value, unit):
        pass
    def drive_for(self, direction, distance, units):
        pass
    def turn_for(self, direction, angle, units):
        pass
    def drive(self, direction):
        pass

class Distance:
    def __init__(self, port):
        self.port = port
        self.detected = False
        self.distance_value = 1000
    def is_object_detected(self):
        return self.detected
    def object_distance(self, unit):
        return self.distance_value

class Optical:
    def __init__(self, port):
        self.port = port
        self.hue_value = 0
    def set_light_power(self, power, unit=None):
        pass
    def set_light(self, on):
        pass
    def hue(self):
        return self.hue_value

class Bumper:
    def __init__(self, port):
        self.port = port

class Sonar:
    def __init__(self, port):
        self.port = port

class GearSetting:
    RATIO_18_1 = 0
    RATIO_36_1 = 1

class Ports:
    PORT1 = 1
    PORT2 = 2
    PORT3 = 3
    PORT4 = 4
    PORT5 = 5
    PORT6 = 6
    PORT7 = 7
    PORT8 = 8
    PORT9 = 9
    PORT10 = 10
    PORT11 = 11
    PORT12 = 12
    PORT13 = 13
    PORT14 = 14
    PORT15 = 15
    PORT16 = 16
    PORT17 = 17
    PORT18 = 18
    PORT19 = 19
    PORT20 = 20

# Direction and unit constants
FORWARD = 1
REVERSE = 2
RIGHT = 3
LEFT = 4
DEGREES = 5
INCHES = 6
MM = 7
MSEC = 8
PERCENT = 9
COAST = 10

wait_counter = 0
wait_max = None

def wait(_time, _units):
    global wait_counter, wait_max
    wait_counter += 1
    if wait_max is not None and wait_counter >= wait_max:
        raise StopIteration
