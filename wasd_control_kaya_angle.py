import readchar
from kaya_angle_control import KayaAngleController
from kaya_motor_control import KayaMotorController

try:
    angle_control = KayaAngleController()
    control = KayaMotorController()
    angle = 0
    left = 0
    right = 0
    while 1:
        angle = 0
        left = 0
        right = 0
        power = 100
        kb = readchar.readchar()
        if kb == 'p':
            print("EXIT")
            break
        elif kb == 'w':
            print('W')
            angle = 0
            left = 0
            right = 0
        elif kb == 'a':
            print("A")
            #angle = -90
            left = 50
            right = -100
        elif kb == 's':
            print("S")
            #angle = 180
            left = -100
            right = 100
        elif kb == 'd':
            print("D")
            #angle = 90
            left = 100
            right = -50
        elif kb == 'q':
            print("Q")
            angle = -90
            """
            left = -100
            center = -100
            right = -100
            """
        elif kb == 'e':
            print("E")
            angle = 90
            """
            left = 100
            center = 100
            right = 100
            """
        elif kb == 'z':
            print('z')
            angle = -135

        elif kb == "c":
            print('c')
            angle = 135
        else:
            print("Stop")
            angle = 0
            power = 0

        angle_control.angle(left, right, angle, power)
finally:
    control.clean()
