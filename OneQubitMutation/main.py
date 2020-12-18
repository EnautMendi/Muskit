import Menu
import Functionalities
import os


print("Insert your file path:")
path = input()
path = "python " + path
#os.system(path)
"""
option = Menu.StartMenu()
if option == 1:
    result = Functionalities.add(path)
elif option == 2:
    result = Functionalities.remove(path)
elif option == 3:
    result = Functionalities.replace(path)
elif option == 4:
    result = Functionalities.add(path)
    result = Functionalities.remove(path)
    result = Functionalities.replace(path)
else:
    result = 0

if result == 1:
    print("The mutated programs has been created successfully")
else:
    print("An ERROR occurred while doing the mutation")
"""