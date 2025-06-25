#!/usr/bin/env python3
import sys
import re

if len(sys.argv)-1 != 2:
    print("none")
else:
    same = re.findall(sys.argv[1], sys.argv[2])
    print(len(same))