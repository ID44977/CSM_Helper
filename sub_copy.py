# -*- coding: UTF-8 -*-
import os
import glob
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

SUBDIY_Dir = "F:\\BDMV DIY\\"
SUBDIY_SOURCE_Dir = "ALL_SUB\\"

bdmv_name = input("输入名称：")
print("bdmv_name = ", bdmv_name)

os.mkdir(SUBDIY_Dir + bdmv_name)
print("成功创建文件夹" + bdmv_name)

vol_num = input("输入分卷个数：")
print("vol_num = ", vol_num)

for i in range(1, int(vol_num)+1):
    os.mkdir(SUBDIY_Dir + bdmv_name + "\\Vol." + str(i) + "_SUBDIY")
print("成功创建目录")

ep_num = input("输入每卷集数：")
print("ep_num = ", ep_num)

#xcopy "F:\BDMV DIY\ALL_SUB\Date A Live2\[CASO&SumiSora][Date_A_Live_II][BDRip][01][x264_flac](4CDCAA43).sc.ass" "F:\BDMV DIY\Date A Live2\Vol.1_SUBDIY"

subfile_dir = SUBDIY_Dir + SUBDIY_SOURCE_Dir + bdmv_name
#print(subfile_dir)
subfile_num = glob.glob(subfile_dir + "\\*.ass")
for files in os.walk(subfile_dir):
    #print(subfile_dir + '\\' + files[2][0])
    for i in range(1, int(vol_num)+1):
        for j in range(0, int(ep_num)):
            #print("文件个数：" + str(len(subfile_num)-1))
            if int(i)*2-1-int(j) <= len(subfile_num)-1:
                os.system('xcopy "' + subfile_dir + '\\' + files[2][int(i)*2-1-int(j)] + '" "' + SUBDIY_Dir + bdmv_name + '\\Vol.' + str(i) + '_SUBDIY" /c')
