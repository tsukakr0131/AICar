import math
from kaya_motor_control import KayaMotorController

control = KayaMotorController()

class KayaAngleController():
    def angle(self, left, right, angle, power = 100):
        #center
        if left != 0 or right != 0:
            center = 0
        elif angle == 0:
            left = power
            center = 0
            right =  -1 * power
        #center
        elif angle == 180 or angle == -180:
            left = -1 * power
            center = 0
            right = power

        #left or right
        else:
            left = -1 * int(math.sin(math.radians(angle - 120)) * power)
            center = int(math.sin(math.radians(angle - 180)) *power)
            right = -1 * int(math.sin(math.radians(angle + 120)) * power)
            
            if 0 < left < 80:
                left = left + 20
            elif -80 < left < 0:
                left = left -20
            if 0 < right < 80:
                right = right + 20
            elif -80 < right < 0:
                right = right -20
            
       
        print(left, center, right, power)
        control.left(left)
        control.center(center)
        control.right(right)
