# Version 2 Setup – Diddy Team

Follow these notes to adapt `state_machine/version2.py` for the Diddy robot.

## Motors and Drive Train

```python
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
```

All motors are reversed (`True`) because of the wiring orientation on this robot. Keep the wheel diameter and track width from `version2.py` unless your robot measurements are different.

## Sensors

```python
distance_sensor = Distance(Ports.PORT11)
optical_sensor = Optical(Ports.PORT19)
optical_sensor.set_light_power(100)
optical_sensor.set_light(True)
```

The optical sensor is configured with its light enabled. Include the two `set_light` lines in your setup code if you rely on color detection.

## Movement Style

The Diddy team typically drives the left and right motor groups directly instead of using the `DriveTrain` helper. However, `version2.py` uses `DriveTrain`. If you notice inconsistent turning, check the boolean reversal flags or replace the `drive_train.turn` calls with explicit motor commands.

Example replacement for scanning:

```python
drive_train.set_turn_velocity(20, PERCENT)
left_drive.spin(FORWARD, 20, PERCENT)
right_drive.spin(REVERSE, 20, PERCENT)
```

Using direct `MotorGroup` commands may better match Diddy’s existing code.

## Testing Checklist

1. Update port numbers and verify manual driving works.
2. Test scanning with the robot on blocks so the wheels can spin freely.
3. Ensure the optical sensor’s light turns on.
4. Approach a target and confirm the distance sensor triggers the attack sequence.

Make small adjustments to the velocities if the robot turns too slowly or overshoots.
