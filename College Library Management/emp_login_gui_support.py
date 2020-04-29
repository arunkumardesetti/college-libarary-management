#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 12:43:40 AM
#    May 18, 2018 09:16:00 AM


import sys
import common
import emp_options
try:
    from Tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global uid
    uid = StringVar()
    global upassword
    upassword = StringVar()

def back_Function():
    destroy_window()
    common.vp_start_gui()
    sys.stdout.flush()

def clear_Function():
    uid.set("")
    upassword.set("")
    sys.stdout.flush()

def login_Function():
    id = uid.get()
    password = upassword.get()
    import Db_Operations as dbo
    a = dbo.login(id,password)
    import tkMessageBox as tkmsg
    if a == 1:
        tkmsg.showinfo(title="SUCCESSFUL",message="LOGIN SUCCESSFUL")
        destroy_window()
        emp_options.vp_start_gui()
    elif a == 0:
        tkmsg.showerror(title="LOGIN ERROR",message="LOGIN ID OR PASSWORD INCORRECT")
        clear_Function()
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

#if __name__ == '__main__':
#    import emp_login_gui
#    emp_login_gui.vp_start_gui()





