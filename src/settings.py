import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText
def settings():
    layout=[
        [sg.Text("Enter the path to the autohotkey file (if you have installed ahk, left click, new, autohotkey script)")],
        [sg.Input(key="PATHTOAHK",size=(650, 10))],
        [sg.Button("Save", key="SAVE"), sg.Button("Cancel", key="CANCEL"), sg.Button("Wipe", key="WIPE")]
    ]
    window = sg.Window("Settings", layout, size=(650,205))
    while True:
         event, values = window.read()
         def write():    
                      with open("src//UserAssignedData//path.txt", "w") as file:
                          file.write(values["PATHTOAHK"])
                          file.close()
         if event == sg.WIN_CLOSED:
             break
         if event == "SAVE":
             if os.path.exists(values["PATHTOAHK"]):
                 write()
             else:
                 sg.PopupError("Not a valid file!")
             
         if event == "CANCEL":
             window.close()
             break
         if event == "WIPE":
             open("src//UserAssignedData//path.txt", "w").close()
                     

        