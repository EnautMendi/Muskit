import getopt
import sys
import functionalities
import generatorConfig


mode = str(sys.argv[len(sys.argv)-1])

if mode == "Execute":
    files = sys.argv[1:(len(sys.argv) - 1)]
    splitChar = "\\"
    if splitChar not in files[0]:
        splitChar = chr(47)
    path = files[0].split(splitChar)
    savePath = path[0]
    x = 1
    while x < len(path) - 1:
        savePath = savePath + splitChar + path[x]
        x = x + 1
    functionalities.executeMutants(files, savePath, executorConfig.numShots, executorConfig.allInputs)
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
    functionalities.createMutants(generatorConfig.maxNumberOfMutants, generatorConfig.operators, generatorConfig.types, generatorConfig.gateNum, generatorConfig.gapNum, file, savePath, generatorConfig.allMutants)
else:
    print("The command was not okay")