# State Machine Examples

This folder contains multiple versions of a VEX V5 state machine implementation. The `version3.py` script demonstrates a merged manual and autonomous control scheme. Below is an overview of how that file operates.

## Overview of `version3.py`

The script defines a state machine with four states:

1. **MANUAL** – default mode where the driver directly controls the robot.
2. **SCANNING** – the robot slowly turns while searching for an object using sensors.
3. **TARGET_FOUND** – the robot approaches a detected object until it is within a set distance.
4. **ATTACKING** – once close enough, the robot performs an action (such as moving an arm) and then retreats to manual control.

Sensors and motors are passed in to the `run_state_machine` function so the same code can run on different hardware setups. The optical sensor (if provided) is also configured to act as a boundary detector.

### Key Behaviors by State

- **Manual**
  - Uses controller joysticks to drive left and right motor groups.
  - Buttons can control an optional arm mechanism.
  - Pressing button B switches to the scanning state.

- **Scanning**
  - Robot slowly rotates to look for objects using the distance sensor.
  - If the optical sensor detects a green boundary (based on hue), the robot backs up and turns around.
  - Detection of an object transitions to `TARGET_FOUND`. Pressing button A cancels back to manual mode.

- **Target Found**
  - Robot drives forward toward the object.
  - Reaching the target distance triggers the attacking state.
  - Losing sight of the object returns to scanning.

- **Attacking**
  - Optionally moves the arm to flip or interact with the target.
  - Drives backward a set distance and then goes back to manual mode.

### Display Feedback

A helper function updates the brain's screen with the current state, sensor hue, and object distance each loop iteration.

### Main Loop

A dictionary maps each state to its handler function. The loop repeatedly executes the current state's function, displays status, and waits briefly before the next iteration.

The combination of manual controls with autonomous behaviors allows the robot to search for, approach, and interact with targets while giving the driver an easy way to retake control.

