This version adds the `rack_dictionary`, and reads the XML rack-data from the Sales Order into it.
It also adds the 'Rack' menu, and its 'Add Racks' option.

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program rack_builder_v1.03_add_racks.py
# Written by: Joe Dorward
# Started: 08/10/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# rack_builder_v1.03_add_racks
# * adds the import reference to 'os'
# * adds the import reference to 'xml.dom.minidom'
# * adds the rack_dictionary
# * gets the rack data
# * adds the 'Rack' menu
# * adds the 'Add Racks' option to the 'Rack' menu

from tkinter import Tk, Menu, Frame, Label
import os
import xml.dom.minidom

rack_dictionary = {}
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
# UTILLITY FUNCTIONS
# ========== ========== ========== ========== ========== ========== ========== ==========
def list_Child_Widgets(parent_widget):
    # lists the child-widgets of a parent-widget
    print("[DEBUG] list_Child_Widgets() called")

    print("The child-widgets are:")
    for each_child in parent_widget.winfo_children():
        print(" ",each_child.winfo_name())
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def get_Node_Text(node):
    # returns node-name (if first-character of the node-value is the return-character)
    # returns node-value (if first-character of the node-value is NOT the return-character)

    if ord(node.firstChild.nodeValue[0]) == 10:
        return node.nodeName
    else:
        return node.firstChild.nodeValue
# ========== ========== ========== ========== ========== ========== ========== ==========
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
    
    # ---------- ---------- ---------- ---------- ----------
    # add 'Racks' menu
    racks_menu = Menu(menubar_1)
    menubar_1.add_cascade(menu=racks_menu, label='Racks')
    racks_menu.add_command(label='Add Racks', command=add_Racks)
    # ---------- ---------- ---------- ---------- ----------

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
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def get_Rack_Data():
    # gets rack-data from sales_order
    print("[DEBUG] get_Rack_Data() called")

    # get path to file
    path_to_file = os.getcwd() + "\\sales_order_01.xml"

    # parse file
    sales_order = xml.dom.minidom.parse(path_to_file)

    rack_list = sales_order.getElementsByTagName("rack")
    rack_counter = len(rack_list)
    #print("  There are {} racks:".format(rack_counter))

    for each_rack in rack_list:
        #print(each_rack.nodeName) # prints the node-name

        for each_data_item in each_rack.childNodes:
            if (each_data_item.nodeType == 1):
                
                if each_data_item.nodeName == 'identifier':
                    rack_identifier = get_Node_Text(each_data_item)

                elif each_data_item.nodeName == 'stencil':
                    rack_stencil = get_Node_Text(each_data_item)

                elif each_data_item.nodeName == 'name':
                    rack_name = get_Node_Text(each_data_item)

                elif each_data_item.nodeName == 'position':
                    rack_position = get_Node_Text(each_data_item)
                    
        rack_dictionary.update({rack_identifier: {'stencil':rack_stencil, 'name':rack_name, 'position':rack_position}})

    #print(rack_dictionary)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def list_Rack_Data():
    # lists rack-data
    print("[DEBUG] list_Rack_Data() called")

    print("  [FORMATTED]")
    for each_key, each_value in rack_dictionary.items():        
        print("    {}={}".format(each_key,each_value))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Racks():
    # add rack(s)
    print("[DEBUG] add_Racks() called")

    #global rack_height
    #rack_height = racks_wrapper_height - 4

    for each_key in rack_dictionary:
        rack_identifier = each_key
        rack_position = rack_dictionary[rack_identifier]['position']
        #print("  {}={}".format(rack_identifier,rack_dictionary[rack_identifier]['position']))
        #print("  {}={}".format(rack_identifier,rack_position))

        rack_name = rack_identifier.lower()
        rack_name = rack_name.replace(" ","_")
        rack_left = rack_width * (int(rack_position) - 1) + (2 * int(rack_position))

        # add the racks
        #this_rack = add_Rack(rack_left, rack_width, rack_height, rack_name)
        this_rack = add_Rack(rack_left, rack_name)
        add_Rack_Label(this_rack, rack_identifier, rack_name)
        add_Units(this_rack)

    #list_Child_Widgets(racks_wrapper)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Rack(rack_left, rack_name):
    # adds a rack
    print("  [DEBUG] add_Rack() called")

    rack = Frame(racks_wrapper, background='lightgray', name=rack_name)    
    rack.place(x=rack_left, y=2, width=rack_width, height=rack_height)

    return rack
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Rack_Label(rack, text, rack_name):
    # adds a rack label
    print("  [DEBUG] add_Rack_Label() called")

    # add rack_label
    rack_label_top = rack_height - rack_label_height
    rack_label = Label(rack,
                       background='white',
                       font=rack_label_font,
                       text=text,
                       name=rack_name + '_label')

    rack_label.place(x=0,
                     y=rack_label_top,
                     width=rack_width,
                     height=rack_label_height)
# ========== ========== ========== ========== ========== ========== ========== ==========
# UNITS
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Units(parent_widget):
    # adds the units to a rack
    print("  [DEBUG] add_Units() called")
    #print(parent_widget)
    #print(parent_widget.winfo_name() )

    for unit_counter in range(42):

        unit_top = rack_height - 35 - (unit_counter * unit_height) - (unit_counter * 2)

        # add unit-numbers
        unit_number_name = parent_widget.winfo_name() + '_unit_' + str(unit_counter + 1) + '_number'
        unit_number_text = str(unit_counter + 1)

        unit_number = Label(parent_widget,
                            background='white',
                            text=unit_number_text,
                            font=unit_font,
                            name=unit_number_name)
        
        unit_number.place(x=2,
                          y=unit_top,
                          width=unit_number_width,
                          height=unit_number_height)

        # add units
        unit_left = unit_number_width + 4
        unit_name = parent_widget.winfo_name() + '_unit_' + str(unit_counter + 1)

        unit = Label(parent_widget,background='white', name=unit_name)
        unit.place(x=unit_left, y=unit_top, width=unit_width, height=unit_height)
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
    get_Rack_Data()
    #list_Rack_Data()
    #add_Racks()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
