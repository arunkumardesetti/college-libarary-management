#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 09:03:52 AM
#    May 18, 2018 09:06:25 AM


import sys
import emp_login_gui
import student_login_gui
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



def empcall():
    destroy_window()
    emp_login_gui.vp_start_gui()
    sys.stdout.flush()

def stucall():
    destroy_window()
    student_login_gui.vp_start_gui()
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

if __name__ == '__main__':
    import common
    common.vp_start_gui()





