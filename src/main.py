import os
import PySimpleGUI as sg
import os
from keys import keys
from keys import specialCharacters
from settings import settings
from designaLoop import loop
from designaLoop import loopCreated
with open("src//UserAssignedData//path.txt", "r") as file:
    pathtoahk = file.read()    
    file.close()
def main():
    menu_def = [['File',['Settings', 'Create a Loop']]]
    sg.theme("LightBlue4")
    box=[
        [sg.Menu(menu_def)],
        [sg.Text("DONT SELECT THE SAME HOTKEY TWICE!", font=(50))],
        [sg.HorizontalSeparator()],
        [sg.Combo(keys, size=(10,10), key="LISTBOX")],
        [sg.Combo(['Send,', 'Run,'], size=(10,10), key="Listedbox")],
        [sg.Text("Type what you'd like to run or send here")], # this is a cry for help?
        [sg.Input(key="COMMAND")],
        [sg.Text("For special characters please select one of the below, if none, leave empty")],
        [sg.Combo(specialCharacters, key="SPECIALCHARACTERS")],
        [sg.Button("Enter", key="ENTER"), sg.Button("Wipe", key="WIPE")]
    ]
    layout=[
        [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
        [sg.Text('', pad=(0,0),key='-EXPAND2-'),              # the thing that expands from left
        sg.Column(box, vertical_alignment='center', justification='center',  k='-C-')],
    ]
    #ADD CUSTOMIZABLE AHK FILE !!!
    window = sg.Window("Input to Autohotkey", layout, size=(500,250))
    while True:        
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        def check():
            with open(pathtoahk, "r") as file:
                     readfile = file.read()
            for line in readfile:
                    if values["LISTBOX"] in readfile:
                        return True
            return False
            
        if event == "WIPE":
            open(pathtoahk, "w").close()
        if event == "ENTER":
            def write():        
                 with open(pathtoahk, "a") as file:
                     newline = "\n"
                     value = values["LISTBOX"]
                     file.write(value)
                     file.write(newline)
                     file.write(values["Listedbox"])
                     file.write(" ")
                     file.write(values["COMMAND"])
                     file.write(newline)
                     if not values["SPECIALCHARACTERS"] == "":
                             file.write("Send,")
                             file.write(values['SPECIALCHARACTERS'])
                     file.write(newline)        
            if values["COMMAND"] == "":
                sg.PopupError("Please enter at least one value")
            if values["LISTBOX"] == "":
                sg.PopupError("Please enter at least one key")
            if values["Listedbox"] == "":
                sg.PopupError("Please enter at least one method")        
            if values["Listedbox"] != "" and values["LISTBOX"] != "" and values["COMMAND"] != "":
                check()
                if check():
                    sg.PopupError("Key is already in use")
                else:
                    write()
        if event == "Settings":
            settings()
        if event == "Create a Loop":
            loop()    
                
                    
            

if __name__ == '__main__':
     main()        
