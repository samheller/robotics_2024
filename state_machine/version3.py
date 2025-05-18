from vex import *
from enum import Enum, auto


class State(Enum):
    MANUAL = auto()
    SCANNING = auto()
    TARGET_FOUND = auto()
    ATTACKING = auto()


GREEN_HUE_MIN = 100
GREEN_HUE_MAX = 160
TARGET_DISTANCE_MM = 300


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
    """Run the merged state machine with manual and autonomous modes."""

    state = State.MANUAL

    if optical_sensor is not None:
        optical_sensor.set_light_power(100, PERCENT)
        optical_sensor.set_light(True)

    def display_status() -> None:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("State: " + state.name)
        if optical_sensor is not None:
            brain.screen.set_cursor(2, 1)
            brain.screen.print("Hue: " + str(optical_sensor.hue()))
        if distance_sensor is not None:
            brain.screen.set_cursor(3, 1)
            brain.screen.print("Dist: " + str(distance_sensor.object_distance(MM)))

    def manual() -> None:
        nonlocal state
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

        if controller.buttonB.pressing():
            while controller.buttonB.pressing():
                wait(10, MSEC)
            drive_train.stop()
            state = State.SCANNING

    def scanning() -> None:
        nonlocal state
        drive_train.set_turn_velocity(20, PERCENT)
        drive_train.turn(RIGHT)

        if optical_sensor is not None:
            hue = optical_sensor.hue()
            if GREEN_HUE_MIN <= hue <= GREEN_HUE_MAX:
                drive_train.stop()
                drive_train.set_drive_velocity(50, PERCENT)
                drive_train.drive_for(REVERSE, 6, INCHES)
                drive_train.turn_for(RIGHT, 180, DEGREES)
                return

        if distance_sensor is not None and distance_sensor.is_object_detected():
            drive_train.stop()
            state = State.TARGET_FOUND

        if controller.buttonA.pressing():
            drive_train.stop()
            state = State.MANUAL

    def target_found() -> None:
        nonlocal state
        if distance_sensor is None:
            state = State.SCANNING
            return

        drive_train.set_drive_velocity(30, PERCENT)
        drive_train.drive(FORWARD)

        if distance_sensor.object_distance(MM) < TARGET_DISTANCE_MM:
            drive_train.stop()
            state = State.ATTACKING
        elif not distance_sensor.is_object_detected():
            drive_train.stop()
            state = State.SCANNING

    def attacking() -> None:
        nonlocal state
        if arm_drive is not None:
            arm_drive.set_velocity(50, PERCENT)
            arm_drive.spin_for(REVERSE, 180, DEGREES)
            arm_drive.spin_for(FORWARD, 180, DEGREES)
        drive_train.drive_for(REVERSE, 20, INCHES)
        state = State.MANUAL

    handlers = {
        State.MANUAL: manual,
        State.SCANNING: scanning,
        State.TARGET_FOUND: target_found,
        State.ATTACKING: attacking,
    }

    while True:
        handlers[state]()
        display_status()
        wait(20, MSEC)
