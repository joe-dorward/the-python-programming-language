Continuing the exploration of using Tkinter with Python, this version includes
the exploration of the tkinter 'widget' hierarchy from the *parent* to *grandchild*,
while adding the use of the `nametowidget()` method.

||||
|-|-|-|
|![ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue.py](illustrations/ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue_one.png)|![ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue.py](illustrations/ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue_two.png)|![ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue.py](illustrations/ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue_three.png)|

**Steps**

1. From the `Labels` menu, select the `Add (Honeydew to ui)` option
2. From the `nametowidget()` menu, select the `Show (label_1)` option - the `name_To_Widget()` method will run and the Console will display:

```Console
[DEBUG] name_To_Widget(label_1) called
  parent-name='tk' <- 'master' is the equivalent of 'parent of'
  widget-name='label_1' <- the 'name' of the widget
  widget-path='.label_1' <- the 'dot' is the parent-node of the path
```

```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue.py
# Written by: Joe Dorward
# Started: 01/12/2024

# This program creates a Tkinter user interface
# * adds the import reference to 'Tk'
# ui_v1.33_nametowidget_grandchild_honeydew_and_aliceblue
# * adds the import reference to 'Label'
# * adds the 'Labels' menu
# * adds label adding options to the 'Labels' menu
# * adds handler (methods) for those label adding options

from tkinter import Tk, Menu, Label

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
    file_menu.add_command(label='Quit', command=parent_widget.quit)    
    # ---------- ---------- ---------- ---------- ----------
    # add labels_menu to menubar_1
    labels_menu = Menu(menubar_1, name='labels_menu')
    menubar_1.add_cascade(menu=labels_menu, label='Labels')
    
    # add options
    labels_menu.add_command(label='Add (Honeydew to ui)',
                            command=lambda:add_Honeydew(parent_widget))
    labels_menu.add_command(label='Add (Sub Labels to Honeydew)',
                            command=lambda:add_Sub_Labels(honeydew))
    
    labels_menu.add_command(label='Add (Aliceblue to ui)',
                            command=lambda:add_Aliceblue(parent_widget))
    labels_menu.add_command(label='Add (Sub Labels to Aliceblue)',
                            command=lambda:add_Sub_Labels(aliceblue))
    # ---------- ---------- ---------- ---------- ----------
    # add nametowidget_menu to menubar_1
    nametowidget_menu = Menu(menubar_1, name='nametowidget_menu')
    menubar_1.add_cascade(menu=nametowidget_menu, label='nametowidget()')

    nametowidget_menu.add_command(label='Show (label_1)',
                                  command=lambda:name_To_Widget(parent_widget, 'label_1'))
    
    nametowidget_menu.add_command(label='Show (label_1.sub_label_1)',
                                  command=lambda:name_To_Widget(parent_widget, 'label_1.sub_label_1'))

    # show menubar_1 in UI
    parent_widget['menu'] = menubar_1
# ========== ========== ========== ========== ========== ========== ========== ==========
# LABELS
# ========== ========== ========== ========== ========== ========== ========== ==========
def add_Honeydew(parent_widget):

    global honeydew
    honeydew = Label(parent_widget,
                     background='Honeydew',
                     foreground='Forestgreen',
                     text='label_1',
                     anchor='n',
                     name='label_1')    
    honeydew.place(x=10, y=10, width=102, height=95)

    list_Widgets(ui)
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Aliceblue(parent_widget):

    global aliceblue
    aliceblue = Label(parent_widget,
                     background='Aliceblue',
                     foreground='Cornflowerblue',
                     text='label_2',
                     anchor='n',
                     name='label_2')    
    aliceblue.place(x=122, y=10, width=102, height=95)

    list_Widgets(ui)
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def add_Sub_Labels(parent_widget):

    forestgreen = Label(parent_widget,
                    background='Forestgreen',
                    foreground='Honeydew',
                    text='sub_label_1',
                    anchor='n',
                    name='sub_label_1')    
    forestgreen.place(x=10, y=30, width=80)

    cornflowerblue = Label(parent_widget,
                        background='Cornflowerblue',
                        foreground='Aliceblue',
                        text='sub_label_2',
                        anchor='n',
                        name='sub_label_2')
    cornflowerblue.place(x=10, y=60, width=80)

    list_Widgets(ui)
# ========== ========== ========== ========== ========== ========== ========== ==========
# UTILLITY METHODS
# ========== ========== ========== ========== ========== ========== ========== ==========
def list_Widgets(parent_widget):
    # lists widgets
    print("----------------------------------------------------")
    print("[DEBUG] list_Widgets() called")

    # parent-widget
    print("\nParent:")
    print("  parent-name='{}' <- the 'name' of the user interface"\
          .format(parent_widget.winfo_name()))
    print("  parent-title='{}' <- the 'title' of the user interface"\
          .format(parent_widget.title()))
    print("  parent-path='{}' <- the 'dot' is the parent-node of the path"\
          .format(parent_widget))

    # child-widgets
    for each_child in parent_widget.winfo_children():
        print("\n  Child:")

        print("    parent-name='{}' <- 'master' is the equivalent of 'parent of'"\
              .format(each_child.master.winfo_name()))
        print("    child-name='{}' <- the 'name' of a child"\
              .format(each_child.winfo_name()))
        print("    child-path='{}' <- the 'dot + name' is a child"\
              .format(each_child))

        # grandchild-widgets
        print("\n    Grandchild:")
        for each_grandchild in each_child.winfo_children():
            print("\n      parent-name='{}' <- 'master' is the equivalent of 'parent of'"\
                  .format(each_grandchild.master.winfo_name()))
            print("      grandchild-name='{}' <- the 'name' of a grandchild"\
                  .format(each_grandchild.winfo_name()))
            print("      grandchild-path='{}' <- adding a 'dot + name' for a grandchild path\n"\
                  .format(each_grandchild))
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def name_To_Widget(parent_widget, name):
    # gets a widget from a name (path)
    print("----------------------------------------------------")
    print("[DEBUG] name_To_Widget({}) called".format(name))

    # get the_widget
    the_widget = parent_widget.nametowidget(name)

    print("  parent-name='{}' <- 'master' is the equivalent of 'parent of'"\
          .format(the_widget.master.winfo_name()))
    
    print("  widget-name='{}' <- the 'name' of the widget"\
          .format(the_widget.winfo_name()))

    print("  widget-path='{}' <- the 'dot' is the parent-node of the path"\
          .format(the_widget))

    # uppercase the label text
    the_widget['text'] = the_widget['text'].upper()
# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':        
    print("----------------------------------------------------")

    # create the 'blank' tkinter user interface
    ui = Tk()
    ui.title("ui")

    # set default ui position
    ui_left = 10
    ui_top = 10

    # set user interface proportions to 16:9
    ui_width = 16 * 25
    ui_height = 9 * 25
    ui.geometry('%dx%d+%d+%d' % (ui_width, ui_height, ui_left, ui_top))
    ui.config(background='lightgray')
    ui.wm_resizable(width=False, height=False)
    ui.option_add('*tearOff', False)

    add_Menubar(ui)

    ui.mainloop()
    print("----------------------------------------------------\n")
```
