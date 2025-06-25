#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
    print("none")
else:
    input_string = ' '.join(sys.argv[1:])  
    z_matches = re.findall(r'z', input_string)

    if z_matches:
        print(''.join(z_matches))  
    else:
        print("none")