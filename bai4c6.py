# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:49:26 2024

@author: Vivobook
"""

print("Câu 4: ")
gio = int(input("Nhập giờ: "))

phut = int(input("Nhập phút: "))
 
giay = int(input("Nhập giây: "))

tongsogiay = gio * 3600 + phut * 60 + giay
print("Kết quả khi đổi ra giây: ", tongsogiay)
