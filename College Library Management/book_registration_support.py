#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 08:26:09 PM


import sys
import emp_login_gui
import emp_options
import Db_Operations as dbo
import tkMessageBox as tkmsg
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
    global btitle
    btitle = StringVar()
    global bsub
    bsub = StringVar()
    global bauthor
    bauthor = StringVar()

def back_Function():
    destroy_window()
    emp_options.vp_start_gui()
    sys.stdout.flush()

def clear_Function():
    btitle.set("")
    bsub.set("")
    bauthor.set("")
    sys.stdout.flush()

def logout_Function():
    destroy_window()
    emp_login_gui.vp_start_gui()
    sys.stdout.flush()

def submit_Function():
    title = btitle.get()
    subject = bsub.get()
    author = bauthor.get()
    a = dbo.book_registration(title,subject,author)
    if a==1:
        tkmsg.showinfo(title="SUCCESSFUL", message="NEW BOOK ADDED TO RECORD\nTHANK YOU!")
    elif a==0:
        tkmsg.showerror(title="ERROR",message="BOOK CANNOT BE ADDED")
    destroy_window()
    emp_options.vp_start_gui()
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
#    import book_registration
#    book_registration.vp_start_gui()


