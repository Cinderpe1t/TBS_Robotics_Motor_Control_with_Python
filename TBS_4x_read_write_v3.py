#!/usr/bin/env python

import os
import sys, tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getch():
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

from dxl_4x_drive import *

drive_4x=dxl_4x()
drive_4x.torqueOn()

speedMotor=0
turnLeftRight=0

while 1:
    print("1: decrease speed, 2: stop, 3: increase speed, J: left turn, K: straight, L: right turn (or press ESC to quit!)")
    charInput=getch()
    if charInput == chr(0x1b):
        break
    if charInput == "1":
        speedMotor-=50
    if charInput == "2":
        speedMotor=0
    if charInput == "3":
        speedMotor+=50
    if charInput == "z":
        turnLeftRight=0
    if charInput == "j":
        turnLeftRight+=50
    if charInput == "k":
        turnLeftRight=0
    if charInput == "l":
        turnLeftRight-=50

    # Set speed
    drive_4x.setSpeed(speedMotor,turnLeftRight)
    drive_4x.updateSpeed()
    drive_4x.getCurrentSpeed()
    print("Status: %d/%d %d/%d %d/%d %d/%d" % (drive_4x.speedNowMotor1, drive_4x.speedMotor1, drive_4x.speedNowMotor2, drive_4x.speedMotor2, drive_4x.speedNowMotor3, drive_4x.speedMotor3, drive_4x.speedNowMotor4, drive_4x.speedMotor4) )
  
drive_4x.torqueOff()
drive_4x.closePort()
