import tkinter as tk
import easygui as eg
from tkinter import font
from tkinter import filedialog
from tkinter import *

#global variables
originPath = ""
mutantSavePath = ""
resultsSavePath = ""
maxNumMutants = ""
operation = ""
location = ""
gateType = ""
executionShots = 10


class StartPage:

    def __init__(self, master):
        self.master = master
        self.frame1 = Frame(self.master, borderwidth=5)
        self.frame2 = Frame(self.master, borderwidth=5)
        self.b1 = Button(self.frame1, font=helv36, text="Create mutants", width=16, height=4, bg="grey", fg="white", command=self.createMutants)
        self.b2 = Button(self.frame2, font=helv36, text="Execute mutants", width=16, height=4, bg="grey", fg="white", command=self.executeMutants)
        self.b1.pack(expand=True)
        self.b2.pack(expand=True)
        self.frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def createMutants(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("%dx%d+%d+%d" % (screen_width, screen_height,-5,0))
        bb = createPage(self.newWindow)

    def executeMutants(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("%dx%d+%d+%d" % (screen_width, screen_height, -5, 0))
        bb = executionPage(self.newWindow)


class createPage():

    def __init__(self, master):
        self.master = master
        self.frame1 = Frame(self.master, borderwidth=5)
        self.frame2 = Frame(self.master, borderwidth=5)
        self.frame3 = Frame(self.master)
        self.frame11 = Frame(self.frame1)
        self.frame12 = Frame(self.frame1)
        self.frame21 = Frame(self.frame2)
        self.frame22 = Frame(self.frame2)
        self.frame31 = Frame(self.frame3)
        self.frame32 = Frame(self.frame3)
        self.filepath = Text(self.frame11, height=2, width=30)
        self.file = Button(self.frame12, text="Browse file", command=self.executionPath_button)
        self.savepath = Text(self.frame21, height=2, width=30)
        self.folder = Button(self.frame22, text="Browse save path", command=self.savePath_button)
        self.b1 = Button(self.frame31, text="All posible mutants", font=helv36, width=16, height=4, bg="grey", fg="white",
                         command=self.createAll)
        self.b2 = Button(self.frame32, text="Custom settings", font=helv36, width=16, height=4, bg="grey", fg="white",
                         command=self.customInterface)


        self.frame1.pack(pady=(100,100))
        self.frame11.pack(side=tk.LEFT)
        self.frame12.pack(side=tk.LEFT)
        self.frame2.pack(pady=(100,100))
        self.frame21.pack(side=tk.LEFT)
        self.frame22.pack(side=tk.LEFT)
        self.frame3.pack()
        self.frame31.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame32.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.b1.pack(expand=True, padx=(50, 50), pady=(100, 100))
        self.b2.pack(expand=True, padx=(50, 50), pady=(100, 100))
        self.filepath.pack()
        self.file.pack()
        self.savepath.pack()
        self.folder.pack()


    def createAll(self):
        print("Creating all mutants")

    def customInterface(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("%dx%d+%d+%d" % (screen_width, screen_height, -5, 0))
        bb = customPage(self.newWindow)

    def executionPath_button(self):
        self.filepath.delete(1.0, tk.END)
        originPath = filedialog.askopenfilenames(parent=self.master, initialdir="", title="Open file", filetypes = (("Python files",["*.py" , "*.pyc"]),("all files","*.*")))
        self.filepath.insert(tk.END, originPath)

    def savePath_button(self):
        self.savepath.delete(1.0, tk.END)
        mutantSavePath = filedialog.askdirectory(parent=self.master, initialdir="", title="Please select a directory")
        self.savepath.insert(tk.END, mutantSavePath)

class executionPage():

    def __init__(self, master):
        tkvar = IntVar(master)
        tkvar.set(10)
        numChoices = [5, 10, 50, 100]
        self.master = master
        self.master.grid_columnconfigure(0,weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.frame1 = Frame(self.master)
        self.frame2 = Frame(self.master)
        self.frame3 = Frame(self.master)
        self.frame4 = Frame(self.master)
        self.frame11 = Frame(self.frame1)
        self.frame12 = Frame(self.frame1)
        self.frame13 = Frame(self.frame1)
        self.frame21 = Frame(self.frame2)
        self.frame22 = Frame(self.frame2)
        self.frame23 = Frame(self.frame2)
        self.frame31 = Frame(self.frame3)
        self.frame32 = Frame(self.frame3)

        self.filelabel = Label(self.frame11, text="Select the file you want to execute:")
        self.filepath = Text(self.frame12, height=2, width=30)
        self.file = Button(self.frame13, text="Browse file", command=self.executionPath_button)

        self.savelabel = Label(self.frame21, text="Select the directory you want to save results:")
        self.savepath = Text(self.frame22, height=2, width=30)
        self.folder = Button(self.frame23, text="Browse save path", command=self.savePath_button)

        self.shotsNumlabel = Label(self.frame31, text="Select number of shots in the simulation:")
        self.shotsDropDown = OptionMenu(self.frame32, tkvar, *numChoices)

        self.executer = Button(self.frame4, text="Execute", font=helv36, bg="grey", fg="white", command=self.executeMutants)


        self.frame1.grid(row=0, column=0, pady=(50,50))
        self.frame1.grid_columnconfigure(0,weight=1)
        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame11.grid(row=0, column=0)
        self.frame12.grid(row=1, column=0)
        self.frame13.grid(row=1, column=1)
        self.filelabel.pack()
        self.filepath.pack()
        self.file.pack()

        self.frame2.grid(row=1, column=0, pady=(50,50))
        self.frame2.grid_columnconfigure(0,weight=1)
        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame21.grid(row=0, column=0)
        self.frame22.grid(row=1, column=0)
        self.frame23.grid(row=1, column=1)
        self.savelabel.pack()
        self.savepath.pack()
        self.folder.pack()

        self.frame3.grid(row=2, column=0, pady=(50,50))
        self.frame3.grid_columnconfigure(0,weight=1)
        self.frame3.grid_rowconfigure(0, weight=1)
        self.frame31.grid(row=0, column=0)
        self.frame32.grid(row=1, column=0)
        self.shotsNumlabel.pack()
        self.shotsDropDown.pack()

        self.frame4.grid(row=3, column=0)
        self.executer.pack()


    def executionPath_button(self):
        self.filepath.delete(1.0, tk.END)
        originPath = filedialog.askopenfilenames(parent=self.master, initialdir="", title="Open file", filetypes = (("Python files",["*.py" , "*.pyc"]),("all files","*.*")))
        self.filepath.insert(tk.END, originPath)

    def savePath_button(self):
        self.savepath.delete(1.0, tk.END)
        resultsSavePath = filedialog.askdirectory(parent=self.master, initialdir="", title="Please select a directory")
        self.savepath.insert(tk.END, resultsSavePath)

    def executeMutants(self):
        print(str(resultsSavePath))

        print('Executing mutants')

class customPage():

    def __init__(self, master):
        var = StringVar(master)
        tkvar = StringVar(master)
        tkvar.set("All")
        numChoices = ["100", "1000", "All"]
        self.master = master

        self.mutantsNumFrame = Frame(self.master)
        self.operationFrame = Frame(self.master)
        self.locationFrame = Frame(self.master)
        self.gateFrame = Frame(self.master)

        self.mutantsNumlabel = Label(self.mutantsNumFrame, text="Select the max number of mutants")
        self.numDropDown = OptionMenu(self.mutantsNumFrame, tkvar, *numChoices)

        self.operationlabel = Label(self.operationFrame, text="Select which operation do you want to use")
        self.operationCheckFrame = Frame(self.operationFrame)

        self.locationlabel = Label(self.locationFrame, text="Select the location qhere you want to apply changes")

        self.gatelabel = Label(self.gateFrame, text="Select which type of gate you want")
        self.gateCheckFrame = Frame(self.gateFrame)

        self.addRadio = Radiobutton(self.operationCheckFrame, text="ADD", variable = var, value="Add")
        self.removeRadio = Radiobutton(self.operationCheckFrame, text="REMOVE", variable = var, value="Remove")
        self.replaceRadio = Radiobutton(self.operationCheckFrame, text="REPLACE", variable = var, value="Replace")
        self.allRadio = Radiobutton(self.operationCheckFrame, text="ALL", variable = var, value="All")

        self.oneQubitCheck = Checkbutton(self.gateCheckFrame, text="ONE QUBIT GATES")
        self.manyQubitCheck = Checkbutton(self.gateCheckFrame, text="MANY QUBIT GATES")
        self.phaseCheck = Checkbutton(self.gateCheckFrame, text="PHASE GATES")
        self.allGatesCheck = Checkbutton(self.gateCheckFrame, text="ALL GATES")

        self.createButton = Button(self.master, text="Create mutants", font=helv36, bg="grey", fg="white", command=self.creation)


        self.mutantsNumFrame.grid(row=0,column=0, padx=(200,200), pady=(100,100))
        self.mutantsNumlabel.pack()
        self.numDropDown.pack()

        self.operationFrame.grid(row=0,column=1, padx=(200,200), pady=(100,100))
        self.operationlabel.pack()
        self.operationCheckFrame.pack()
        self.addRadio.grid(row=0, column=0)
        self.removeRadio.grid(row=0, column=1)
        self.replaceRadio.grid(row=1, column=0)
        self.allRadio.grid(row=1, column=1)

        self.locationFrame.grid(row=1,column=0, padx=(200,200), pady=(100,100))
        self.locationlabel.pack()

        self.gateFrame.grid(row=1,column=1, padx=(200,200), pady=(100,100))
        self.gatelabel.pack()
        self.gateCheckFrame.pack()
        self.oneQubitCheck.grid(row=0, column=0)
        self.manyQubitCheck.grid(row=0, column=1)
        self.phaseCheck.grid(row=1, column=0)
        self.allGatesCheck.grid(row=1, column=1)

        self.createButton.grid(row=3, column=0, padx=(200, 200), pady=(100, 100))

    def creation(self):
        print('Customizing mutant creation')




root = tk.Tk()
helv36 = font.Font(family='Helvetica', size=36)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (screen_width, screen_height,-5,0))
StartPage(root)
root.mainloop()
