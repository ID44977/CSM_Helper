# -*- coding: UTF-8 -*-
import os
import glob
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

SUBDIY_Dir = "F:\\ACG\\Animate\\[BDMV] 素材\\"
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
print(subfile_dir)
os.chdir(subfile_dir)
subfile_num = glob.glob("*.ass")
#subfile_num = glob.glob('F:/ACG/Animate/[BDMV] 素材/ALL_SUB/路人女主的养成方法/*.ass')

'''
subfile_num = 0
for root,dirs,files in os.walk(subfile_dir):
    for each in files:
        subfile_num += 1
print(subfile_num)
'''

for files in os.walk(subfile_dir):
    print(subfile_dir + '\\' + files[2][0])
    for i in range(1, int(vol_num)+1):
        for j in range(0, int(ep_num)):
            os.system('xcopy "' + subfile_dir + '\\' + files[2][(i-1)*int(ep_num) + j] + '" "' + SUBDIY_Dir + bdmv_name + '\\Vol.' + str(i) + '_SUBDIY" /c')
