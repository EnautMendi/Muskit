import Menu
import Functionalities
import easygui as eg

"Select the file that is going to be mutated"
extension = ["*.py", "*.pyc"]
path = eg.fileopenbox(msg="Open file", title="Fileopenbox", default='', filetypes=extension)

"Select the mutation option"
option = Menu.StartMenu()
if option == 1:
    result = Functionalities.add(path)
elif option == 2:
    result = Functionalities.remove(path)
elif option == 3:
    result = Functionalities.replace(path)
elif option == 4:
    result = Functionalities.add(path)
    result = result + Functionalities.remove(path)
    result = result + Functionalities.replace(path)
else:
    result = 0

if result > 0:
    print("\n")
    print("--------------------------------------------------------------------")
    print("The mutated programs has been created successfully!!!")
    print("Total mutated files created: " + str(result))
    print("--------------------------------------------------------------------")
else:
    print("An ERROR occurred while doing the mutation")
