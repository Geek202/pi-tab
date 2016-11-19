#!/usr/bin/env python3
def controller(do,val):
	do = do.upper()
	if do == 'N':
		reset()
	elif do == 'F':
		forward(val)
	elif do == 'R':
		right(val)
	elif do == 'B':
		backward(val)
	elif do == 'L':
		left(val)
	elif do == 'U':
		penup()
	elif do == 'D':
		pendown()
	else:
		print("unrecognised command")
		return False
def string_artist(string):
	cmd_list = string.split('-')
	for cmd in cmd_list:
		cmd_len = len(cmd)
		if cmd_len == 0:
			continue
		cmd_type = cmd[0]
		num = 0
		if cmd_len > 1:
			num_string = cmd[1:]
			num = int(num_string)
		controller(cmd_type, num)
from turtle import *

screen = getscreen()
try:
	while True:
		program = screen.textinput('Drawing machine!','Enter a program for the turtle:\neg f100-r45-u-f100-l45-d-f100-r90-b50\nn = reset\nu/d = pen up/down\nf = forward\nb = backwards\nr = turn right\nl = turn left\nEND = exit')
		if program == 'END' or program == None:
			raise KeyboardInterrupt("Exit")
		string_artist(program)
except:
	pass
finally:
	print("Have a nice day! :-)")
			
