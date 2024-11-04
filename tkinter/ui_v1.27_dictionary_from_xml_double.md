Continuing the exploration of using Tkinter with Python, this version
is a digression into reading XML data from a file and adding it to a
Python **Dictionary**.

```xml
<?xml version='1.0'?>
<racks>
  <rack>
    <identifier>Rack 1</identifier>
    <stencil>NetApp-Cabinets.vss</stencil>
    <name>42U Cabinet</name>
    <position>1</position>
  </rack>
  <rack>
    <identifier>Rack 2</identifier>
    <stencil>NetApp-Cabinets.vss</stencil>
    <name>42U Cabinet</name>
    <position>2</position>
  </rack>
  <rack>
    <identifier>Rack 3</identifier>
    <stencil>NetApp-Cabinets.vss</stencil>
    <name>42U Cabinet</name>
    <position>4</position>
  </rack>
</racks>
```

This version uses the value of `identifier` as the unique-key for the Python dictionary.
It then prints its contents in both [RAW] (manually re-formatted for space and clarity) and [FORMATTED] forms.

```python
[RAW] {
        'Rack 1': {'name': '42U Cabinet', 'position': '1'},
        'Rack 2': {'name': '42U Cabinet', 'position': '2'},
        'Rack 3': {'name': '42U Cabinet', 'position': '4'}
      }
```

```Python
[FORMATTED]
  Rack 1:
    name=42U Cabinet
    position=1
  Rack 2:
    name=42U Cabinet
    position=2
  Rack 3:
    name=42U Cabinet
    position=4
```

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.27_dictionary_from_xml_double.py
# Written by: Joe Dorward
# Started: 03/11/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# ui_v1.27_dictionary_from_xml_double
# * reads two-dimension XML rack-data from a file, and
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
    path_to_file = os.getcwd() + "\\xml\\racks_01.xml"

    # parse file
    inventory = xml.dom.minidom.parse(path_to_file)

    # get the 'rack' nodes
    rack_list = inventory.getElementsByTagName("rack")
    print("  The {} rack data-items are:".format(len(rack_list)))

    for each_rack in rack_list:
        #print(each_rack.nodeName) # prints the node-name

        for each_data_item in each_rack.childNodes:
            if (each_data_item.nodeType == 1):
                
                if each_data_item.nodeName == 'identifier':
                    identifier = get_Node_Text(each_data_item)

                elif each_data_item.nodeName == 'name':
                    name = get_Node_Text(each_data_item)

                elif each_data_item.nodeName == 'position':
                    position = get_Node_Text(each_data_item)
                    
        rack_dictionary.update({identifier: {'name':name, 'position':position}})
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def list_Rack_Data():
    # lists rack-data
    print("[DEBUG] list_Rack_Data() called")

    print("  [RAW] {}".format(rack_dictionary))

    print("  [FORMATTED]")
    for each_key, each_value in rack_dictionary.items():
        #print("    {}={}".format(each_key,each_value))
        print("    {}:".format(each_key))

        for each_sub_key in each_value:
            print("      {}={}".format(each_sub_key, each_value[each_sub_key]))
# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("\n----------------------------------------------------")

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
