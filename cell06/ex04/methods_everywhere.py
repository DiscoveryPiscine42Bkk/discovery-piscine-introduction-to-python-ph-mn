#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])
def enlarge(text):
    print(text + (8-len(text))*"Z")

if len(sys.argv) < 2:
    print("none")
else:
    for n in sys.argv[1:]:
        if len(n) > 8:
            shrink(n)
        else:
            enlarge(n)