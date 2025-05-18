from vex import *
from enum import Enum, auto


class State(Enum):
    MANUAL = auto()
    SEARCH = auto()
    APPROACH = auto()
    FLIP = auto()
    AVOID_BOUNDARY = auto()


GREEN_HUE_MIN = 100
GREEN_HUE_MAX = 160
APPROACH_DISTANCE_MM = 400
FLIP_DISTANCE_MM = 150


def _manual_drive(controller, left_drive, right_drive, arm_drive):
    """Drive robot manually using the controller."""
    left_speed = controller.axis3.position() + controller.axis1.position()
    right_speed = controller.axis3.position() - controller.axis1.position()

    if abs(left_speed) < 5:
        left_drive.stop()
    else:
        left_drive.set_velocity(left_speed, PERCENT)
        left_drive.spin(FORWARD)

    if abs(right_speed) < 5:
        right_drive.stop()
    else:
        right_drive.set_velocity(right_speed, PERCENT)
        right_drive.spin(FORWARD)

    if arm_drive is not None:
        if controller.buttonR1.pressing():
            arm_drive.spin(FORWARD)
        elif controller.buttonR2.pressing():
            arm_drive.spin(REVERSE)
        else:
            arm_drive.stop()


# pylint: disable=too-many-arguments

def run_state_machine(
    brain: Brain,
    controller: Controller,
    drive_train: DriveTrain,
    left_drive: MotorGroup,
    right_drive: MotorGroup,
    arm_drive: MotorGroup | None = None,
    distance_sensor: Distance | None = None,
    optical_sensor: Optical | None = None,
) -> None:
    """Run a simple state machine handling manual and automated control."""
    state = State.MANUAL

    if optical_sensor is not None:
        optical_sensor.set_light_power(100, PERCENT)
        optical_sensor.set_light(True)

    while True:
        if state == State.MANUAL:
            _manual_drive(controller, left_drive, right_drive, arm_drive)
            if controller.buttonB.pressing():
                while controller.buttonB.pressing():
                    wait(10, MSEC)
                drive_train.stop()
                state = State.SEARCH
            wait(20, MSEC)
            continue

        # Automated mode can be exited with button A
        if controller.buttonA.pressing():
            while controller.buttonA.pressing():
                wait(10, MSEC)
            drive_train.stop()
            state = State.MANUAL
            continue

        # Boundary detection using optical sensor
        if optical_sensor is not None:
            hue = optical_sensor.hue()
            if GREEN_HUE_MIN <= hue <= GREEN_HUE_MAX:
                drive_train.stop()
                drive_train.set_drive_velocity(50, PERCENT)
                drive_train.drive_for(REVERSE, 6, INCHES)
                drive_train.turn_for(RIGHT, 180, DEGREES)
                state = State.SEARCH
                continue

        if state == State.SEARCH:
            drive_train.set_turn_velocity(20, PERCENT)
            drive_train.turn(RIGHT)
            if distance_sensor is not None and distance_sensor.is_object_detected():
                drive_train.stop()
                state = State.APPROACH
        elif state == State.APPROACH:
            if distance_sensor is None:
                state = State.SEARCH
            else:
                dist = distance_sensor.object_distance(MM)
                if dist < FLIP_DISTANCE_MM:
                    drive_train.stop()
                    state = State.FLIP
                else:
                    drive_train.set_drive_velocity(50, PERCENT)
                    drive_train.drive(FORWARD)
        elif state == State.FLIP:
            if arm_drive is not None:
                arm_drive.spin_for(FORWARD, 360, DEGREES)
            wait(500, MSEC)
            state = State.SEARCH

        wait(20, MSEC)
