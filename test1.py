from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time
mc = MyCobot(PI_PORT, PI_BAUD)


coords = mc.get_coords()
print(coords)
##mc.send_coords([-207.7, 5.8, 96.2, -76.46, -67.62, 140.84], 40, 1)
##mc.send_coords([-255.6, 6.5, 213.9, -77.57, -62.13, 142.93], 40, 1)
mc.set_gripper_value(120,40)
time.sleep(3)
##mc.send_coords([-229.6, -16.5, 148.9, -96.24, -57.95, 157.8]
mc.send_coords([-52.8, -264.2, 203.0, -92.88, -54.09, -122.33],40, 1)
time.sleep(5)
mc.set_gripper_value(70,40)
time.sleep(3)

##mc.send_coords([125.6, -177.7, 195.2, -105.52, -62.55, 169.74], 40, 1)
##mc.send_coords(mc.send_coords([125.6, -177.7, 195.2, -105.52, -62.55, 169.74], 40, 1)
mc.send_coords([-267.5, 2.8, 159.6, -81.57, -58.66, 147.18], 40, 1)

time.sleep(3)
mc.set_gripper_value(200,40)
time.sleep(3)

coords = mc.get_coords()
print(coords)

