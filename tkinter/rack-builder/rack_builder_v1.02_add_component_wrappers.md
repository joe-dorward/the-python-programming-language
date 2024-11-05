This version adds the `switches_wrapper`, the `controllers_wrapper`, and the `disk_shelves_wrapper`.

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program rack_builder_v1.02_add_component_wrappers.py
# Written by: Joe Dorward
# Started: 08/10/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# rack_builder_v1.02_add_component_wrappers
# * adds the switches_wrapper
# * adds the controllers_wrapper
# * adds the disk_shelves_wrapper

from tkinter import Tk, Menu, Frame, Label

# ========== ========== ========== ========== ========== ========== ========== ==========
# the offsets are the horizontal and vertical spacing between widgets
x_offset = 2
y_offset = 2

# since 'generic components' are the fundamental objects in the user interface, their width
# and height are the fundemental units of the user interface - the widths and heights of
# every other object in the user interface is calculated from them

generic_component_width = 150
generic_component_height = 13

# UNITS ---------- ---------- ---------- ---------- ----------
# 'unit numbers' are square
unit_font = ('Arial',5,'normal')
unit_number_width = generic_component_height
unit_number_height = generic_component_height

# 'units' are the same size as 'generic components'
unit_width = generic_component_width
unit_height = generic_component_height

# RACKS ---------- ---------- ---------- ---------- ----------
# rack width accommodates a 'unit number' and a 'unit'
# rack height accommodates 42 'units'
rack_label_font = ('Arial',8,'normal')
rack_label_height = 20
rack_width = unit_number_width + unit_width + (3 * x_offset)
rack_height = (unit_height * 42) + (43 * y_offset) + rack_label_height

# GENERIC WRAPPER HEIGHT ---------- ---------- ---------- ---------- ----------
# the 'rack height' defines the height of the 'generic wrapper height'
generic_wrapper_height = rack_height + (2 * x_offset)

tabs_wrapper_height = generic_wrapper_height
components_wrapper_height = generic_wrapper_height
racks_wrapper_height = generic_wrapper_height

# the height of the user interface is calculated from the 'generic wrapper height'
ui_left = x_offset
ui_top = y_offset
ui_height = generic_wrapper_height + (2 * x_offset)
ui_width = (ui_height / 9) * 16 # calculate 16:9 proportional width

# TABS WRAPPER ---------- ---------- ---------- ---------- ----------
tabs_wrapper_left = x_offset
tabs_wrapper_width = ui_width / 3

# COMPONENTS WRAPPER ---------- ---------- ---------- ---------- ----------
component_font = ('Arial',7,'normal')

# inner wrapper (x3)
component_wrapper_label_height = 20
component_wrapper_width = generic_component_width + (2 * x_offset)
component_wrapper_height = int(((components_wrapper_height - component_wrapper_label_height) - (4 * y_offset)) / 3) - 1
print(int(component_wrapper_height))

# outer wrapper (x1)
components_wrapper_label_height = 24
components_wrapper_left = tabs_wrapper_left + tabs_wrapper_width + x_offset
components_wrapper_width = component_wrapper_width + (2 * x_offset)

# switches wrapper
switches_wrapper_width = component_wrapper_width
switches_wrapper_top = components_wrapper_label_height + y_offset

# controllers wrapper
controllers_wrapper_top = switches_wrapper_top + component_wrapper_height + y_offset

# disk shelves wrapper
disk_shelves_wrapper_top = controllers_wrapper_top + component_wrapper_height + y_offset

# RACKS WRAPPER ---------- ---------- ---------- ---------- ----------
racks_wrapper_left = components_wrapper_left + components_wrapper_width + x_offset
racks_wrapper_width = ui_width - tabs_wrapper_width - components_wrapper_width - (4 * x_offset)

# ========== ========== ========== ========== ========== ========== ========== ==========
# MENUBAR
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Menubar():
    # adds menubar_1
    print("[DEBUG] add_Menubar() called")

    menubar_1 = Menu(ui, name='menubar_1')

    # ---------- ---------- ---------- ---------- ---------- 
    # add file_menu to menubar_1
    file_menu = Menu(menubar_1, name='file_menu')
    menubar_1.add_cascade(menu=file_menu, label='File')
    
    # add options to file_menu
    file_menu.add_command(label='Quit', command=ui.quit)    
    # ---------- ---------- ---------- ---------- ---------- 

    # show menubar_1 in UI
    ui['menu'] = menubar_1
# ========== ========== ========== ========== ========== ========== ========== ==========
# TABS WRAPPER
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Tabs_Wrapper():
    # adds the tabs_wrapper 
    print("[DEBUG] add_Tabs_Wrapper() called")
   
    global tabs_wrapper
    tabs_wrapper = Frame(ui,
                         background='Gray',
                         name='tabs_wrapper')
    
    tabs_wrapper.place(x=tabs_wrapper_left,
                       y=y_offset,
                       width=tabs_wrapper_width,
                       height=tabs_wrapper_height)
# ========== ========== ========== ========== ========== ========== ========== ==========
# COMPONENTS WRAPPER
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Components_Wrapper():
    # adds the wrapper 'Frame' widgets
    print("[DEBUG] add_Components_Wrapper() called")

    global components_wrapper
    components_wrapper = Frame(ui,
                               background='Gray',
                               name='components_wrapper')
    
    components_wrapper.place(x=components_wrapper_left,
                             y=y_offset, 
                             width=components_wrapper_width, 
                             height=components_wrapper_height)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Components_Wrapper_Label(parent_widget):
    # adds components_wrapper_label
    print("[DEBUG] add_Components_Wrapper_Label() called")

    components_wrapper_label = Label(components_wrapper,
                                     background='DarkGray',
                                     foreground='white', 
                                     text='Components',
                                     name='components_wrapper_label')
    
    components_wrapper_label.place(x=0,
                                   y=0,
                                   width=components_wrapper_width,
                                   height=components_wrapper_label_height)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Controllers_Wrapper(parent_widget):
    # add controller_wrapper
    print("[DEBUG] add_Controller_Wrapper() called")

    # add controllers_wrapper
    controllers_wrapper = Frame(parent_widget, background='Lavender', name='controller_wrapper')
    controllers_wrapper.place(x=x_offset,
                              y=controllers_wrapper_top,
                              width=component_wrapper_width,
                              height=component_wrapper_height)

    # add controller_wrapper_label
    controllers_wrapper_label = Label(controllers_wrapper,
                                      text='Controllers',
                                      background='Lavender',
                                      foreground='gray')
    
    controllers_wrapper_label.place(x=0,
                                    y=0,
                                    width=component_wrapper_width,
                                    height=component_wrapper_label_height)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Switches_Wrapper(parent_widget):
    # add switches_wrapper
    print("[DEBUG] add_Switches_Wrapper() called")

    # add switches_wrapper
    switches_wrapper = Frame(parent_widget, background='Honeydew', name='switches_wrapper')
    switches_wrapper.place(x=x_offset,
                           y=switches_wrapper_top,
                           width=component_wrapper_width,
                           height=component_wrapper_height)

    # add switches_wrapper_label
    switches_wrapper_label = Label(switches_wrapper,
                                   text='Switches',
                                   background='Honeydew',
                                   foreground='gray')
    
    switches_wrapper_label.place(x=0,
                                 y=0,
                                 width=component_wrapper_width,
                                 height=component_wrapper_label_height)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Disk_Shelves_Wrapper(parent_widget):
    # add disk_shelves_wrapper
    print("[DEBUG] add_Disk_Shelves_Wrapper() called")

    # add disk_shelves_wrapper
    disk_shelves_wrapper = Frame(parent_widget,
                                 background='Cornsilk',
                                 name='disk_shelves_wrapper')
    
    disk_shelves_wrapper.place(x=x_offset,
                               y=disk_shelves_wrapper_top,
                               width=component_wrapper_width,
                               height=component_wrapper_height)

    # add disk_shelves_wrapper_label
    disk_shelves_wrapper_label = Label(disk_shelves_wrapper,
                                       text='Disk Shelves',
                                       background='Cornsilk',
                                       foreground='gray')
    
    disk_shelves_wrapper_label.place(x=0,
                                     y=0,
                                     width=component_wrapper_width,
                                     height=component_wrapper_label_height)
# ========== ========== ========== ========== ========== ========== ========== ==========
# RACKS WRAPPER
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Racks_Wrapper():
    # adds the racks_wrapper
    print("[DEBUG] add_Racks_Wrapper() called")

    global racks_wrapper
    racks_wrapper = Frame(ui,
                          background='Gray',
                          name='racks_wrapper')
    
    racks_wrapper.place(x=racks_wrapper_left,
                        y=y_offset,
                        width=racks_wrapper_width,
                        height=racks_wrapper_height)
# ========== ========== ========== ========== ========== ========== ========== ==========
# UTILLITY FUNCTIONS
# ========== ========== ========== ========== ========== ========== ========== ==========
def list_Child_Widgets(parent_widget):
    # lists the child-widgets of a parent-widget
    print("[DEBUG] list_Child_Widgets() called")

    print("The child-widgets are:")
    for each_child in parent_widget.winfo_children():
        print(" ",each_child.winfo_name())

# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("----------------------------------------------------")

    # create the 'blank' UI window
    ui = Tk()
    ui.title("Rack Builder")
    ui.geometry('%dx%d+%d+%d' % (ui_width, ui_height, ui_left, ui_top))
    ui.wm_resizable(width=False, height=False)
    ui.option_add('*tearOff', False)

    # add controls
    add_Menubar()
    add_Tabs_Wrapper()
    add_Components_Wrapper()
    add_Components_Wrapper_Label(components_wrapper)
    #list_Child_Widgets(ui)

    add_Switches_Wrapper(components_wrapper)
    add_Controllers_Wrapper(components_wrapper)
    add_Disk_Shelves_Wrapper(components_wrapper)

    add_Racks_Wrapper()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
