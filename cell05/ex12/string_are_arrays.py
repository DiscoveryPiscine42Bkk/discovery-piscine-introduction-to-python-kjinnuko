#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit(1)

input_str = sys.argv[1]
z_list = [char for char in input_str if char == 'z']

if z_list:
    print(''.join(z_list))
else:
    print("none")