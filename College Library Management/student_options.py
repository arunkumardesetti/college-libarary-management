#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 12:07:27 AM

import sys

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

import student_options_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.resizable(0, 0)
    top = OPTIONS (root)
    student_options_support.init(root, top)
    root.mainloop()

w = None
def create_OPTIONS(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = OPTIONS (w)
    student_options_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_OPTIONS():
    global w
    w.destroy()
    w = None


class OPTIONS:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("591x357+626+195")
        top.title("OPTIONS")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.1, rely=0.08, height=46, width=489)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome Student''')

        self.logout = Button(top)
        self.logout.place(relx=0.86, rely=0.03, height=33, width=69)
        self.logout.configure(activebackground="#d9d9d9")
        self.logout.configure(activeforeground="#000000")
        self.logout.configure(background="#d9d9d9")
        self.logout.configure(command=student_options_support.logout_Function)
        self.logout.configure(disabledforeground="#a3a3a3")
        self.logout.configure(foreground="#000000")
        self.logout.configure(highlightbackground="#d9d9d9")
        self.logout.configure(highlightcolor="black")
        self.logout.configure(pady="0")
        self.logout.configure(text='''Logout''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.1, rely=0.25, relheight=0.6, relwidth=0.82)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=483)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.1, rely=0.05, height=36, width=378)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Choose one of the options to continue''')

        self.v_all_book_details = Button(self.Canvas1)
        self.v_all_book_details.place(relx=0.12, rely=0.28, height=53, width=361)

        self.v_all_book_details.configure(activebackground="#d9d9d9")
        self.v_all_book_details.configure(activeforeground="#000000")
        self.v_all_book_details.configure(background="#d9d9d9")
        self.v_all_book_details.configure(command=student_options_support.view_all_book_details_Function)
        self.v_all_book_details.configure(disabledforeground="#a3a3a3")
        self.v_all_book_details.configure(font=font9)
        self.v_all_book_details.configure(foreground="#000000")
        self.v_all_book_details.configure(highlightbackground="#d9d9d9")
        self.v_all_book_details.configure(highlightcolor="black")
        self.v_all_book_details.configure(pady="0")
        self.v_all_book_details.configure(text='''VIEW ALL BOOK DETAILS''')

        self.searchbook = Button(self.Canvas1)
        self.searchbook.place(relx=0.12, rely=0.52, height=53, width=361)
        self.searchbook.configure(activebackground="#d9d9d9")
        self.searchbook.configure(activeforeground="#000000")
        self.searchbook.configure(background="#d9d9d9")
        self.searchbook.configure(command=student_options_support.search_book_Function)
        self.searchbook.configure(disabledforeground="#a3a3a3")
        self.searchbook.configure(font=font9)
        self.searchbook.configure(foreground="#000000")
        self.searchbook.configure(highlightbackground="#d9d9d9")
        self.searchbook.configure(highlightcolor="black")
        self.searchbook.configure(pady="0")
        self.searchbook.configure(text='''SEARCH BOOK''')






#if __name__ == '__main__':
#    vp_start_gui()



