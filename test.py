import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

SUB_Dir = "F:/ACG/Animate/[BDMV] 加流重灌/"
BDMV_Dir = "F:\ACG\Animate\[BDMV]"

print(u'测试开始')

bdmv_name = input("输入名称：")
print("bdmv_name = ", bdmv_name)
os.mkdir(SUB_Dir + bdmv_name)
print("成功创建文件夹" + bdmv_name)
vol_num = input("输入分卷个数：")
print("vol_num = ", vol_num)
for i in range(1, int(vol_num)+1):
    os.mkdir(SUB_Dir + bdmv_name + "/Vol." + str(i) + "_SUB")
print("成功创建目录")


var1 = 'waterstone977.ddns.net'
#var_source = '"F:\ACG\Animate\[BDMV]\[BDMV][アニメ][虚构推理][Kyokou Suiri][虚構推理][Vol.1-Vol.4 Fin][JP]\SUIRI_4\BDROM"'
#var_target = '"F:\ACG\Animate\[BDMV] 加流重灌\虚构推理\Vol.4"'
var_source = filedialog.askdirectory()
#print(var_source)
var_target = filedialog.askdirectory()
#print(var_target)
#print('echo d | xcopy "' + var_source + '" "' + var_target + '" /s /e /exclude:uncopy.txt')
os.system('echo d | xcopy "' + var_source + '" "' + var_target + '" /s /e /exclude:uncopy.txt')
os.system('pause')
print(u'测试结束')
