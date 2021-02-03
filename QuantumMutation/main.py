import menu
import functionalities
import easygui as eg
originPath = "/home/enautmendi/Documentos/circuit.py"       #Path of the origin file
savePath = "/home/enautmendi/Documentos"                    #path where the mutants are going to be saved
executingFiles = ("/home/enautmendi/Documentos/AddMutations/Add1.py",
                  "/home/enautmendi/Documentos/AddMutations/Add2.py",
                  "/home/enautmendi/Documentos/AddMutations/Add3.py") #Files selected to be executed
resultPath = "/home/enautmendi/Documentos"                  #path where the reslts file is going to be saved
maxNum = 100                                                #max number of mutants will create
operators = ("ADD",)                                    #Type of operators are going to use to create mutants
types = ("OneQubit","ManyQubit")                                       #Types of gates the mutation will change
gateNum = (1,2)                                             #IDNumber of the gates that mutation is going to change
gapNum = (1,2,3,4)                                              #IDNumber of the gaps that mutation is going to change
#functionalities.createMutants(maxNum, operators, types, gateNum, gapNum, originPath, savePath)
#functionalities.executeMutants(executingFiles, resultPath)
