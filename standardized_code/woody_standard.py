from vex import *

brain = Brain()
controller = Controller(PRIMARY)

# Drive motors
left_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

drive_train = DriveTrain(left_drive, right_drive, 319.19, 295, 40, MM, 1)

# Arm motors
arm_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
arm_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
arm_drive = MotorGroup(arm_motor_a, arm_motor_b)

# Sensors
front_bumper = Bumper(brain.three_wire_port.g)
rear_bumper = Bumper(brain.three_wire_port.h)
sonar_sensor = Sonar(brain.three_wire_port.a)
front_distance = Distance(Ports.PORT14)
optical_sensor = Optical(Ports.PORT3)

