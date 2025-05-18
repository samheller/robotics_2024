#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
distance_11 = Distance(Ports.PORT11)
optical_19 = Optical(Ports.PORT19)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
motor_group_1_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_36_1, True)
motor_group_1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_36_1, False)
motor_group_1 = MotorGroup(motor_group_1_motor_a, motor_group_1_motor_b)
motor_group_3_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motor_group_3_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
motor_group_3 = MotorGroup(motor_group_3_motor_a, motor_group_3_motor_b)
distance_11 = Distance(Ports.PORT11)

# New optical sensor
optical_sensor = Optical(Ports.PORT19)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))

# Set random seed 
initializeRandomSeed()

def play_vexcode_sound(sound_name):
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)
print("\033[2J")
#endregion

# Motor configuration
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
left_drive = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_drive = MotorGroup(right_motor_a, right_motor_b)

# Distance sensor on port 11
distance_sensor = Distance(Ports.PORT11)

# Optical sensor on port 19
optical_sensor = Optical(Ports.PORT19)
optical_sensor.set_light_power(100)
optical_sensor.set_light(True)  # Turn on LED for color detection

wait(300, MSEC)
print("\033[2J")

def turn_around():
    left_drive.spin(FORWARD, 50, PERCENT)
    right_drive.spin(REVERSE, 50, PERCENT)
    wait(1.5, SECONDS)
    left_drive.stop()
    right_drive.stop()
    brain.screen.set_cursor(5, 1)
    brain.screen.print("Green detected! Turning around...")

def when_started():
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Scanning...")

        # Spin in place
        left_drive.spin(FORWARD, 20, PERCENT)
        right_drive.spin(FORWARD, 20, PERCENT)
        wait(1, SECONDS)

        # Stop spinning to check sensors
        left_drive.stop()
        right_drive.stop()
        wait(0.1, SECONDS)

        # Check for Blue
        hue = optical_sensor.hue()
        if 100 <= hue <= 160:
            turn_around()
            continue

        # Check distance
        distance_mm = distance_sensor.object_distance(DistanceUnits.MM)
        brain.screen.set_cursor(2, 1)
        brain.screen.print("Distance: " + str(distance_mm))

        # Display detected color based on hue
        brain.screen.set_cursor(6, 1)
        if 200 <= hue <= 250:
            brain.screen.print("Color: Blue")
        elif 100 <= hue <= 160:
            brain.screen.print("Color: Green")
        elif 0 <= hue <= 30 or hue >= 330:
            brain.screen.print("Color: Red")
        else:
            brain.screen.print("Color: Unknown")

        if 0 < distance_mm < 400:
            brain.screen.set_cursor(3, 1)
            brain.screen.print("Target detected!")

            # Charge
            left_drive.spin(REVERSE, 70, PERCENT)
            right_drive.spin(FORWARD, 70, PERCENT)
            for _ in range(25):  # 2.5 seconds with check every 0.1s
                if 100 <= optical_sensor.hue() <= 160:
                    left_drive.stop()
                    right_drive.stop()
                    turn_around()
                    break
                wait(0.1, SECONDS)

            # Small reverse
            left_drive.spin(FORWARD, 50, PERCENT)
            right_drive.spin(REVERSE, 50, PERCENT)
            wait(1, SECONDS)

            # Final charge
            left_drive.spin(REVERSE, 100, PERCENT)
            right_drive.spin(FORWARD, 100, PERCENT)
            for _ in range(25):  # 2.5 seconds
                if 100 <= optical_sensor.hue() <= 160:
                    left_drive.stop()
                    right_drive.stop()
                    turn_around()
                    break
                wait(0.1, SECONDS)

            # Stop all
            left_drive.stop(BRAKE)
            right_drive.stop(BRAKE)
            brain.screen.set_cursor(4, 1)
            brain.screen.print("Attack complete.")
            wait(1, SECONDS)
        else:
            brain.screen.set_cursor(3, 1)
            brain.screen.print("No target. Keep scanning.")

        wait(0.3, SECONDS)

# Start the program
when_started()
