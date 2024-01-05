# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program Onboarder_v4.02.py
# Written by: Joe Dorward
# Started: 05/01/2024

# This program:
# * creates the Onboarder User Interface
# * adds PATH and INFORMATION labels
# * adds the QUIT button
# v4.2
# * adds the 'Creat Team Folder' button

import CONST # CONSTANTS from CONST.py
from tkinter import Tk, Label, Button
import os # to get PATH information
# ---------- ---------- ---------- ----------

# ////////// ////////// ////////// ////////// ////////// ////////// ////////// //////////
def Add_Path_Label():
  # adds the path label
  print("[DEBUG] Add_Path_Label() called")

  Path_Label_Background = Label(Onboarder)
  Path_Label_Background.place(x=0,y=0,width=CONST.ONBOARDER_WIDTH)
  Path_Label_Background.config(background="#3F3F3F")

  Path_Label = Label(Onboarder)
  Path_Label.place(x=0,y=0)
  Path_Label_Text = os.getcwd()
  Path_Label.config(foreground="white",background="#3F3F3F",text=Path_Label_Text,justify='left')
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Information_Label():
    # adds the information label
    print("[DEBUG] Add_Information_Label() called")

    Onboarder_Information = Label(Onboarder)
    Onboarder_Information.place(x=CONST.X_OFFSET,y=CONST.Y_OFFSET + 20)
    Onboarder_Information.config(wraplength=CONST.INFORMATION_WRAP,justify='left',background="lightgray")

    Information = "This application is an exploration of this idea: the semi-automatic creation of "
    Information = Information + "onboarding documentation (as DITA XML files) for a new team member, with "
    Information = Information + "the implication that it could be adapted for any onboarding process. "
    Information = Information + "These DITA XML files, includes a Bookmap file, from which the output " 
    Information = Information + "(in any format) can be generated - think PDF or ePUB."

    Information = Information + "\n\nSTEPS:"
    Information = Information + "\n    1. Click the [Create Team Folder] button - a folder"
    Information = Information + " named 'Team' will be added to the path"

    Onboarder_Information.config(text=Information)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Quit_Button():
    # adds the [Quit] button
    print("[DEBUG] Add_Quit_Button() called")

    LEFT = CONST.X_OFFSET
    TOP = CONST.ONBOARDER_HEIGHT - CONST.BUTTON_HEIGHT - CONST.Y_OFFSET - 6

    Quit_Button = Button(Onboarder,text="Quit",command=Onboarder.quit)
    Quit_Button.place(x=LEFT,y=TOP,width=CONST.BUTTON_WIDTH)
# ////////// ////////// ////////// ////////// ////////// ////////// ////////// ////////// 
def Add_Create_TeamFolder_Button():
    # adds the [Create Team Folder] button
    print("\n[DEBUG] Add_Create_TeamFolder_Button() called")
  
    LEFT = CONST.X_OFFSET

    Create_TeamFolder_Button = Button(Onboarder,text="Create Team Folder",command=Create_TeamFolder)
    Create_TeamFolder_Button.place(x=LEFT,y=CONST.CONTROLS_TOP, width=CONST.BUTTON_WIDTH)
    Create_TeamFolder_Button.focus_set
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Create_TeamFolder():
    # creates the 'Team' folder
    print("[DEBUG] > Create_TeamFolder() called")

    # built expected path to 'Team' folder
    path_to_team_folder = os.getcwd() + "\\Team"

    if os.path.exists(path_to_team_folder):
        print("[DEBUG] > 'Team' folder exists")
    else:
        print("[DEBUG] > 'Team' folder created")
        os.mkdir(path_to_team_folder)
# ////////// ////////// ////////// ////////// ////////// ////////// ////////// //////////
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
'__main__'
print("\n'__main__' called")
print("----------------------------------------------------")
Onboarder = Tk()
Onboarder.title("Onboarder " + CONST.VERSION)
Onboarder.config(background='lightgray')
Onboarder.geometry('%dx%d+%d+%d' % (CONST.ONBOARDER_WIDTH, CONST.ONBOARDER_HEIGHT, 10, 10))
Onboarder.wm_resizable(width=False,height=False)

Add_Path_Label()
Add_Information_Label()
Add_Quit_Button()

Add_Create_TeamFolder_Button()

Onboarder.mainloop()
print("----------------------------------------------------\n")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
