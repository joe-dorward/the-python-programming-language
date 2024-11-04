Continuing the exploration of using Tkinter with Python, this version
is a digression into reading XML data from a file and adding it to a
Python **Dictionary**.

```xml
<?xml version='1.0'?>
<racks>
  <rack>
    <identifier>Rack 1</identifier>
  </rack>
  <rack>
    <identifier>Rack 2</identifier>
  </rack>
  <rack>
    <identifier>Rack 3</identifier>
  </rack>
</racks>
```

Although a 'single-dimension' list of values (such as this) SHOULD be loaded into
a Python **List**, this example is *about* showing you how to load them into a
Python dictionary.

Since, Python dictionaries are a list of key-value pairs, where eack key MUST be
unique, this example generates its own unique-keys for the values.
It then prints its contents in both [RAW] and [FORMATTED] forms.

```
[RAW] {'unique_key_1': 'Rack 1', 'unique_key_2': 'Rack 2', 'unique_key_3': 'Rack 3'}
```

```
[FORMATTED]
  unique_key_1=Rack 1
  unique_key_2=Rack 2
  unique_key_3=Rack 3
```

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.27_dictionary_from_xml_one.py
# Written by: Joe Dorward
# Started: 03/11/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# ui_v1.27_dictionary_from_xml_one
# * adds the import reference to 'os'
# * adds the import reference to 'xml.dom.minidom'
# * reads one-dimension XML rack-data from a file, and
# * puts that rack-data into the rack_dictionary, then
# * list the contents of the rack_dictionary

from tkinter import Tk, Menu
import os
import xml.dom.minidom

# position the UI window
ui_top = 10
ui_left = 10

# set UI window proportions to 16:9
ui_width = 16 * 27
ui_height = 9 * 27

# global dictionary
rack_dictionary = {}
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
# UTILLITY FUNCTIONS
# ========== ========== ========== ========== ========== ========== ========== ==========
def get_Node_Text(node):
    # returns node-name (if first-character of the node-value is the return-character)
    # returns node-value (if first-character of the node-value is NOT the return-character)

    if ord(node.firstChild.nodeValue[0]) == 10:
        return node.nodeName
    else:
        return node.firstChild.nodeValue
# ========== ========== ========== ========== ========== ========== ========== ==========
def get_Rack_Data():
    # gets rack-data from sales_order
    print("[DEBUG] get_Rack_Data() called")

    # get path to file
    path_to_file = os.getcwd() + "\\xml\\racks_00.xml"

    # parse file
    inventory = xml.dom.minidom.parse(path_to_file)

    # get the 'rack' nodes
    rack_list = inventory.getElementsByTagName("rack")
    print("  The {} rack data-items are:".format(len(rack_list)))

    rack_counter = 0
    for each_rack in rack_list:
        #print(each_rack.nodeName) # prints the node-name

        for each_data_item in each_rack.childNodes:
            if (each_data_item.nodeType == 1):
                
                if each_data_item.nodeName == 'identifier':
                    # each dictionary item must have a unique-key if the XML nodes
                    # are not unique, a unique-key must be generated for each one
                    rack_counter = rack_counter + 1
                    unique_key = 'unique_key_' + str(rack_counter)

                    identifier = get_Node_Text(each_data_item)
                    print("    `identifier'={}".format(identifier))
                    rack_dictionary.update({unique_key:identifier})
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def list_Rack_Data():
    # lists rack-data
    print("[DEBUG] list_Rack_Data() called")

    print("  [RAW] {}".format(rack_dictionary))

    print("  [FORMATTED]")
    for each_key, each_value in rack_dictionary.items():
        print("    {}={}".format(each_key,each_value))
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
    get_Rack_Data()
    list_Rack_Data()

    ui.mainloop()
    print("----------------------------------------------------\n")
```
