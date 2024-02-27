# --------------------------------------------------------------------------------- #
#                                                                                   #
#    Project:          Base Robot With Sensors                                      #
#    Module:           main.py                                                      #
#    Author:           VEX    (lines 19-49)                                                      #
#    Created:          Fri Aug 05 2022                                              #
#    Description:      Base IQ Gen 2 robot with controls and with sensors           #
#                                                                                   #
#    Configuration:    BaseBot with Sensors (Drivetrain 2-motor, Inertial)          #
#                      Left Motor in Port 1                                         #
#                      Right Motor in Port 6                                        #
#                      TouchLED in Port 2                                           #
#                      Optical Sensor in Port 3                                     #
#                      Distance Sensor in Port 7                                    #
#                      Bumper in Port 9   
#
#   Modification:      Sharon Harrison, February 2024                               #
#                                                                                   #
# --------------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1, True)
right_drive_smart = Motor(Ports.PORT6, 1, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
touchled_2 = Touchled(Ports.PORT2)
optical_3 = Optical(Ports.PORT3)
distance_7 = Distance(Ports.PORT7)
bumper_9 = Bumper(Ports.PORT9)


def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Begin project code
