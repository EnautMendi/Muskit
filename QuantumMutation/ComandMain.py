import getopt
import sys
import functionalities
import experimentsConfig


mode = str(sys.argv[len(sys.argv)-1])

if mode == "Execute":
    files = sys.argv[1:(len(sys.argv) - 1)]
    splitChar = 92
    if chr(splitChar) not in files:
        splitChar = 47

    path = files[0].split(chr(splitChar))
    savePath = path[0]
    x = 1
    while x < len(path) - 1:
        savePath = savePath + chr(splitChar) + path[x]
        x = x + 1
    functionalities.executeMutants(files, savePath, experimentsConfig.numShots, experimentsConfig.allInputs)
elif mode == "Create":
    file = str(sys.argv[1])

    splitChar = 92
    if chr(splitChar) not in file:
        splitChar = 47

    path = file.split(chr(splitChar))
    savePath = path[0]
    x = 1
    while x < len(path) - 1:
        savePath = savePath + chr(splitChar) + path[x]
        x = x + 1
    functionalities.createMutants(experimentsConfig.maxNumberOfMutants, experimentsConfig.operators, experimentsConfig.types, experimentsConfig.gateNum, experimentsConfig.gapNum, file, savePath, experimentsConfig.allMutants)
else:
    print("The command was not okay")