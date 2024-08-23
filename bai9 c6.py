# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:51:21 2024

@author: Vivobook
"""

print("Câu 9: ")
import math
a=float(input("Nhập vào số thực a: "))
b=float(input("Nhập vào số thực b: "))
a1=math.sqrt(a)
b1=math.sqrt(b)
a2=pow(a, 1/4)
b2=pow(b, 1/4)
ab=pow(a*b, 1/4)
print("Kết quả: ",((a1-b1)/(a2-b2)) - ((a1+ab)/(a2+b2)))