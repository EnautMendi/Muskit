import menu
import functionalities
import easygui as eg


"Select the file that is going to be mutated"
extension = ["*.py", "*.pyc"]
path = eg.fileopenbox(msg="Open file", title="Fileopenbox", default='', filetypes=extension)



"Select the mutation option"
option = menu.StartMenu()
if option == 1:
    result = functionalities.add(path)
    mutants = len(result)
    functionalities.execute(result)

elif option == 2:
    result = functionalities.remove(path)
    mutants = len(result)
    functionalities.execute(result)

elif option == 3:
    result = functionalities.replace(path)
    mutants = len(result)
    functionalities.execute(result)

elif option == 4:
    result = functionalities.add(path)
    result.extend(functionalities.remove(path))
    result.extend(functionalities.replace(path))
    mutants = len(result)
    functionalities.execute(result)
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

