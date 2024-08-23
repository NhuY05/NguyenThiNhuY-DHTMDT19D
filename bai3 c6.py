# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:48:44 2024

@author: Vivobook
"""

print("Câu 3: ")
N = int(input("Nhập vào số nguyên dương có 2 chữ số: "))
a = N // 10
b = N % 10
if 10 <= N <= 99:
    print("Kết quả là: ", a + b)
else:
    print("Không thực hiện được")