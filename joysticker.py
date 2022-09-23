import os, struct, array
from fcntl import ioctl
from time import time

print("Connected joystick device:")

#获取joystick端口文件
for dev_in in os.listdir('/dev/input'):
  if dev_in.startswith('js'):
    print('joystick: /dev/input/%s'  %(dev_in))

axis_states = {}
button_statas = {}
#命名方式在Linux/input.h
axis_names = {
  0x00 : 'x',
  0x01 : 'y',
  0x05 : 'rz',
}

axis_map = []

#XBox键位地址
# BUTTON_A = 0x00
# BUTTON_B = 0x01
# BUTTON_X = 0x02
# BUTTON_Y = 0x03

#Swith Pro 键位地址
BUTTON_B = 0x00
BUTTON_A = 0x01
BUTTON_Y = 0x02
BUTTON_X = 0x03

dev_in = '/dev/input/js0'
#打开文件，rb字节bytes格式
jsdev = open(dev_in, 'rb')

#获取手柄名字
buf = array.array('u', ['\0'] * 5)
ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf)
js_name = buf.tostring()
print('Device name: %s' % js_name)

#获取手柄轴和案件的编号
buf = array.array('B', [0])
ioctl(jsdev, 0x80016a11, buf)
num_axes = buf[0]

#获取摇杆映射
buf = array.array('B', [0] * 0x40)
ioctl(jsdev, 0x80406a32, buf)
for axis in buf[:num_axes]:
  axis_name = axis_names.get(axis, 'unknown(0x%02x)' % axis)
  axis_map.append(axis_name)
  axis_states[axis_name] = 0.0

while True:
  evbuf = jsdev.read(8)
  if evbuf:
    time, value, type, number = struct.unpack('IhBB', evbuf)

    # if type & 0x02:
    #   axis = axis_map[number]
    #   if axis:
    #     if axis == "x":
    #       fvalue = value / 30000

    #       axis_states[axis] = fvalue
    #       print("%s: %.3f" % (axis, fvalue))
    #     if axis == "y":
    #       fvalue = value / 30000

    #       axis_states[axis] = fvalue
    #       print("%s: %.3f" % (axis, fvalue))        
    if type & 0x02:  
      if number == 0x00:
        fvalue = value / 30000

        # axis_states[axis] = fvalue
        print("X: %.3f" % (fvalue))
      if number == 0x01:
        fvalue = value / 30000

        # axis_states[axis] = fvalue
        print("Y: %.3f" % (fvalue))
    if type & 0x01:
      if number == BUTTON_A:
        print("Button_A: %.3f" % (value))
      elif number == BUTTON_B:
        print("Button_B: %.3f" % (value))
      elif number == BUTTON_X:
        print("Button_X: %.3f" % (value))
      elif number == BUTTON_Y:
        print("Button_Y: %.3f" % (value))