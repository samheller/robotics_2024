# Version 2 State Machine Guide

This guide explains how to modify `state_machine/version2.py` so it can run on different robots. Each team has its own hardware layout and movement strategy, so we provide general editing steps followed by team‑specific notes.

The goal is to keep `version2.py` mostly unchanged while adjusting the motor groups, drivetrain, and any sensor interactions so the script matches your robot. The file uses a simple state machine with four states:

1. **MANUAL** – driver control
2. **SCANNING** – slowly turning to find a target
3. **TARGET_FOUND** – approaching the detected target
4. **ATTACKING** – flipping or interacting with the target

## General Editing Steps

1. **Review Motor Ports**
   - At the top of the file motors are created with specific port numbers.
   - Update these port numbers to match your robot.
   - Example:
     ```python
     left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
     ```
     Change `PORT1` to whichever port your left motor uses.

2. **Check Motor Inversion**
   - The third argument to `Motor` decides whether the motor is reversed.
   - If your robot turns the wrong way, flip the boolean value.

3. **Adjust the `DriveTrain` Parameters**
   - `DriveTrain` takes wheel diameter, track width, and wheelbase. These numbers affect turning.
   - Measure your robot and update the `DriveTrain` call accordingly.

4. **Tuning Drive Velocities**
   - The handlers call `set_drive_velocity` and `set_turn_velocity` in percentages.
   - Increase or decrease these values based on how fast you want the robot to move in each state.

5. **Sensor Ports**
   - `version2.py` expects a distance sensor on port 20 and an optical sensor on port 9.
   - If your sensors are different, update the `Distance` or `Optical` constructor calls.

6. **Testing Manual Control**
   - Run the script on your robot and verify that the joysticks move the wheels correctly.
   - Ensure the arm buttons spin the arm motors in the correct directions.

7. **Testing the Autonomous States**
   - Press the `B` button to enter the scanning mode.
   - Wave an object in front of the distance sensor to trigger `TARGET_FOUND`.
   - Observe the attack sequence and tweak distances or wait times as needed.

## Team‑Specific Notes

The rest of this guide links to dedicated pages for each team. Each page walks through the exact edits needed to match that team’s robot layout and movement style.

- [Robot Team IIS](Team_IIS_Version2.md)
- [Diddy](Diddy_Version2.md)
- [Team 4](Team4_Version2.md)
- [Woody](Woody_Version2.md)

Read your team’s page after completing the general steps above.
