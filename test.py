import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
print(u'测试开始')
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
