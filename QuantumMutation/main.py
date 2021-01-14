import menu
import functionalities
import easygui as eg
originPath = "/home/enautmendi/Documentos/circuit.py"       #Path of the origin file
savePath = "/home/enautmendi/Documentos"                    #path where the mutants are going to be saved
maxNum = 100                                             #max number of mutants will create
operators = ("REPLACE")                    #Type of operators are going to use to create mutants
types = ("OneQubit", "ManyQubit")                           #Types of gates the mutation will change
gateNum = (1,2)                                             #IDNumber of the gates that mutation is going to change
gapNum = (1,2)                                              #IDNumber of the gaps that mutation is going to change

functionalities.createMutants(maxNum, operators, types, gateNum, gapNum, originPath, savePath)

"""
"Select the file that is going to be mutated"
extension = ["*.py", "*.pyc"]
path = eg.fileopenbox(msg="Open file", title="Fileopenbox", default='', filetypes=extension)
print(path)


"Select the mutation option"
option = menu.StartMenu()
if option == 1:
    result = functionalities.addOLD(path)
    mutants = len(result)
    functionalities.executeOLD(result)

elif option == 2:
    result = functionalities.removeOLD(path)
    mutants = len(result)
    functionalities.executeOLD(result)

elif option == 3:
    result = functionalities.replaceOLD(path)
    mutants = len(result)
    functionalities.executeOLD(result)

elif option == 4:
    result = functionalities.addOLD(path)
    result.extend(functionalities.removeOLD(path))
    result.extend(functionalities.replaceOLD(path))
    mutants = len(result)
    functionalities.executeOLD(result)
else:
    mutants = 0

if mutants > 0:
    print("\n")
    print("--------------------------------------------------------------------")
    print("The mutated programs has been created successfully!!!")
    print("Total mutated files created: " + str(mutants))
    print("--------------------------------------------------------------------")
else:
    print("An ERROR occurred while doing the mutation")
"""
