#!/usr/bin/env python3
import sys

if len(sys.argv)-1 != 2:
    print("none")
else:
    for i in range(sys.argv[1],sys.argv[2]):
        print(list(range(sys.argv[1],sys.argv[2])))
