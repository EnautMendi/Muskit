import PySimpleGUI as sg
import os.path
import QuantumGates
import functionalities
import threading
import time


#originPath = ""         #Path of the origin file
#savePath = ""           #path where the mutants are going to be saved
#executingFiles = ("",)  #Files selected to be executed
#resultPath = ""         #path where the results file is going to be saved
maxNum = 100            #max number of mutants will create
operators = ("",)       #Type of operators are going to use to create mutants
types = ("",)            #Types of gates the mutation will change
gateNum = (1,)          #IDNumber of the gates that mutation is going to change
gapNum = (1,)           #IDNumber of the gaps that mutation is going to change
numShots = 10
all = False
add = False
remove = False
replace = False
oneQubit = False
manyQubit = False
allInputs = False
#sg.theme_previewer(scrollable=True)
MutantCreationColumn = [
    [
        sg.Text("Select origin file ", font="Arial 14"),
        sg.In(size=(32, 1), enable_events=True, key="-OriginFile-"),
        sg.FileBrowse(file_types=(("Python files",["*.py" , "*.pyc"]), ("All files","*.*")), pad=(0,20), key="-OriginFileBrowser-"),
    ],
    [
        sg.Text("Select mutants save path", font="Arial 14"),
        sg.In(size=(25, 1), enable_events=True, key="-MutantsSavePath-", disabled=True),
        sg.FolderBrowse(pad=(0,20), disabled=True, key="-MutantsSaveBrowser-"),
    ],
    [
        sg.Text("Check this box if you want to create all possible mutants: ", font="Arial 14", pad=(0, 20)),
        sg.Checkbox("All", default=False, enable_events=True, key="-All-", disabled=True),
    ],
    [
        sg.Text("Max number of mutants created", font="Arial 14"),
        sg.InputCombo((10, 50, 100), size=(5, 1), default_value=100, pad=(0,20), enable_events=True, key="-MaxMutants-", disabled=True),
    ],
    [
        sg.Text("Select operators:", font="Arial 14", pad=(0,20)),
    ],
    [
        sg.Checkbox("Add", default=False, enable_events=True, key="-Add-", disabled=True),
        sg.Checkbox("Remove", default=False, enable_events=True, key="-Remove-", disabled=True),
        sg.Checkbox("Replace", default=False, enable_events=True, key="-Replace-", disabled=True)
    ],
    [
        sg.Text("Select gate types:", font="Arial 14", pad=(0,20)),
    ],
    [
        sg.Checkbox("OneQubit            ", default=False, enable_events=True, key="-OneQubit-", disabled=True),
        sg.Checkbox("ManyQubit", default=False, enable_events=True, key="-ManyQubit-", disabled=True)
    ],
    [
        sg.Text("Select gates:", font="Arial 14", pad=(0, 20)),
    ],
    [
        sg.Listbox("", size=(20, 5), select_mode="multiple", pad=(120,10), enable_events=True, key="-GateList-", disabled=True),
    ],
    [
        sg.Button("CREATE", key="-Create-", disabled=True)
    ],
    [
        sg.Text("The files are being created, Wait a moment!!!", font="Arial 20", visible=False, text_color="firebrick", key="-WarningMessage1-"),

    ],
    [
        sg.Text("Your files were created ;)", font="Arial 20", visible=False, text_color="light blue", key="-FinishMessage1-"),

    ],
]

MutantExecutionColumn = [
    [
        sg.Text("Select files to execute", font="Arial 14"),
        sg.In(size=(25, 1), enable_events=True, key="-ExecutionFiles-"),
        sg.FilesBrowse(file_types=(("Python files",["*.py" , "*.pyc"]), ("All files","*.*")), pad=(0,20), key="-ExecutionFilesBrowser-"),
    ],
    [
        sg.Text("Select result save path", font="Arial 14"),
        sg.In(size=(25, 1), enable_events=True, key="-ResultsSavePath-", disabled=True),
        sg.FolderBrowse(pad=(0,50), disabled=True, key="-ResultsSaveBrowser-"),
    ],
    [
        sg.Text("Number of shots for the execution", font="Arial 14"),
        sg.InputCombo((10, 100, 1000), size=(5, 1), default_value=0, pad=(0,50), enable_events=True, key="-NumShots-", disabled=True),
    ],
    [
        sg.Text("Inputs for the execution", font="Arial 14"),
        sg.Checkbox("All inputs", default=False, enable_events=True, key="-AllInputs-", disabled=True),
    ],
    [
        sg.Button("EXECUTE", key="-Execute-", disabled=True)
    ],
    [
        sg.Text("The files are being executed, Wait a moment!!!", font="Arial 20", visible=False, text_color="firebrick", key="-WarningMessage2-"),

    ],
    [
        sg.Text("Your files were executed and the results saved ;)", font="Arial 20", visible=False, text_color="light blue", key="-FinishMessage2-"),

    ],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(MutantCreationColumn),
        sg.VSeperator(),
        sg.Column(MutantExecutionColumn),
    ]
]


window = sg.Window("Mutant Generation Framework", layout, size=[1200,800], location=[350,10])


# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-OriginFile-":
        originPath = values["-OriginFile-"]
        if originPath != "":
            info = functionalities.getInfo(originPath)
            window["-GateList-"].update(disabled=False)
            window["-GateList-"].update(info[5])
            window["-GateList-"].update(disabled=True)
            window["-MutantsSavePath-"].update(disabled=False)
            window["-MutantsSaveBrowser-"].update(disabled=False)


    elif event == "-MutantsSavePath-":
        savePath = values["-MutantsSavePath-"]
        if savePath != "":
            window["-All-"].update(disabled=False)
            window["-MaxMutants-"].update(disabled=False)

    elif event == "-All-":
        if all == False:
            all = True
            window["-MaxMutants-"].update(disabled=True)
            window["-Add-"].update(disabled=True)
            window["-Remove-"].update(disabled=True)
            window["-Replace-"].update(disabled=True)
            window["-OneQubit-"].update(disabled=True)
            window["-ManyQubit-"].update(disabled=True)
            window["-GateList-"].update(disabled=True)
            window["-Create-"].update(disabled=False)
        else:
            all = False
            window["-MaxMutants-"].update(disabled=False)

    elif event == "-MaxMutants-":
        maxNum = values["-MaxMutants-"]
        window["-Add-"].update(disabled=False)
        window["-Remove-"].update(disabled=False)
        window["-Replace-"].update(disabled=False)
        window["-OneQubit-"].update(disabled=False)
        window["-ManyQubit-"].update(disabled=False)
        window["-GateList-"].update(disabled=False)


    elif event == "-Add-":
        if add == False:
            add = True
        else:
            add = False

    elif event == "-Remove-":
        if remove == False:
            remove = True
        else:
            remove = False

    elif event == "-Replace-":
        if replace == False:
            replace = True
        else:
            replace = False

    elif event == "-OneQubit-":
        if oneQubit == False:
            oneQubit = True
        else:
            oneQubit = False

    elif event == "-ManyQubit-":
        if manyQubit == False:
            manyQubit = True
        else:
            manyQubit = False

    elif event == "-GateList-":
        selectedGates = values["-GateList-"]
        for x in selectedGates:
            tmp = x.split(" ")
            if x == selectedGates[0]:
                if tmp[2] in QuantumGates.AllGates:
                    gateNum = (int(tmp[0]),)
                    gapNum = (int(tmp[0]),)
                else:
                    gapNum = (int(tmp[0]),)
            else:
                if tmp[2] in QuantumGates.AllGates:
                    gateNum = gateNum + (int(tmp[0]),)
                    gapNum = gapNum + (int(tmp[0]),)
                else:
                    gapNum = gapNum + (int(tmp[0]),)

        window["-Create-"].update(disabled=False)
    elif event == "-Create-":
        if all == True:
            info = functionalities.getInfo(originPath)
            operators= ("Add","Remove","Replace")
            types = ("OneQubit","ManyQubit")
            x = 1
            gateNum = (x,)
            while x < info[2]:
                x = x + 1
                gateNum = gateNum + (x,)

            x = 1
            gapNum = (x,)
            while x < (info[2]+info[0]):
                x = x + 1
                gapNum = gapNum + (x,)
            maxNum = len(QuantumGates.AllGates)*len(gapNum) + (len(QuantumGates.AllGates)-1)*len(gateNum) + len(gateNum)

        else:
            if add == True:
                operators = ("Add",)
                if remove == True:
                    operators = operators + ("Remove",)
                if replace == True:
                    operators = operators + ("Replace",)
            elif remove == True:
                operators = ("Remove",)
                if replace == True:
                    operators = operators + ("Replace",)
            elif replace == True:
                operators = ("Replace",)

            if oneQubit == True:
                types = ("OneQubit",)
                if manyQubit == True:
                    types = types + ("ManyQubit",)
            elif manyQubit == True:
                types = ("ManyQubit",)

        window["-OriginFile-"].update(disabled=True)
        window["-OriginFileBrowser-"].update(disabled=True)
        window["-MutantsSavePath-"].update(disabled=True)
        window["-MutantsSaveBrowser-"].update(disabled=True)
        window["-MaxMutants-"].update(disabled=True)
        window["-All-"].update(disabled=True)
        window["-Add-"].update(disabled=True)
        window["-Remove-"].update(disabled=True)
        window["-Replace-"].update(disabled=True)
        window["-OneQubit-"].update(disabled=True)
        window["-ManyQubit-"].update(disabled=True)
        window["-GateList-"].update(disabled=True)
        window["-Create-"].update(disabled=True)
        window["-ExecutionFiles-"].update(disabled=True)
        window["-ExecutionFilesBrowser-"].update(disabled=True)
        window["-ResultsSavePath-"].update(disabled=True)
        window["-ResultsSaveBrowser-"].update(disabled=True)
        window["-NumShots-"].update(disabled=True)
        window["-Execute-"].update(disabled=True)
        window["-WarningMessage1-"].update(visible=True)
        window.refresh()
        functionalities.createMutants(maxNum,operators,types,gateNum,gapNum,originPath,savePath,all)
        window["-WarningMessage1-"].update(visible=False)
        window["-FinishMessage1-"].update(visible=True)
        window["-OriginFile-"].update(disabled=False)
        window["-OriginFileBrowser-"].update(disabled=False)
        window["-MutantsSavePath-"].update(disabled=False)
        window["-MutantsSaveBrowser-"].update(disabled=False)
        window["-All-"].update(disabled=False)
        window["-ExecutionFiles-"].update(disabled=False)
        window["-ExecutionFilesBrowser-"].update(disabled=False)
        window["-ResultsSavePath-"].update(disabled=False)
        window["-ResultsSaveBrowser-"].update(disabled=False)
        window["-NumShots-"].update(disabled=False)
        window["-Execute-"].update(disabled=False)
        window.refresh()
        time.sleep(2)
        window["-FinishMessage1-"].update(visible=False)
        window.refresh()

    elif event == "-ExecutionFiles-":
        executingFiles = values["-ExecutionFiles-"].split(";")
        window["-ResultsSavePath-"].update(disabled=False)
        window["-ResultsSaveBrowser-"].update(disabled=False)

    elif event == "-ResultsSavePath-":
        resultPath = values["-ResultsSavePath-"]
        window["-NumShots-"].update(disabled=False)

    elif event == "-NumShots-":
        numShots = values["-NumShots-"]
        window["-AllInputs-"].update(disabled=False)
        window["-Execute-"].update(disabled=False)

    elif event == "-AllInputs-":
        if allInputs == False:
            allInputs = True
        else:
            allInputs = False


    elif event == "-Execute-":
        window["-OriginFile-"].update(disabled=True)
        window["-OriginFileBrowser-"].update(disabled=True)
        window["-MutantsSavePath-"].update(disabled=True)
        window["-MutantsSaveBrowser-"].update(disabled=True)
        window["-MaxMutants-"].update(disabled=True)
        window["-All-"].update(disabled=True)
        window["-Add-"].update(disabled=True)
        window["-Remove-"].update(disabled=True)
        window["-Replace-"].update(disabled=True)
        window["-OneQubit-"].update(disabled=True)
        window["-ManyQubit-"].update(disabled=True)
        window["-GateList-"].update(disabled=True)
        window["-Create-"].update(disabled=True)
        window["-ExecutionFiles-"].update(disabled=True)
        window["-ExecutionFilesBrowser-"].update(disabled=True)
        window["-ResultsSavePath-"].update(disabled=True)
        window["-ResultsSaveBrowser-"].update(disabled=True)
        window["-NumShots-"].update(disabled=True)
        window["-AllInputs-"].update(disabled=True)
        window["-Execute-"].update(disabled=True)
        window["-WarningMessage2-"].update(visible=True)
        window.refresh()
        functionalities.executeMutants(executingFiles, resultPath, numShots, allInputs)
        window["-WarningMessage2-"].update(visible=False)
        window["-FinishMessage2-"].update(visible=True)
        window["-OriginFile-"].update(disabled=False)
        window["-OriginFileBrowser-"].update(disabled=False)
        window["-MutantsSavePath-"].update(disabled=False)
        window["-MutantsSaveBrowser-"].update(disabled=False)
        window["-ExecutionFiles-"].update(disabled=False)
        window["-ExecutionFilesBrowser-"].update(disabled=False)
        window["-ResultsSavePath-"].update(disabled=False)
        window["-ResultsSaveBrowser-"].update(disabled=False)
        window["-NumShots-"].update(disabled=False)
        window["-AllInputs-"].update(disabled=False)
        window["-Execute-"].update(disabled=False)
        window.refresh()
        time.sleep(2)
        window["-FinishMessage2-"].update(visible=False)
        window.refresh()


window.close()