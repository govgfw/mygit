"""
练习2：输入圆的半径计算计算周长和面积。

Version: 0.1
Author: govgfw
"""
import math
R = float(input('请输入半径： '))
L = 2 * math.pi * R
S = math.pi * R * R
print("周长是： %.2f ， 面积是： %.2f" % (L, S))