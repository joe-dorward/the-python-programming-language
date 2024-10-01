Continuing the exploration of using Tkinter with Python, this version adds
'LabelFrame' widgets with their 'relief' attribute set to 'groove'.
Since 'groove' is the default-relief, specifying it is unnecessary.

The second example has its 'highlightthickness' attribute set to '8'.

![ui_v1.12_groove_labelframes.py](illustrations/ui_v1.12_groove_labelframes.png)

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.12_groove_labelframes.py
# Written by: Joe Dorward
# Started: 01/10/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# ui_v1.12_groove_labelframes
# * adds the import reference to 'LabelFrame'

from tkinter import Tk, Menu, LabelFrame

# position the UI window
ui_top = 10
ui_left = 10

# set UI window proportions to 16:9
ui_width = 16 * 22
ui_height = 9 * 22
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Menubar():
    # adds menubar_1
    print("[DEBUG] add_Menubar() called")

    menubar_1 = Menu(ui)

    # ---------- ---------- ---------- ---------- ---------- 
    # add file_menu to menubar_1
    file_menu = Menu(menubar_1)
    menubar_1.add_cascade(menu=file_menu, label='File')
    
    # add options to file_menu
    file_menu.add_command(label='Quit', command=ui.quit)    
    # ---------- ---------- ---------- ---------- ---------- 

    # show menubar_1 in UI
    ui['menu'] = menubar_1
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Groove_LabelFrame():
    # adds 'groove' frames
    print("[DEBUG] add_Groove_LabelFrame() called")

    x_offset = 10
    y_offset = 10

    frame_width = 16 * 10
    frame_height = 9 * 10
    # ---------- ---------- ---------- ---------- ---------- 
    # groove_labelframe_1
    frame_left = x_offset
    frame_top = y_offset

    groove_labelframe_1 = LabelFrame(ui,
                                     text='groove',
                                     relief='groove',
                                     name="groove_labelframe_1")
    
    groove_labelframe_1.place(x=frame_left,
                              y=frame_top,
                              width=frame_width,
                              height=frame_height)
    # ---------- ---------- ---------- ---------- ---------- 
    # groove_labelframe_2
    frame_left = (2 * x_offset) + frame_width

    groove_labelframe_2 = LabelFrame(ui,
                                     text='groove',
                                     relief='groove',
                                     highlightthickness=8,
                                     name="groove_labelframe_2")
    
    groove_labelframe_2.place(x=frame_left,
                              y=frame_top,
                              width=frame_width,
                              height=frame_height)
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
    add_Groove_LabelFrame()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
