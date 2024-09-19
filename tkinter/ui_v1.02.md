I'm digging more deeply into the use of the Tkinter package (it comes with Python) to create Python applications with 'proper' user interfaces. If you have (or can get) Python installed, you can follow along at home. 
 
Just copy-n-paste each version of the self-contained application as I go, and have fun!
 
This version, adds the **File** menu.

![ui_v1.02](illustrations/ui_v1.02.png)

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.02_menubar.py
# Written by: Joe Dorward
# Started: 18/09/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# * adds the 'File' menu
# * adds 'Option 1' to the 'File' menu
# * adds the stub_Handler (method) for 'Option 1'
# * adds 'Quit' option to the 'File' menu

from tkinter import Tk, Menu

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
    file_menu_option = Menu(menubar_1)
    menubar_1.add_cascade(menu=file_menu_option, label='File')

    # add options to 'File' menu
    file_menu_option.add_command(label='Option 1', command=stub_Handler)
    file_menu_option.add_command(label='Quit', command=ui.quit)

    # show menubar_1 in UI
    ui['menu'] = menubar_1
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def stub_Handler():
    # handles any event
    print("[DEBUG] stub_Handler() called")

# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("----------------------------------------------------")

    # create the 'blank' UI window
    ui = Tk()
    ui.title("UI")
    ui.geometry('%dx%d+%d+%d' % (ui_width, ui_height, ui_left, ui_top))
    ui.option_add('*tearOff', False)

    # add controls
    add_Menubar()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
