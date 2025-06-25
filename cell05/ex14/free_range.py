#!/usr/bin/env python3
import sys

if len(sys.argv)-1 != 2:
    print("none")
else:
    print(list(range(int (sys.argv[1]),int(sys.argv[2])+1)), end="")