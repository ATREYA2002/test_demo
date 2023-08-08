# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

N = int(input())
for i in range(N):
    x = list(map(int, input().split()))
    x.sort()
    print(x[1])