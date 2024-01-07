# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program Onboarder_v4.06.py
# Written by: Joe Dorward
# Started: 07/01/2024

# This program:
# * creates the Onboarder User Interface
# * adds PATH and INFORMATION labels
# * adds the QUIT button
# v4.02
# * adds the 'Create Team Folder' button
# v4.03
# * adds the methods to create generic pseudo-content TOPIC files
# * adds the 'Create Psuedo Content' button 
# v4.04
# * adds the [Team Member] LabelFrame
# * adds the team-member Entry widgets & StringVar
# * adds the [Create Team File] button
# v4.05
# * adds the [Add Team Member] button
# v4.06
# * adds the [Onboarding Content] LabelFrame
# * adds the [List Onboarding Content] button

import CONST # CONSTANTS from CONST.py
from tkinter import Tk, Label, Button, LabelFrame, Entry, StringVar, Checkbutton, IntVar
import os # to get PATH information
import xml.dom.minidom
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

    Information = Information + "\n    As the first team member:"
    Information = Information + "\n    3. In the [Team Member] panel - enter your 'Name', 'Email',"
    Information = Information + " and 'Report To' information"

    Information = Information + "\n    4. Click the [Create Team File] button - this will create the"
    Information = Information + " 't_team.dita' file in the 'Team' folder, with your information"
    Information = Information + " in the first row of a '<simpletable>' element"

    Information = Information + "\n    To add a new team member:"
    Information = Information + "\n    5. Edit the 'Name', 'Email', and 'Reports To' information"
    Information = Information + "\n    6. Click the [Add Team Member] button - a new team member"
    Information = Information + " will be added to the 't_team.dita' file in the 'Team' folder"

    Information = Information + "\n    7. Click the [List Content Files] button - the list of pseudo"
    Information = Information + "-content files (in the 'Team' folder) will be shown. In this scenario,"
    Information = Information + " the 't_team.dita' file is mandatory, so it is"
    Information = Information + "\n        selected and cannot be de-selected"

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
    Create_TeamFolder_Button.place(x=LEFT,y=CONST.CONTROLS_TOP,width=CONST.BUTTON_WIDTH)
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
    Header = Header + "\n  <title>" + title + "</title>"
    Header = Header + "\n  <body>"

    return(Header)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_Topic_Content():
    # gets the Topic 'content'
    print("[DEBUG] > Get_Topic_Footer() called")

    Content = "\n    <p>Because of the simple nature of the aplication that"
    Content = Content + " created this file, this content can only be generic.</p>"

    return(Content)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_Topic_Footer():
    # gets the Topic 'footer' XML
    print("[DEBUG] > Get_Topic_Footer() called")

    Footer = "\n  </body>"
    Footer = Footer + "\n</topic>"

    return(Footer)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Create_Topic(Title,Topic_Content):
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
    TopicFile_Handle.write(Topic_Content)
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
        Create_Topic("Team Policy",Get_Topic_Content())
        Create_Topic("Team Procedures",Get_Topic_Content())
        Create_Topic("Useful Links",Get_Topic_Content())
        Create_Topic("How to do this",Get_Topic_Content())
        Create_Topic("How to do that",Get_Topic_Content())
    else:
        print("[DEBUG] > 'Team' folder DOES NOT exist")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# ADD TEAM MEMBER LABELFRAME ///// ////////// ////////// ////////// ////////// //////////
def Add_TeamMember_LableFrame():
    # adds the [Team Member] from the lableframe
    print("\n[DEBUG] Add_TeamMember_LableFrame() called")

    global Name_Variable, Email_Variable, Reports_Variable

    LEFT = CONST.BUTTON_WIDTH + (CONST.X_OFFSET * 2)
    TOP = CONST.CONTROLS_TOP

    # LableFrame Widget
    TeamMember_LabelFrame = LabelFrame(Onboarder,text=" Team Member ")
    TeamMember_LabelFrame.place(x=LEFT,y=TOP,width=CONST.TM_WIDTH, height=CONST.TM_HEIGHT)
    TeamMember_LabelFrame.config(borderwidth=2, background="lightgray")
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
    # Label Widgets
    Name_Label = Label(TeamMember_LabelFrame,text="Name:",background="lightgray")
    Name_Label.place(x=CONST.X_OFFSET,y=CONST.Y_OFFSET/2)
    Name_Label.config(justify='left')

    Email_Label = Label(TeamMember_LabelFrame,text="Email:",background="lightgray")
    Email_Label.place(x=CONST.X_OFFSET,y=CONST.Y_OFFSET/2 + 26)

    Reports_Label = Label(TeamMember_LabelFrame,text="Reports To:",background="lightgray")
    Reports_Label.place(x=CONST.X_OFFSET,y=CONST.Y_OFFSET/2 + 26 * 2)
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
    # Entry Widgets
    Name_Variable = StringVar(TeamMember_LabelFrame)
    Name_Variable.set("Joe Dorward")
    Name_Entry = Entry(TeamMember_LabelFrame, textvariable=Name_Variable)
    Name_Entry.place(x=CONST.TM_ENTRY_LEFT,y=CONST.Y_OFFSET/2 + 1,width=CONST.TM_ENTRY_WIDTH)

    Email_Variable = StringVar(TeamMember_LabelFrame)
    Email_Variable.set("joe.dorward@example.com")
    Email_Entry = Entry(TeamMember_LabelFrame, textvariable=Email_Variable)
    Email_Entry.place(x=CONST.TM_ENTRY_LEFT,y=CONST.Y_OFFSET/2 + 27,width=CONST.TM_ENTRY_WIDTH)

    Reports_Variable = StringVar(TeamMember_LabelFrame)
    Reports_Variable.set("Team Director")
    Reports_Entry = Entry(TeamMember_LabelFrame, textvariable=Reports_Variable)
    Reports_Entry.place(x=CONST.TM_ENTRY_LEFT,y=CONST.Y_OFFSET/2 + 53,width=CONST.TM_ENTRY_WIDTH)
    # ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
    TOP = CONST.TM_HEIGHT - CONST.BUTTON_HEIGHT - (CONST.Y_OFFSET * 2)
    Create_TeamFile_Button = Button(TeamMember_LabelFrame,text="Create Team File",command=Create_TeamFile)
    Create_TeamFile_Button.place(x=CONST.X_OFFSET,y=TOP, width=CONST.BUTTON_WIDTH)

    LEFT = (CONST.X_OFFSET * 2) + CONST.BUTTON_WIDTH
    Add_TeamMember_Button = Button(TeamMember_LabelFrame,text="Add Team Member",command=Add_TeamMember)
    Add_TeamMember_Button.place(x=LEFT,y=TOP, width=CONST.BUTTON_WIDTH)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_TeamFile_Content():
    # gets the content for the 'Team' file
    print("\n[DEBUG] Get_TeamFile_Body_Content() called")

    Content = "\n    <p>These are the members of our team, ...</p>"
    Content = Content + "\n    <simpletable>"
    Content = Content + "\n      <sthead>"
    Content = Content + "\n        <stentry>Name</stentry>"
    Content = Content + "\n        <stentry>Email</stentry>"
    Content = Content + "\n        <stentry>Reports To</stentry>"
    Content = Content + "\n      </sthead>"
    Content = Content + "\n      <strow>"
    Content = Content + "\n        <stentry>" + Name_Variable.get() + "</stentry>"
    Content = Content + "\n        <stentry>" + Email_Variable.get() + "</stentry>"
    Content = Content + "\n        <stentry>" + Reports_Variable.get() + "</stentry>"
    Content = Content + "\n      </strow>"
    Content = Content + "\n    </simpletable>"

    return(Content)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Create_TeamFile():
    print("\n[DEBUG] Create_TeamFile() called")
    # creates the 'Team' file
        
    Create_Topic("Team",Get_TeamFile_Content())
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# ADD TEAM MEMBER ///// ////////// ////////// ////////// ////////// ////////// //////////
def Add_TeamMember():
    print("\n[DEBUG] Add_TeamMember() called")
    # adds a new member to 'Team' file

    ExistingRows = Get_Existing_TeamMember_Rows()
    NewRow = Get_New_TeamMember_Row()

    Content = "\n    <p>These are the members of our team, ...</p>"
    Content = Content + "\n    <simpletable>"
    Content = Content + "\n      <sthead>"
    Content = Content + "\n        <stentry>Name</stentry>"
    Content = Content + "\n        <stentry>Email</stentry>"
    Content = Content + "\n        <stentry>Reports To</stentry>"
    Content = Content + "\n      </sthead>"
    Content = Content + ExistingRows
    Content = Content + NewRow
    Content = Content + "\n    </simpletable>"

    # create a new 'Team' file
    Create_Topic("Team",Content)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_Existing_TeamMember_Rows():
    # gets existing team members from 'Team' file
    print("\n[DEBUG] Get_Existing_TeamMember_Rows() called")

    ExistingRows = ""

    # build expected path to team file
    path_to_team_file = os.getcwd() + "\\Team\\t_team.dita"

    if os.path.exists(path_to_team_file):
        #print("[DEBUG] > Existing rows in 't_team.dita':")

        document = xml.dom.minidom.parse(path_to_team_file)

        for node_strow in document.getElementsByTagName("strow"):
            ExistingRows = ExistingRows + "\n      <strow>"
            for node in node_strow.getElementsByTagName("stentry"):
                #print(node.firstChild.nodeValue)
                ExistingRows = ExistingRows + "\n        <stentry>" + node.firstChild.nodeValue + "</stentry>"

            ExistingRows = ExistingRows + "\n      </strow>"

    return(ExistingRows)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Get_New_TeamMember_Row():
    # gets new team member row    
    print("\n[DEBUG] Get_New_TeamMember_Row() called")

    NewRow = "\n      <strow>"
    NewRow = NewRow + "\n        <stentry>" + Name_Variable.get() + "</stentry>"
    NewRow = NewRow + "\n        <stentry>" + Email_Variable.get() + "</stentry>"
    NewRow = NewRow + "\n        <stentry>" + Reports_Variable.get() + "</stentry>"
    NewRow = NewRow + "\n      </strow>"

    return(NewRow)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# ONBOARDING CONTENT // ////////// ////////// ////////// ////////// ////////// //////////
def Add_OnboardingContent_LableFrame():
    print("\n[DEBUG] Add_OnboardingContent_LableFrame() called")

    # LableFrame Widget
    global OnboardingContent_LabelFrame
    OnboardingContent_LabelFrame = LabelFrame(Onboarder,text=" Onboarding Content ")
    OnboardingContent_LabelFrame.place(x=CONST.OC_LEFT,y=CONST.CONTROLS_TOP,width=CONST.OC_WIDTH, height=CONST.OC_HEIGHT)
    OnboardingContent_LabelFrame.config(borderwidth=2, background="lightgray")

    # Buttons
    List_ContentFiles_Button = Button(OnboardingContent_LabelFrame,text="List Content Files",command=List_ContentFiles)
    List_ContentFiles_Button.place(x=200,y=CONST.Y_OFFSET / 2,width=CONST.BUTTON_WIDTH)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_0():
    # adds checkbox 0
    print("\n[DEBUG] Add_Checkbox_0() called")

    global Checkbox_0
    Checkbox_0_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_0 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=" t_team.dita",variable=Checkbox_0_Variable,onvalue=1,offvalue=0)
    Checkbox_0.place(x=8,y=8)
    Checkbox_0.config(state="disabled")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_1(filename):
    # adds checkbox 1
    print("\n[DEBUG] Add_Checkbox_1() called")

    global Checkbox_1
    Checkbox_1_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_1 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_1_Variable,onvalue=1,offvalue=0)
    Checkbox_1.place(x=8,y=8 + 24)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_2(filename):
    # adds checkbox 2
    print("\n[DEBUG] Add_Checkbox_2() called")

    global Checkbox_2
    Checkbox_2_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_2 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_2_Variable,onvalue=1,offvalue=0)
    Checkbox_2.place(x=8,y=8 + (24 * 2))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_3(filename):
    # adds checkbox 3
    print("\n[DEBUG] Add_Checkbox_3() called")

    global Checkbox_3
    Checkbox_3_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_3 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_3_Variable,onvalue=1,offvalue=0)
    Checkbox_3.place(x=8,y=8 + (24 * 3))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_4(filename):
    # adds checkbox 4
    print("\n[DEBUG] Add_Checkbox_4() called")

    global Checkbox_4
    Checkbox_4_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_4 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_4_Variable,onvalue=1,offvalue=0)
    Checkbox_4.place(x=8,y=8 + (24 * 4))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_5(filename):
    # adds checkbox 5
    print("\n[DEBUG] Add_Checkbox_5() called")

    global Checkbox_5
    Checkbox_5_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_5 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_5_Variable,onvalue=1,offvalue=0)
    Checkbox_5.place(x=8,y=8 + (24 * 5))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def Add_Checkbox_6(filename):
    # adds checkbox 6
    print("\n[DEBUG] Add_Checkbox_6() called")

    global Checkbox_6
    Checkbox_6_Variable = IntVar(OnboardingContent_LabelFrame)
    Checkbox_6 = Checkbutton(OnboardingContent_LabelFrame,background="lightgray",text=filename,variable=Checkbox_6_Variable,onvalue=1,offvalue=0)
    Checkbox_6.place(x=8,y=8 + (24 * 6))
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def List_ContentFiles():
    # lists the content files
    print("\n[DEBUG] List_ContentFiles() called")

    global  Checkbox_0_filename,\
            Checkbox_1_filename,\
            Checkbox_2_filename,\
            Checkbox_3_filename,\
            Checkbox_4_filename,\
            Checkbox_5_filename,\
            Checkbox_6_filename
    
    # build expected path to 'Team' folder
    path_to_team_file = os.getcwd() + "\\Team"
    folder = os.listdir(path_to_team_file)
    
    Add_Checkbox_0()
    Checkbox_0_filename = " t_team.dita"
    Checkbox_0.select()

    Counter = 1
    for file in folder:
        if file!="t_team.dita" and file.startswith("t_") and not(file.startswith("b_")):
            if Counter==1:
                Add_Checkbox_1(" " + file)
                Checkbox_1_filename = file

            if Counter==2:
                Add_Checkbox_2(" " + file)
                Checkbox_2_filename = file
        
            if Counter==3:
                Add_Checkbox_3(" " + file)
                Checkbox_3_filename = file

            if Counter==4:
                Add_Checkbox_4(" " + file)
                Checkbox_4_filename = file

            if Counter==5:
                Add_Checkbox_5(" " + file)
                Checkbox_5_filename = file

            if Counter==6:
                Add_Checkbox_6(" " + file)
                Checkbox_6_filename = file

            Counter = Counter + 1
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

Add_TeamMember_LableFrame()

Add_OnboardingContent_LableFrame()

Onboarder.mainloop()
print("----------------------------------------------------\n")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
