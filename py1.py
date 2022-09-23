#！/usr/bin/env python
import py2
# import joystick_info
from joystick_info import *

py2.py2_function()

class PY1():
  def __init__(self) -> None:
    # self.joystick = joystick_info.Joysitck()
    self.joystick = Joysitck()
    

  def runLoop(self):
    reList = self.joystick.Joyread()
    # print(reList)
    value = reList[0]
    type = reList[1]
    number = reList[2]
    if type & 0x02:
      if number == 0x00:
        fvalue = value / 30000
        print("X: %.3f" % (fvalue))
      # if number == 0x01:
      #   fvalue = value / 30000
      #   print("Y: %.3f" % (fvalue))
    if type & 0x01:
      if number == self.joystick.BUTTON_A:
        print("Button_A: %.3f" % (value))
      elif number == self.joystick.BUTTON_B:
        print("Button_B: %.3f" % (value))
      elif number == self.joystick.BUTTON_X:
        print("Button_X: %.3f" % (value))
      elif number == self.joystick.BUTTON_Y:
        print("Button_Y: %.3f" % (value))

py1 = PY1()
while True:
  py1.runLoop()
