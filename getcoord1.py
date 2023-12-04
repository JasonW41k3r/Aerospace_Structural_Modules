from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time
mc = MyCobot(PI_PORT, PI_BAUD)
coords = mc.get_coords()
print(coords)
