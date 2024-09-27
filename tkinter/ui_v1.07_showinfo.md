Continuing the exploration of using Tkinter with Python, this version adds
the functionality to to raise a 'showinfo' messagebox.

[!ui_v1.07_showinfo.py](illustrations/ui_v1.07_showinfo.png)

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.07_showinfo.py
# Written by: Joe Dorward
# Started: 27/09/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# ui_v1.07_showinfo
# * adds the import reference to 'messagebox' 
# * adds showinfo_1
# * adds messagebox_menu to menubar_1
# * adds show_Info option to messagebox_menu
# * adds handler (method) to handle the show_Info option

from tkinter import Tk, Menu, messagebox as showinfo_1

# position the UI window
ui_top = 10
ui_left = 10

# set UI window proportions to 16:9
ui_width = 16 * 20
ui_height = 9 * 20
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Menubar():
    # adds menubar_1
    print("[DEBUG] Add_Menubar() called")

    menubar_1 = Menu(ui)

    # add 'File' menu
    file_menu = Menu(menubar_1)
    menubar_1.add_cascade(menu=file_menu, label='File')
    file_menu.add_command(label='Quit', command=ui.quit)

    # add 'messagebox' menu
    messagebox_menu = Menu(menubar_1)
    menubar_1.add_cascade(menu=messagebox_menu, label='Messagebox')
    messagebox_menu.add_command(label='Show Info', command=show_Info)

    # show menubar_1 in UI
    ui['menu'] = menubar_1
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def show_Info():
    # raises the showinfo_1 messagebox
    print("[DEBUG] show_Info() called")

    response = showinfo_1.showinfo(title="Show Info", message="This is the 'showinfo' messagebox")
    print("The value of `response' is: `{}'".format(response))
# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("----------------------------------------------------")

    # create the 'blank' UI window
    ui = Tk()
    ui.title("UI")
    ui.config(background='lightgray')
    ui.geometry('%dx%d+%d+%d' % (ui_width, ui_height, ui_left, ui_top))
    ui.wm_resizable(width=False, height=False)
    ui.option_add('*tearOff', False)

    # add controls
    add_Menubar()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
