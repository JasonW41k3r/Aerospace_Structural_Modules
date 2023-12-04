from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time
mc = MyCobot(PI_PORT, PI_BAUD)
coords = mc.get_coords()
print(coords)
mc.send_coords([-247.7, 5.8, 96.2, -76.46, -67.62, 140.84], 40, 1)
time.sleep(3)
mc.set_gripper_value(170,40)
time.sleep(3)
mc.send_coords([124.0, -177.3, 208.8, -102.62, -58.82, 167.09], 40, 1)
time.sleep(3)
mc.set_gripper_value(20,40)
time.sleep(3)
coords = mc.get_coords()
print(coords)
