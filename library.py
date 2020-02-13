#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")

def drive_straight(speed, dist_to_go):
	K.set_create_distance(0)
  	K.create_drive_direct(speed, speed)
  	while K.get_create_distance() < dist_to_go:
		print (K.get_create_distance(), ":", dist_to_go)
		pass
 	K.create_drive_direct(0,0)
 
def drive_backwards(speed, dist_to_go):
	K.set_create_distance(0)
  	K.create_drive_direct(-speed, -speed)
  	while K.get_create_distance() > -dist_to_go:
		pass
 	K.create_drive_direct(0,0)
            
def spin_CCW(speed, angle_to_go):
	K.set_create_total_angle(0)
  	K.create_spin_CCW(speed)
  	while K.get_create_total_angle() < angle_to_go:
		pass
 	K.create_drive_direct(0,0)
            
def spin_CW(speed, angle_to_go):
	K.set_create_total_angle(0)
  	K.create_spin_CW(speed)
  	while K.get_create_total_angle() > -angle_to_go:
		pass
 	K.create_drive_direct(0,0)
            
def drive_till_bump(speed):
	K.create_drive_direct(speed, speed)
  	while K.get_create_lbump() == 0 and get_create_rbump()==0:
		pass
 	K.create_drive_direct(0,0) 
        
def back_till_bump(speed):
	K.create_drive_direct(-speed, -speed)
  	while K.get_create_lbump() == 0 and get_create_rbump()==0:
		pass
 	K.create_drive_direct(0,0)
            

