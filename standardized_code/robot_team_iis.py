from vex import *

brain = Brain()
controller = Controller(PRIMARY)

# Drive motors
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

drive_train = DriveTrain(left_drive, right_drive, 319.19, 295, 40, MM, 1)

# Arm motors
arm_motor_a = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
arm_motor_b = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)

# Sensors
distance_sensor = Distance(Ports.PORT20)
optical_sensor = Optical(Ports.PORT9)

