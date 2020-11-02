#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
calculate fibonacci
1
2
3
5
8
13
...

"""

import random

count=random.randrange(10)

value=stack="1"
print (stack)
i=1
while (i <= count):
    i+=1
    last=stack

    stack+=last
    print(stack)