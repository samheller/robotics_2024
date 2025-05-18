# Version 2 Setup – Robot Team IIS

This page lists concrete edits for the IIS robot configuration. Use it alongside [Version2_User_Guide.md](Version2_User_Guide.md).

## Motors and Drive Train

```python
# Drive motors
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

# DriveTrain uses 319.19 mm wheel size and 295 mm track width
```

If your physical robot differs, change the port numbers or reverse flags. The default values match the IIS robot as of `robot_team_iis.py`.

## Arm Motors

```python
arm_motor_a = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
arm_motor_b = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)
```

## Sensors

```python
distance_sensor = Distance(Ports.PORT20)
optical_sensor = Optical(Ports.PORT9)
```

These are the same ports used in the team’s existing programs. Make sure the cables are connected accordingly.

## Turning and Movement

The IIS robot relies on standard `DriveTrain` turns (`turn_for` and `turn`) using the wheelbase numbers above. When port values and track width match the hardware, `version2.py` should spin in place correctly. You may fine‑tune the turning speed in `handle_scanning()` by adjusting:

```python
drive_train.set_turn_velocity(50, PERCENT)
```

Reduce the percentage if the robot turns too quickly.

## Testing Checklist

1. Upload `version2.py` after editing ports.
2. Drive manually with the controller to confirm the wheels and arm respond.
3. Press **B** to start scanning and confirm the robot slowly rotates.
4. Place an object in front of the distance sensor to trigger the attack sequence.
5. Verify the arm movement is strong enough to flip the object.

Once these steps pass, the IIS robot is ready to use the version 2 state machine.
