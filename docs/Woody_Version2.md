# Version 2 Setup – Woody Team

The Woody robot features bumpers, a sonar sensor, and an arm on ports 11 and 12. This guide explains the minimal edits required to run `version2.py`.

## Motor Configuration

```python
left_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
right_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
```

Note the left motors are on ports 9 and 10. Adjust these if your wiring changes.

## Arm Motors

```python
arm_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
arm_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)
```

## Sensors

```python
front_bumper = Bumper(brain.three_wire_port.g)
rear_bumper = Bumper(brain.three_wire_port.h)
sonar_sensor = Sonar(brain.three_wire_port.a)
front_distance = Distance(Ports.PORT14)
optical_sensor = Optical(Ports.PORT3)
```

`version2.py` does not use bumpers or sonar directly. You can remove those lines or keep them for future expansion. Ensure the `front_distance` and `optical_sensor` lines are present so the autonomous modes work.

## Turning Considerations

Woody’s drive train uses the same measurements as the other teams, so the default wheel diameter and track width should allow accurate turns. If the robot veers when driving, check that one side’s motors are not reversed incorrectly.

## Testing Checklist

1. Update ports as shown above.
2. Confirm manual driving with the controller.
3. Test the arm’s direction using the `R1` and `R2` buttons.
4. Press **B** to begin scanning and verify that the robot turns smoothly.
5. Place a target in front to trigger the attack sequence.

With these edits, the Woody robot should function correctly with `version2.py`.
