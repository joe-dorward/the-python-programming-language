**[DISCLAIMER]** I am *NOT* sure that any of the following is *CORRECT* - but it works for me.

On my computer, that path to my 'parent' Python folder is:
```Console
C:\Users\Joe\Documents\My Programming\Python
```

**`packages` folder**
Below my 'parent' Python folder, is a `packages` folder, where I have decided to start
adding generically useful methods - this is how that folder (a time of writing) looks.

<p alt="packages folder" align="center"><img src="illustrations/packages.png" /></p>

**`__init__.py` file**
This is my `__init__.py file
```Python
print("\n====================================================")
print("[PACKAGES] __init__.py called")

from . file_system import print_file_system_heartbeat, get_fullpath_to_selected_file

from . print_xml import print_Structure, print_Values, print_xml_heartbeat
```

**`file_system.py` file**
This is my `file_system.py` file
```Python
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Module file_system.py
# Written by: Joe Dorward
# Started: 14/12/2024

from tkinter import filedialog as filedialog_1
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def print_file_system_heartbeat():
    print("[TESTING] print_file_system_heartbeat() called")
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def get_fullpath_to_selected_file(file_type, initial_dir):
    # returns the fullpath of the selected file
    # filtered by file_type - for example 'xml'

    fullpath_to_selected_file =  filedialog_1.askopenfilename(
        title='Select File',
        initialdir=initial_dir,
        filetypes=(
            (file_type.upper() + ' files', '*.' + file_type),
            ('All other files', '*.*')
        )
    )
    return fullpath_to_selected_file
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
```
