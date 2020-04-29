#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 03:18:33 AM

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

import return_book_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.resizable(0,0)
    return_book_support.set_Tk_var()
    top = Return_Book (root)
    return_book_support.init(root, top)
    root.mainloop()

w = None
def create_Return_Book(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    return_book_support.set_Tk_var()
    top = Return_Book (w)
    return_book_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Return_Book():
    global w
    w.destroy()
    w = None


class Return_Book:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x369+651+252")
        top.title("Return Book")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.07, rely=0.08, height=47, width=178)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Return Book''')

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.07, rely=0.27, relheight=0.63, relwidth=0.86)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=513)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.16, rely=0.13, height=34, width=75)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Book ID''')

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.16, rely=0.36, height=34, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Roll No.''')

        self.bookid = Entry(self.Canvas1)
        self.bookid.place(relx=0.45, rely=0.17,height=28, relwidth=0.48)
        self.bookid.configure(background="white")
        self.bookid.configure(disabledforeground="#a3a3a3")
        self.bookid.configure(font="TkFixedFont")
        self.bookid.configure(foreground="#000000")
        self.bookid.configure(highlightbackground="#d9d9d9")
        self.bookid.configure(highlightcolor="black")
        self.bookid.configure(insertbackground="black")
        self.bookid.configure(selectbackground="#c4c4c4")
        self.bookid.configure(selectforeground="black")
        self.bookid.configure(textvariable=return_book_support.bid)

        self.roll = Entry(self.Canvas1)
        self.roll.place(relx=0.45, rely=0.39,height=28, relwidth=0.48)
        self.roll.configure(background="white")
        self.roll.configure(disabledforeground="#a3a3a3")
        self.roll.configure(font="TkFixedFont")
        self.roll.configure(foreground="#000000")
        self.roll.configure(highlightbackground="#d9d9d9")
        self.roll.configure(highlightcolor="black")
        self.roll.configure(insertbackground="black")
        self.roll.configure(selectbackground="#c4c4c4")
        self.roll.configure(selectforeground="black")
        self.roll.configure(textvariable=return_book_support.sroll)

        self.backbutton = Button(self.Canvas1)
        self.backbutton.place(relx=0.12, rely=0.69, height=33, width=76)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#d9d9d9")
        self.backbutton.configure(command=return_book_support.back_Function)
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#000000")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''BACK''')

        self.clearbutton = Button(self.Canvas1)
        self.clearbutton.place(relx=0.43, rely=0.69, height=33, width=75)
        self.clearbutton.configure(activebackground="#d9d9d9")
        self.clearbutton.configure(activeforeground="#000000")
        self.clearbutton.configure(background="#d9d9d9")
        self.clearbutton.configure(command=return_book_support.clear_Function)
        self.clearbutton.configure(disabledforeground="#a3a3a3")
        self.clearbutton.configure(foreground="#000000")
        self.clearbutton.configure(highlightbackground="#d9d9d9")
        self.clearbutton.configure(highlightcolor="black")
        self.clearbutton.configure(pady="0")
        self.clearbutton.configure(text='''CLEAR''')

        self.returnButton = Button(self.Canvas1)
        self.returnButton.place(relx=0.76, rely=0.69, height=33, width=74)
        self.returnButton.configure(activebackground="#d9d9d9")
        self.returnButton.configure(activeforeground="#000000")
        self.returnButton.configure(background="#d9d9d9")
        self.returnButton.configure(command=return_book_support.return_Function)
        self.returnButton.configure(disabledforeground="#a3a3a3")
        self.returnButton.configure(font=font11)
        self.returnButton.configure(foreground="#000000")
        self.returnButton.configure(highlightbackground="#d9d9d9")
        self.returnButton.configure(highlightcolor="black")
        self.returnButton.configure(pady="0")
        self.returnButton.configure(text='''RETURN''')

        self.logoutbutton = Button(top)
        self.logoutbutton.place(relx=0.88, rely=0.03, height=33, width=59)
        self.logoutbutton.configure(activebackground="#d9d9d9")
        self.logoutbutton.configure(activeforeground="#000000")
        self.logoutbutton.configure(background="#d9d9d9")
        self.logoutbutton.configure(command=return_book_support.logout_Function)
        self.logoutbutton.configure(disabledforeground="#a3a3a3")
        self.logoutbutton.configure(foreground="#000000")
        self.logoutbutton.configure(highlightbackground="#d9d9d9")
        self.logoutbutton.configure(highlightcolor="black")
        self.logoutbutton.configure(pady="0")
        self.logoutbutton.configure(text='''Logout''')






#if __name__ == '__main__':
#    vp_start_gui()



