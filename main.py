#!/usr/bin/python
import os, sys
import ctypes
from library import *
from Servo_function import *
K=ctypes.CDLL("/usr/lib/libkipr.so")
sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)

K.enable_servos()  
K.create_connect()

claw_open(30)
arm_back(40)
while K.a_button() == 0:
	pass
K.msleep(2000)
    
#botguy grabber
drive_backwards(150, 780)
arm_BG(40)
#spin_CCW(75,10)
drive_backwards(160, 125)
claw_close(30)
drive_straight(160,400)
spin_CW(100,98)
arm_B(40)
claw_open(100)
spin_CW(100,45)
drive_backwards(160,600)
drive_straight(150, 550)
spin_CW(100,102)
arm_B(40)
drive_backwards(150,145)
claw_close(100)
arm_back(30)


        
        
        
        
        
        
        
        
        
        

"""
#spinmore
spin_CW(75,12)
#210
claw_close(210)
arm_S(40)
drive_straight(60,200)
spin_CCW(75,75)
arm_B(40)
drive_straight(80,250)
claw_open(45)

"""
K.create_disconnect()
K.disable_servos()