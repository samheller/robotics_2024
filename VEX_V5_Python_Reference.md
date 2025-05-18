# VEX V5 Python Function Reference

This document summarizes commonly used functions in the VEX V5 Python API and includes examples based on the code in the `initial_code` folder.

> **Note**: The VEX library contains many more functions than shown here. For a full reference see the official VEX documentation: <https://api.vexcode.cloud/python/>.

## Imports and Setup

```python
from vex import *
brain = Brain()
```

The `vex` module provides classes for motors, sensors, controllers and more.

## Motors and Motor Groups

Create single motors or groups of motors and control them with methods such as `spin`, `stop`, or `set_velocity`.

```python
motor = Motor(Ports.PORT1)
other_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
motors = MotorGroup(motor, other_motor)

motor.spin(FORWARD)
wait(1, SECONDS)
motor.stop()

motors.set_velocity(50, PERCENT)
motors.spin(FORWARD)
```

### Setting Torque and Spinning for a Distance

```python
motors.set_max_torque(100, PERCENT)
motors.spin_for(FORWARD, 180, DEGREES)
```

## Drivetrain

Use a `DriveTrain` to control differential-drive robots.

```python
left_motor = Motor(Ports.PORT1)
right_motor = Motor(Ports.PORT2, True)
drivetrain = DriveTrain(left_motor, right_motor, 319.19, 295, 40, MM)

drivetrain.set_drive_velocity(100, PERCENT)
drivetrain.set_turn_velocity(20, PERCENT)
drivetrain.drive_for(FORWARD, 24, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)
```

## Sensors

### Distance

```python
distance = Distance(Ports.PORT11)
if distance.is_object_detected():
    dist_mm = distance.object_distance(MM)
```

### Optical

```python
optical = Optical(Ports.PORT19)
optical.set_light_power(100, PERCENT)
optical.set_light(True)
color = optical.color()
hue = optical.hue()
```

### Bumper and Sonar

```python
bumper = Bumper(brain.three_wire_port.h)
bumper.pressed(lambda: brain.screen.print("Pressed"))

sonar = Sonar(brain.three_wire_port.a)
range_mm = sonar.distance(MM)
```

## Controller

Access axes and buttons from the gamepad-style controller.

```python
controller = Controller(PRIMARY)
left_speed = controller.axis3.position() + controller.axis1.position()
if controller.buttonR1.pressing():
    motors.spin(FORWARD)
```

Buttons support callbacks:

```python
def handle_down():
    brain.program_stop()

controller.buttonDown.pressed(handle_down)
```

## Brain Screen and Battery

```python
brain.screen.set_cursor(1, 1)
brain.screen.print("Hello")
brain.screen.clear_screen()
brain.screen.draw_rectangle(0, 0, 479, 239)

voltage_mv = brain.battery.voltage(MV)
current_a = brain.battery.current(CurrentUnits.AMP)
```

High resolution timer:

```python
time = brain.timer.system_high_res()
```

## Events and Threads

Use `Event` for callbacks and `Thread` for concurrent loops.

```python
my_event = Event()

def handler():
    brain.screen.print("Triggered")

my_event(handler)

thread = Thread(handler)
```

## Wait Function

Delay program execution:

```python
wait(1.5, SECONDS)
```

## Example Program

A minimal example combining several features:

```python
from vex import *

brain = Brain()
left = Motor(Ports.PORT1)
right = Motor(Ports.PORT2, True)
drivetrain = DriveTrain(left, right, 319.19, 295, 40, MM)
sensor = Optical(Ports.PORT3)

sensor.set_light_power(100, PERCENT)
sensor.set_light(True)

brain.screen.print("Starting")
wait(0.3, SECONDS)

while True:
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.drive(FORWARD)
    if sensor.hue() > 200:
        drivetrain.stop()
        break
    wait(20, MSEC)
```

---
For additional details, please consult the full API guide linked above.
