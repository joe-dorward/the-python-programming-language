# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
# Program Topic_Iterator_v1.01.py
# Written by: Joe Dorward
# Started: 12/01/2024

# This program:
# * iterates DITA XML Topic files, and reports their structure and content

import os # to get PATH information
import xml.dom.minidom
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def nodeText(node,indent):
    # prints the node-name and (if the first-character of the node-value is not the 
    # return-character) the node-value too

    if ord(node.firstChild.nodeValue[0]) == 10:
        node_text = indent + node.nodeName
    else:
        node_text = indent + node.nodeName + " = " + node.firstChild.nodeValue

    print(node_text)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def iterate_team_file():
    # build expected path to Topic file
    path_to_topic_file = os.getcwd() + "\\..\\Onboarder\\Team\\t_team.dita"

    # parse Topic file
    topic_file = xml.dom.minidom.parse(path_to_topic_file)

    for node in topic_file.getElementsByTagName("topic"):
        nodeText(node,"")

        for second_level in node.childNodes:
            if (second_level.nodeType == 1):
                nodeText(second_level,"  ")

            for third_level in second_level.childNodes:
                if (third_level.nodeType == 1):
                    nodeText(third_level,"    ")
 
                for fourth_level in third_level.childNodes:
                    if (fourth_level.nodeType == 1):
                        nodeText(fourth_level,"      ")

                    for fifth_level in fourth_level.childNodes:
                        if (fifth_level.nodeType == 1):
                            nodeText(fifth_level,"        ")

# MAIN ///// ////////// ////////// ////////// ////////// ////////// ////////// //////////
if __name__ == '__main__':    
    print("\nif __name__ == '__main__': (called)")
    
    print("----------------------------------------------------")
    # read command-line parameters
    #parameters = sys.argv[1:]
    
    iterate_team_file()
    print("----------------------------------------------------")
