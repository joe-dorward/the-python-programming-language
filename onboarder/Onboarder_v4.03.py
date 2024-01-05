# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program Onboarder_v4.03.py
# Written by: Joe Dorward
# Started: 05/01/2024

# This program:
# * creates the Onboarder User Interface
# * adds PATH and INFORMATION labels
# * adds the QUIT button
# v4.2
# * adds the 'Create Team Folder' button
# v4.3
# * adds the methods to create generic pseudo-content TOPIC files
# * adds the 'Create Psuedo Content' button

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

    Information = Information + "\n    2. Click the [Create Pseudo Content] button - some generic"
    Information = Information + " pseudo-content files will be added to the 'Team' folder"

    Onboarder_Information.config(text=Information)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Quit_Button():
    # adds the [Quit] button
    print("[DEBUG] Add_Quit_Button() called")

    LEFT = CONST.X_OFFSET
    TOP = CONST.ONBOARDER_HEIGHT - CONST.BUTTON_HEIGHT - CONST.Y_OFFSET

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
def Get_Topic_Header(filename,title):
    # gets the Topic 'header' XML
    print("[DEBUG] > Get_Topic_Header() called")

    Header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    Header = Header + "\n<!DOCTYPE topic PUBLIC \"-//OASIS//DTD DITA Topic//EN\" \"topic.dtd\">"
    Header = Header + "\n<topic id=\"" + filename + "\">"
    Header = Header + "\n <title>" + title + "</title>"
    Header = Header + "\n <body>"

    return(Header)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_Topic_Content():
    # gets the Topic 'content'
    print("[DEBUG] > Get_Topic_Footer() called")

    Content = "\n<p>Because of the simple nature of the aplication that"
    Content = Content + " created this file, this content can only be generic.</p>"

    return(Content)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_Topic_Footer():
    # gets the Topic 'footer' XML
    print("[DEBUG] > Get_Topic_Footer() called")

    Footer = "\n </body>"
    Footer = Footer + "\n</topic>"

    return(Footer)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Create_Topic(Title):
    # creates a Topic file
    print("[DEBUG] Create_Topic() called")

    TopicFilename = Title.lower()
    TopicFilename = TopicFilename.replace(" ","_")
    TopicFilename = "t_" + TopicFilename + ".dita"
    PathToTopicFile = os.getcwd() + "\\Team\\" + TopicFilename

    print("[DEBUG] > Creating",TopicFilename)

    # create topic file
    TopicFile = os.open(PathToTopicFile, os.O_CREAT|os.O_RDWR)
    TopicFile_Handle = os.fdopen(TopicFile,"w+")

    TopicFile_Handle.write(Get_Topic_Header(TopicFilename,Title))
    TopicFile_Handle.write(Get_Topic_Content())
    TopicFile_Handle.write(Get_Topic_Footer())

    TopicFile_Handle.close()
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Create_PseudoContent_Button():
    # adds the [Create Pseudo Content] button
    print("\n[DEBUG] Add_Create_PseudoContent_Button() called")
  
    LEFT = CONST.X_OFFSET
    TOP = CONST.CONTROLS_TOP + CONST.BUTTON_HEIGHT + CONST.Y_OFFSET

    Create_PseudoContent_Button = Button(Onboarder,text="Create Pseudo Content",command=Create_PseudoContent)
    Create_PseudoContent_Button.place(x=LEFT,y=TOP, width=CONST.BUTTON_WIDTH)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Create_PseudoContent():
    # create pseudo content files
    print("\n[DEBUG] Create_PseudoContent() called")

    # build expected path to 'Team' folder
    path_to_team_folder = os.getcwd() + "\\Team"

    if os.path.exists(path_to_team_folder):
        print("[DEBUG] > Creating pseudo content files")
        Create_Topic("Team Policy")        
        Create_Topic("Team Procedures")        
        Create_Topic("Useful Links")
        Create_Topic("How to do this")
        Create_Topic("How to do that")
    else:
        print("[DEBUG] > 'Team' folder DOES NOT exist")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------


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

Add_Create_PseudoContent_Button()

Onboarder.mainloop()
print("----------------------------------------------------\n")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
