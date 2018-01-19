#!/usr/bin/env python


import sys
import time
import random

randnumber = 0;


def start2() :
	print random.randint(1, 6);
	def start() :
		while True:
				reply = str(raw_input("Run again?"+' (y/n): ')).lower().strip()
				if reply[:1] == 'y':
					start2()
				if reply[:1] == 'n':
					sys.exit()
				else:
					print("\n""\n""Only answer with y or n.");
	start()
start2()


#TODO: Upgrade to python3. Raw_input is causing trouble here.