# Version 2 Setup – Team 4

Team 4’s robot uses four distance sensors and an arm on ports 6 and 7. This page describes how to wire those into `version2.py`.

## Motor Ports

```python
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
```

These match `team4_standard.py`. Adjust the reversal flags only if the robot moves the opposite direction when driving manually.

## Arm Motors

```python
arm_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
arm_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)
```

## Distance Sensors

Team 4 employs sensors facing all sides:

- Front: `Distance(Ports.PORT9)`
- Rear: `Distance(Ports.PORT8)`
- Left: `Distance(Ports.PORT10)`
- Right: `Distance(Ports.PORT20)`

`version2.py` only expects one distance sensor. Choose the most important one (usually the front sensor) and set `distance_sensor` accordingly. You can extend the code to check multiple sensors if desired.

## Turning and Movement

The original Team 4 code spins continuously using threads. For `version2.py` we rely on the built‑in `DriveTrain.turn` method. Ensure your wheel diameter and track width are accurate so 90‑degree turns complete properly.

If the robot tends to drift or under‑turn, you can slow down the scan:

```python
drive_train.set_turn_velocity(20, PERCENT)
```

or add a brief wait after turning.

## Testing Checklist

1. Edit the port numbers above and deploy the script.
2. Confirm manual control of driving and the arm.
3. Press **B** to scan and watch for smooth rotation.
4. Place an object in front of the selected distance sensor to see the approach behavior.
5. Tune velocities and wait times to achieve consistent movement.
