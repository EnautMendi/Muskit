def StartMenu():
    num = 0
    print("What do you want to do?:")
    print("1.Add")
    print("2.Remove")
    print("3.Replace")
    print("4.All")
    enter = True
    while num != 1 and num != 2 and num != 3 and num != 4 or enter==True:
        enter = False
        try:
            print("Insert a valid option:")
            num = int(input())
        except ValueError:
            print("ERROR, This is not a number!!!!")
    return num