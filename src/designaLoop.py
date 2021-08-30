import PySimpleGUI as sg
from keys import keys
from keys import specialCharacters
pathtoahk = open("src//UserAssignedData//path.txt", "r").read()
def loopCreated():
    sg.theme('SandyBeach')
    methods = ["Send,", "Run,", "Sleep,"]
    loopCreated = [
        [sg.Text("This is more advanced!, choose what you'd like to add to you loop")],
        [sg.Combo(methods, key="METHOD", size=(10,10))],
        [sg.Input(key="INPUT"), sg.Text("Required!")],
        [sg.Text("Leave it empty if you dont want to use it")],
        [sg.Text("Please click apply before clicking close loop! Thanks! :D")],
        [sg.Combo(specialCharacters, key="SPECIALCHARACTER",size=(10,10))],
        [sg.Button("Apply", key="APPLY"),sg.Button("Close Loop", key="CLOSELOOP"), sg.Button("Go Back", key="GOBACK")]
    ]
    window = sg.Window("Create a Loop", loopCreated)
    while True:
        event, values = window.read()
        def write():
            with open(pathtoahk, "a") as file:
                file.write(values["METHOD"])
                file.write(", ")
                file.write(values["INPUT"])
                file.write("\n")
                if values["SPECIALCHARACTER"] != "":
                    file.write(values["SPECIALCHARACTER"])     
                file.write("\n")
                file.close()    
        if event == sg.WIN_CLOSED:
            break
        if event == "APPLY":
            if values["INPUT"] == "":
                sg.PopupError("No Parameters Wrote!")
            else:
                write()
        if event == "CLOSELOOP":
            with open(pathtoahk, "a") as file:
                file.write("}")
            window.close()
            loop()
            break
def loop():
    numberofloop = [1,2,3,4,5,6,7,8,9,10]
    sg.theme('SandyBeach')
    layout = [
        [sg.Text("choose the button you'd like to assign you  loop to")],
        [sg.Combo(keys, size=(10,10), key="KEY")],
        [sg.Text("how many times would you like it to be looped"),sg.Combo(numberofloop, size=(10,10), key=("TIMESOFLOOP"))],
        [sg.Button("Create Loop", key="CREATELOOP"), sg.Cancel()]
    ]
    window = sg.Window("Create a Loop", layout)
    while True:
        event, values = window.read()
        def gone():
            loopCreated()
            window.close() 
            
        def check():
            with open(pathtoahk, "r") as file:
                     readfile = file.read()
            for line in readfile:
                    if values["KEY"] in readfile:
                        return True
            return False
        def write():
            newline = "\n"
            file = open(pathtoahk, "a")
            file.write(values["KEY"])
            file.write(newline)
            file.write("Loop ")
            file.write(str(values["TIMESOFLOOP"]))
            file.write("{")
            file.write(newline)
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == "CREATELOOP":
            if values["KEY"] == "":
                sg.PopupError("Value Does not match available keys")
            if values["TIMESOFLOOP"] == "":
                sg.PopupError("Value is not selected between selectable numbers")    
                
            if values["KEY"] != ""  and values["TIMESOFLOOP"] != "":
                check()
                if check():
                    sg.PopupError("Key is already in use")
                    
                else:
                    write()
                    gone() 
            
            
