from vex import *

brain = Brain()
controller = Controller(PRIMARY)

# Drive motors
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

drive_train = DriveTrain(left_drive, right_drive, 319.19, 295, 40, MM, 1)

# Arm motors
arm_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
arm_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)

# Distance sensors
front_distance = Distance(Ports.PORT9)
rear_distance = Distance(Ports.PORT8)
left_distance = Distance(Ports.PORT10)
right_distance = Distance(Ports.PORT20)

