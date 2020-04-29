#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 11:30:24 PM

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

import student_login_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.resizable(0, 0)
    student_login_gui_support.set_Tk_var()
    top = Student_login (root)
    student_login_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Student_login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    student_login_gui_support.set_Tk_var()
    top = Student_login (w)
    student_login_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_login():
    global w
    w.destroy()
    w = None


class Student_login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x540+662+216")
        top.title("Student login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.12, rely=0.07, height=44, width=468)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''WELCOME TO STUDENT LOGIN''')
        self.Label1.configure(width=468)

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.1, rely=0.19, relheight=0.75, relwidth=0.81)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=483)

        self.Label5 = Label(self.Canvas1)
        self.Label5.place(relx=0.1, rely=0.07, height=34, width=374)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Please fill your credentials to login''')

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.12, rely=0.25, height=36, width=86)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Login ID''')

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.12, rely=0.45, height=36, width=97)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Password''')

        self.id_entry = Entry(self.Canvas1)
        self.id_entry.place(relx=0.41, rely=0.25,height=34, relwidth=0.46)
        self.id_entry.configure(background="white")
        self.id_entry.configure(disabledforeground="#a3a3a3")
        self.id_entry.configure(font="TkFixedFont")
        self.id_entry.configure(foreground="#000000")
        self.id_entry.configure(highlightbackground="#d9d9d9")
        self.id_entry.configure(highlightcolor="black")
        self.id_entry.configure(insertbackground="black")
        self.id_entry.configure(selectbackground="#c4c4c4")
        self.id_entry.configure(selectforeground="black")
        self.id_entry.configure(textvariable=student_login_gui_support.uid)

        self.password_entry = Entry(self.Canvas1)
        self.password_entry.place(relx=0.41, rely=0.45, height=34, relwidth=0.46)

        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="#c4c4c4")
        self.password_entry.configure(selectforeground="black")
        self.password_entry.configure(show="*")
        self.password_entry.configure(textvariable=student_login_gui_support.upassword)

        self.backbutton = Button(self.Canvas1)
        self.backbutton.place(relx=0.1, rely=0.6, height=43, width=89)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#d9d9d9")
        self.backbutton.configure(command=student_login_gui_support.back_Function)
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#000000")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''BACK''')

        self.clear = Button(self.Canvas1)
        self.clear.place(relx=0.43, rely=0.6, height=43, width=85)
        self.clear.configure(activebackground="#d9d9d9")
        self.clear.configure(activeforeground="#000000")
        self.clear.configure(background="#d9d9d9")
        self.clear.configure(command=student_login_gui_support.clear_Function)
        self.clear.configure(disabledforeground="#a3a3a3")
        self.clear.configure(foreground="#000000")
        self.clear.configure(highlightbackground="#d9d9d9")
        self.clear.configure(highlightcolor="black")
        self.clear.configure(pady="0")
        self.clear.configure(text='''CLEAR''')

        self.loginbutton = Button(self.Canvas1)
        self.loginbutton.place(relx=0.75, rely=0.6, height=43, width=75)
        self.loginbutton.configure(activebackground="#d9d9d9")
        self.loginbutton.configure(activeforeground="#000000")
        self.loginbutton.configure(background="#d9d9d9")
        self.loginbutton.configure(command=student_login_gui_support.login_Function)
        self.loginbutton.configure(disabledforeground="#a3a3a3")
        self.loginbutton.configure(font=font10)
        self.loginbutton.configure(foreground="#000000")
        self.loginbutton.configure(highlightbackground="#d9d9d9")
        self.loginbutton.configure(highlightcolor="black")
        self.loginbutton.configure(pady="0")
        self.loginbutton.configure(text='''LOGIN''')

        self.Label4 = Label(self.Canvas1)
        self.Label4.place(relx=0.04, rely=0.74, height=26, width=444)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Not a registered student? Click below button to register''')
        self.Label4.configure(width=444)

        self.registerbutton = Button(self.Canvas1)
        self.registerbutton.place(relx=0.41, rely=0.84, height=43, width=106)
        self.registerbutton.configure(activebackground="#d9d9d9")
        self.registerbutton.configure(activeforeground="#000000")
        self.registerbutton.configure(background="#d9d9d9")
        self.registerbutton.configure(command=student_login_gui_support.register_Function)
        self.registerbutton.configure(disabledforeground="#a3a3a3")
        self.registerbutton.configure(font=font13)
        self.registerbutton.configure(foreground="#000000")
        self.registerbutton.configure(highlightbackground="#d9d9d9")
        self.registerbutton.configure(highlightcolor="black")
        self.registerbutton.configure(pady="0")
        self.registerbutton.configure(text='''REGISTER''')
        self.registerbutton.configure(width=106)






#if __name__ == '__main__':
#    vp_start_gui()



