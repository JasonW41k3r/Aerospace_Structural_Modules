from pymycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord
from pymycobot import PI_PORT, PI_BAUD
import time
mc = MyCobot(PI_PORT, PI_BAUD)
mc.send_coords([272.9, 100.3, 150.1, -178.43, -0.29, -84.9], 80, 1)
time.sleep(1)
mc.set_gripper_value(20,80)
time.sleep(1)
mc.send_coords([272.9, -100.3, 150.1, -178.43, -0.29, -84.9], 80, 1)
time.sleep(1)
mc.set_gripper_value(250,80)
time.sleep(1)
