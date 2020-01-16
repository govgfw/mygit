"""
练习1：华氏温度转换为摄氏温度。
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

Version: 0.1
Author: govgfw
"""

F=float(input('请输入华氏温度： '))
C=(F-32)/1.8
print('对应的摄氏度为： %f' % C)
print('%.1f 华氏温度 = %.1f 摄氏温度' % (F , C))