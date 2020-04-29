#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 12:26:05 AM

import sys
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

import student_search_result_support

def vp_start_gui(a):
    '''Starting point when module is the main routine.'''
    global val, w, root, key
    root = Tk()
    key = a
    top = Search_Result (root)
    student_search_result_support.init(root, top)
    root.mainloop()

w = None
def create_Search_Result(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Search_Result (w)
    student_search_result_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Search_Result():
    global w
    w.destroy()
    w = None


class Search_Result:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x357+651+252")
        top.title("Search Result")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.32, rely=0.03, height=47, width=195)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Search Result''')

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(relx=0.0, rely=0.15, relheight=0.62
                                     , relwidth=1.0)
        self.Scrolledtreeview1["columns"] = ("Col1", "Col2", "Col3", "Col4", "Col5")
        self.Scrolledtreeview1['show'] = 'headings'
        self.Scrolledtreeview1.heading("#0", text="Tree")
        self.Scrolledtreeview1.heading("#0", anchor="center")
        self.Scrolledtreeview1.column("#0", width="288")
        self.Scrolledtreeview1.column("#0", minwidth="20")
        self.Scrolledtreeview1.column("#0", stretch="1")
        self.Scrolledtreeview1.column("#0", anchor="w")
        self.Scrolledtreeview1.heading("Col1", text="Book ID")
        self.Scrolledtreeview1.heading("Col1", anchor="center")
        self.Scrolledtreeview1.column("Col1", width="289")
        self.Scrolledtreeview1.column("Col1", minwidth="20")
        self.Scrolledtreeview1.column("Col1", stretch="1")
        self.Scrolledtreeview1.column("Col1", anchor="w")

        self.Scrolledtreeview1.heading("Col2", text="Title")
        self.Scrolledtreeview1.heading("Col2", anchor="center")
        self.Scrolledtreeview1.column("Col2", width="289")
        self.Scrolledtreeview1.column("Col2", minwidth="20")
        self.Scrolledtreeview1.column("Col2", stretch="1")
        self.Scrolledtreeview1.column("Col2", anchor="w")

        self.Scrolledtreeview1.heading("Col3", text="Subject")
        self.Scrolledtreeview1.heading("Col3", anchor="center")
        self.Scrolledtreeview1.column("Col3", width="289")
        self.Scrolledtreeview1.column("Col3", minwidth="20")
        self.Scrolledtreeview1.column("Col3", stretch="1")
        self.Scrolledtreeview1.column("Col3", anchor="w")

        self.Scrolledtreeview1.heading("Col4", text="Author")
        self.Scrolledtreeview1.heading("Col4", anchor="center")
        self.Scrolledtreeview1.column("Col4", width="289")
        self.Scrolledtreeview1.column("Col4", minwidth="20")
        self.Scrolledtreeview1.column("Col4", stretch="1")
        self.Scrolledtreeview1.column("Col4", anchor="w")

        self.Scrolledtreeview1.heading("Col5", text="Status")
        self.Scrolledtreeview1.heading("Col5", anchor="center")
        self.Scrolledtreeview1.column("Col5", width="289")
        self.Scrolledtreeview1.column("Col5", minwidth="20")
        self.Scrolledtreeview1.column("Col5", stretch="1")
        self.Scrolledtreeview1.column("Col5", anchor="w")




        self.backButton = Button(top)
        self.backButton.place(relx=0.43, rely=0.84, height=43, width=89)
        self.backButton.configure(activebackground="#d9d9d9")
        self.backButton.configure(activeforeground="#000000")
        self.backButton.configure(background="#d9d9d9")
        self.backButton.configure(command=student_search_result_support.back_Function)
        self.backButton.configure(disabledforeground="#a3a3a3")
        self.backButton.configure(font=font10)
        self.backButton.configure(foreground="#000000")
        self.backButton.configure(highlightbackground="#d9d9d9")
        self.backButton.configure(highlightcolor="black")
        self.backButton.configure(pady="0")
        self.backButton.configure(text='''BACK''')

        rows = dbo.search_book(key)
        if rows == 0:
            tkmsg.showerror(title="NOT FOUND", message="BOOK NOT AVAILABLE IN LIBRARY!")
        else:
            for row in rows:
                self.Scrolledtreeview1.insert("", 'end', text='', value=row)





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


#if __name__ == '__main__':
#    vp_start_gui()



