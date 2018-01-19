#!/usr/bin/env python3

import sys
import time
import random

randnumber = 0;

def start() :
    print random.randint(1, 6);

while True:
        str(raw_input("Run again?"+' (y/n): ')).lower().strip()
    a = str(input("Enter yes/no to continue: "))
    if a=="yes":
        gameplay()
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no")
start()

def gameplay () :
    print ("GAMEPLAY!")