import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
#file_path = filedialog.askopenfilename()		# 选择文件，路径保存于file_path中
foldr_patch = filedialog.askdirectory()			# 选择文件夹，路径保存于foldr_patch中
#save_patch = filedialog.asksaveasfilename()		# 获取保存路径的目录

#print(file_path)			# 打印
print(foldr_patch)