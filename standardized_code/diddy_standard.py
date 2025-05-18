from vex import *

brain = Brain()
controller = Controller(PRIMARY)

# Drive motors
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

drive_train = DriveTrain(left_drive, right_drive, 319.19, 295, 40, MM, 1)

# Sensors
distance_sensor = Distance(Ports.PORT11)
optical_sensor = Optical(Ports.PORT19)
optical_sensor.set_light_power(100)
optical_sensor.set_light(True)

