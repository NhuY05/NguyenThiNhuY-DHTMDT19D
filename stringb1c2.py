# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:53:00 2024

@author: Vivobook
"""

print("bai2Câu 2: ")
s = "Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
s1 = s.replace("P. ","" ).replace("P.","").replace("Q.","").replace("Tp.","").split(", ")
for i in s1:
    print(i)
