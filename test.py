import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

SUBBED_Dir = "F:\\ACG\\Animate\\[BDMV] 加流重灌\\HardLink\\"
BDMV_Dir = "F:\\ACG\\Animate\\[BDMV]"

print(u'测试开始')

bdmv_name = input("输入名称：")
print("bdmv_name = ", bdmv_name)
os.mkdir(SUBBED_Dir + bdmv_name)
print("成功创建文件夹" + bdmv_name)
vol_num = input("输入分卷个数：")
print("vol_num = ", vol_num)
for i in range(1, int(vol_num)+1):
    os.mkdir(SUBBED_Dir + bdmv_name + "\\Vol." + str(i) + "_SUBBED")
print("成功创建目录")


var_source = []
for i in range(1, int(vol_num)+1):
    var_source.append(filedialog.askdirectory())

var_target = []
for i in range(1, int(vol_num)+1):
    var_target.append(SUBBED_Dir + bdmv_name + "\\Vol." + str(i) + "_SUBBED")

#print('echo d | xcopy "' + var_source + '" "' + var_target + '" /s /e /exclude:uncopy.txt')
for i in range (0, int(vol_num)):
    os.system('echo d | xcopy "' + var_source[i] + '" "' + var_target[i] + '" /s /e /exclude:uncopy.txt')

os.system('pause')
print(u'测试结束')
