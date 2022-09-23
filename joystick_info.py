import os, struct, array
from fcntl import ioctl


class Joysitck():
  def __init__(self):
    self.axis_states = {}
    self.button_states = {}
    
    self.BUTTON_B = 0x00
    self.BUTTON_A = 0x01
    self.BUTTON_Y = 0x02
    self.BUTTON_X = 0x03   

    self.jsdev = open('/dev/input/js0', 'rb')

    self.t = 0
    self.value = 0
    self.type = 0
    self.number = 0

  def Joyread(self):
    evbuf = self.jsdev.read(8)
    if evbuf:
      time, value, type, number = struct.unpack('IhBB', evbuf)
      print(str(struct.unpack('IhBB', evbuf)))
      if type & 0x02:
        if number == 0x00:
          fvalue = value / 30000
          print("X: %.3f" % (fvalue))
        if number == 0x01:
          fvalue = value / 30000
          print("Y: %.3f" % (fvalue))
      if type & 0x01:
        if number == self.BUTTON_A:
          print("Button_A: %.3f" % (value))
        elif number == self.BUTTON_B:
          print("Button_B: %.3f" % (value))
        elif number == self.BUTTON_X:
          print("Button_X: %.3f" % (value))
        elif number == self.BUTTON_Y:
          print("Button_Y: %.3f" % (value))

