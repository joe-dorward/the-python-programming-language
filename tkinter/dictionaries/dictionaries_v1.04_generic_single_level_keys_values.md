Continuing the exploration of using Tkinter with Python, this version
continues the exploration of using Python *Dictionaries* for storing and
processing data.

This version demonstrates the simple use of the `keys()`, and `values()`
methods to generically process the **keys**, and **values** of dictionaries.
This version also demonstrates that the results of the `keys()`, and
`values()` methods can be subscriptable when 'cast' as a Python **List**.

**[DISCLAIMER]** Although the keys in this example are unique within the
dictionary, it *IS NOT* a 'good' example of a Python dictionary - the keys
in this example are as much data as the values are. 
```Python
compact_disk_dictionary = {
    'Flesh and Blood':'Roxy Music',
    'Hunky Dory':'David Bowie',
    'Rio':'Duran Duran',
    'Avalon':'Roxy Music'
}
```
When the `Print` > `Single` option is selected, the keys and values
in the dictionary are printed to the console.
```Console
There are: 4 keys:

  dict_keys(['Flesh & Blood', 'Hunky Dory', 'Rio', 'Avalon'])
    subscriptable when 'cast' as a List: Flesh & Blood

There are: 4 values:

  dict_values(['Roxy Music', 'David Bowie', 'Duran Duran', 'Roxy Music'])
    subscriptable when 'cast' as a List: Roxy Music
```

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program dictionaries_v1.04_generic_single_level_keys_values.py
# Written by: Joe Dorward
# Started: 12/12/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# dictionaries_v1.04_generic_single_level_keys_values
# * updates the handler (method) of the 'Single' option to use
#   the keys(), and values() methods

from tkinter import Tk, Menu

single_level_dictionary = {
    'Flesh & Blood':'Roxy Music',
    'Hunky Dory':'David Bowie',
    'Rio':'Duran Duran',
    'Avalon':'Roxy Music'
}
# ========== ========== ========== ========== ========== ========== ========== ==========
# MENUBAR
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Menubar(parent_widget):
    # adds menubar_1
    print("[DEBUG] add_Menubar() called")

    menubar_1 = Menu(parent_widget, name='menubar_1')

    # ---------- ---------- ---------- ---------- ---------- 
    # add file_menu to menubar_1
    file_menu = Menu(menubar_1, name='file_menu')
    menubar_1.add_cascade(menu=file_menu, label='File')
    
    # add options
    file_menu.add_command(label='Quit',
                          command=parent_widget.quit)
    # ---------- ---------- ---------- ---------- ----------
    # add 'Print' menu
    print_menu = Menu(menubar_1)
    menubar_1.add_cascade(menu=print_menu, label='Print')

    # add options
    print_menu.add_command(label='Single',
                           command=lambda:print_Dictionary_Single(single_level_dictionary))
    # ---------- ---------- ---------- ---------- ----------

    # show menubar_1 in the user interface
    parent_widget['menu'] = menubar_1
# ========== ========== ========== ========== ========== ========== ========== ==========
def print_Dictionary_Single(dictionary):
    # prints data from a single-dictionary
    print("[DEBUG] print_Dictionary_Single() called")

    print("\nThere are: {} keys:".format(len(dictionary)))    
    print("\n  {}".format(dictionary.keys()))
    print("    subscriptable when 'cast' as a List: {}".format(list(dictionary.keys())[0]))

    print("\nThere are: {} values:".format(len(dictionary)))  
    print("\n  {}".format(dictionary.values()))
    print("    subscriptable when 'cast' as a List: {}".format(list(dictionary.values())[0]))
# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("====================================================")

    ui_left = 10
    ui_top = 10

    # set UI window proportions to 16:9
    ui_width = 16 * 20
    ui_height = 9 * 20

    # create the 'blank' user interface
    ui = Tk()
    ui.title("Dictionaries")
    ui.geometry('%dx%d+%d+%d' % (ui_width, ui_height, ui_left, ui_top))
    ui.wm_resizable(width=False, height=False)
    ui.option_add('*tearOff', False)

    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
    # build the user interface
    add_Menubar(ui)

    print("The user interface is built!")
    print("----------------------------------------------------")
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------

    ui.mainloop()
```
