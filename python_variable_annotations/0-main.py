#!/usr/bin/env python3

add = __import('0-add').add

print(add(1.12, 2.34) == 1.12 + 2.34)
print(add.__annotations__)
