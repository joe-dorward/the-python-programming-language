Continuing the exploration of using Tkinter with Python, this version
continues the exploration of using Python *Dictionaries* for storing and
processing data.

This version demonstrates the generic processing of a double-level /
doubly-nested dictionary with nested `for` loops.

```Python
double_level_dictionary = {
    '123-1234': { 'title':'Flesh + Blood', 'artist':'Roxy Music' },
    '123-1235': { 'title':'Hunky Dory', 'artist':'David Bowie' },
    '123-1236': { 'title':'Rio', 'artist':'Duran Duran' },
    '123-1237': { 'title':'Avalon', 'artist':'Roxy Music' }
}
```
When the `Print` > `Double (looping)` option is selected, the keys and values
in the dictionary are printed to the console.
```Console
There are: 4 items:

  for key=123-1234
    title=Flesh + Blood
    artist=Roxy Music

  for key=123-1235
    title=Hunky Dory
    artist=David Bowie

  for key=123-1236
    title=Rio
    artist=Duran Duran

  for key=123-1237
    title=Avalon
    artist=Roxy Music
```

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program dictionaries_v1.05_generic_double_level_looping.py
# Written by: Joe Dorward
# Started: 12/12/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# * adds the import reference to 'Menu'
# * adds the menubar_1
# dictionaries_v1.05_generic_double_level_looping
# * adds the hard-coded dictionary named 'two_level_dictionary'
# * adds the 'Double (looping)' option to the 'Print' menu
# * adds the handler (method) for the 'Double (looping)' option

from tkinter import Tk, Menu

double_level_dictionary = {
    '123-1234': { 'title':'Flesh + Blood', 'artist':'Roxy Music' },
    '123-1235': { 'title':'Hunky Dory', 'artist':'David Bowie' },
    '123-1236': { 'title':'Rio', 'artist':'Duran Duran' },
    '123-1237': { 'title':'Avalon', 'artist':'Roxy Music' }
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
    print_menu.add_command(label='Double (looping)',
                           command=lambda:print_Dictionary_Double(double_level_dictionary))
    # ---------- ---------- ---------- ---------- ----------

    # show menubar_1 in the user interface
    parent_widget['menu'] = menubar_1
# ========== ========== ========== ========== ========== ========== ========== ==========
def print_Dictionary_Double(dictionary):
    # prints data from a double-level dictionary
    print("[DEBUG] print_Dictionary_Double() called")

    print("\nThere are: {} items:".format(len(dictionary)))

    for each_key, each_key_data in dictionary.items():
        print("\n  for key={}".format(each_key))

        for each_sub_key in each_key_data:
            print("    {}={}".format(each_sub_key, each_key_data[each_sub_key]))
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
