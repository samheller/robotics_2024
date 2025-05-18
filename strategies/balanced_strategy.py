from vex import *
from enum import Enum, auto


brain = Brain()
controller = Controller(PRIMARY)

# Drive motors (Team 4 configuration)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

drive_train = DriveTrain(left_drive, right_drive, 319.19, 295, 40, MM, 1)

# Arm motors (Team 4 configuration)
arm_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
arm_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)

# Distance sensors (Team 4 configuration)
front_distance = Distance(Ports.PORT9)
rear_distance = Distance(Ports.PORT8)
left_distance = Distance(Ports.PORT10)
right_distance = Distance(Ports.PORT20)

# Use front sensor by default for state machine logic
distance_sensor = front_distance

# Team 4 robot does not have an optical sensor
optical_sensor: Optical | None = None

class RobotState(Enum):
    MANUAL = auto()
    SCANNING = auto()
    TARGET_FOUND = auto()
    ATTACKING = auto()

current_state = RobotState.MANUAL

# ------------------------------------------------------------
# State handlers

def handle_manual():
    global current_state

    # Controller sticks drive the motors
    left_speed = controller.axis3.position() + controller.axis1.position()
    right_speed = controller.axis3.position() - controller.axis1.position()

    left_drive.set_velocity(left_speed, PERCENT)
    right_drive.set_velocity(right_speed, PERCENT)

    left_drive.spin(FORWARD if left_speed != 0 else COAST)
    right_drive.spin(FORWARD if right_speed != 0 else COAST)

    # Arm control
    if controller.buttonR1.pressing():
        arm_drive.spin(FORWARD)
    elif controller.buttonR2.pressing():
        arm_drive.spin(REVERSE)
    else:
        arm_drive.stop()

    # Transition: user presses B to start scanning
    if controller.buttonB.pressing():
        current_state = RobotState.SCANNING


def handle_scanning():
    global current_state

    # Medium speed scan for a mix of offense and defense
    drive_train.set_turn_velocity(35, PERCENT)
    drive_train.turn(RIGHT)

    # Transition to TARGET_FOUND if distance sensor spots something
    if distance_sensor.object_size() in [ObjectSizeType.MEDIUM, ObjectSizeType.LARGE]:
        drive_train.stop()
        current_state = RobotState.TARGET_FOUND

    # User can cancel scanning with button A
    if controller.buttonA.pressing():
        drive_train.stop()
        current_state = RobotState.MANUAL


def handle_target_found():
    global current_state

    # Steady approach for reliable positioning
    drive_train.set_drive_velocity(40, PERCENT)
    drive_train.drive_for(FORWARD, 6, INCHES)

    # If the target is close enough, begin attacking
    if distance_sensor.object_distance(MM) < 300:
        drive_train.stop()
        current_state = RobotState.ATTACKING
        return

    # If the target disappears, resume scanning
    if distance_sensor.object_size() == ObjectSizeType.NONE:
        drive_train.stop()
        current_state = RobotState.SCANNING


def handle_attacking():
    global current_state

    arm_drive.set_velocity(45, PERCENT)

    # Example attack sequence
    arm_drive.spin(REVERSE)
    wait(1, SECONDS)
    arm_drive.stop()
    arm_drive.spin(FORWARD)
    wait(1, SECONDS)
    arm_drive.stop()

    # After attack, back up and return to manual control
    drive_train.drive_for(REVERSE, 18, INCHES)
    current_state = RobotState.MANUAL

# ------------------------------------------------------------
# Map states to handlers
state_handlers = {
    RobotState.MANUAL: handle_manual,
    RobotState.SCANNING: handle_scanning,
    RobotState.TARGET_FOUND: handle_target_found,
    RobotState.ATTACKING: handle_attacking,
}

# ------------------------------------------------------------
# Utility to show status on the Brain screen

def display_status():
    """Display current state, hue, and distance."""
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("State: " + current_state.name)

    if optical_sensor is not None:
        hue = optical_sensor.hue()
        brain.screen.set_cursor(2, 1)
        brain.screen.print("Hue: " + str(hue))

    distance_mm = distance_sensor.object_distance(MM)
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Dist: " + str(distance_mm))

# ------------------------------------------------------------
# Main control loop
while True:
    state_handlers[current_state]()
    display_status()
    wait(20, MSEC)
