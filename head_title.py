# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 01:35:40 2019

head title
20190130
version 0.0

@author: user
"""

import tkinter as tk
from tkinter import ttk

ini_font = ('Microsoft YaHei UI', 16, 'bold')
ini_title = '測  試  用  標  題'
# it is necessary to input chinese string for head title.

# title is 'head title' string
# set_font is to set font for title label

class head_title(tk.Frame):
    def __init__(self,master=None, title = ini_title, set_font = ini_font):
        tk.Frame.__init__(self,master)
        
        self.title_frame = tk.Frame(master)
        self.title_frame.pack(side="top", fill='x')
        
        self.title_label = tk.Label(self.title_frame, 
                                    text=title, 
                                    height = 2,
                                    fg="black",
                                    bg = 'white',
                                    font=set_font)
        self.title_label.pack(side='top') #, pady=10, expand='yes')


        self.title_sp1_1 = ttk.Separator(self.title_frame, 
                                         style="Line.TSeparator",
                                         orient="horizontal")
        self.title_sp1_1.pack(side='top', fill = 'x')
        
        
        
# In[000]:
#==============================================================================
# maintain window

def main():
    root = tk.Tk()

    head_title(root)

    w = 1500
    h = 700
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title('maintain window' + ' (Version 0.0)')
    #root.state('zoomed')
    #root.wm_attributes('-topmost',1) #窗口彈出置頂
    #root.iconbitmap("envi.ico")
    root.mainloop()


if __name__ == '__main__':
    main()  
        