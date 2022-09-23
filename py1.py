#！/usr/bin/env python
import py2
import joystick_info

py2.py2_function()

class PY1():
  def __init__(self) -> None:
    self.joystick = joystick_info.Joysitck()
    

  def runLoop(self):
    self.joystick.Joyread()

py1 = PY1()
while True:
  py1.runLoop()
