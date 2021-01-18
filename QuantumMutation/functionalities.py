import QuantumGates
import random
import os


def createMutants(maxNum, operators, types, gateIDs, gapIDs, originPath, savePath):
    info = getInfo(originPath)
    gateNum = len(gateIDs)
    GapNum = len(gapIDs)
    restquantity = maxNum
    first = True
    totalMutants = 0
    # Group only selected type gates
    if "OneQubit" in types:
        if "ManyQubit" in types:
            gates = QuantumGates.AllGates
        else:
            gates = QuantumGates.OneQubit
    elif "ManyQubit" in types:
        gates = QuantumGates.ManyQubit

    # Call each operator if has been selected and with it´s mutant number
    if "ADD" in operators:
        num = restquantity / len(operators)
        rest = restquantity % len(operators)
        addnum = num + rest
        if addnum > GapNum * len(gates):
            addnum = GapNum * len(gates)
        restquantity = restquantity - addnum
        totalMutants = totalMutants + add(addnum, gates, gapIDs, originPath, savePath)
        first = False
    if "REMOVE" in operators:
        if first == True:
            num = restquantity / len(operators)
            rest = restquantity % len(operators)
            removenum = num + rest
            if removenum > gateNum:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
        else:
            removenum = restquantity / (len(operators) - 1)
            if removenum > gateNum:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
    if "REPLACE" in operators:
        replacenum = restquantity
        if replacenum > (gateNum * len(gates))-gateNum:
            replacenum = (gateNum * len(gates))-gateNum
        totalMutants = totalMutants + replace(replacenum, gates, gateIDs, originPath, savePath)


    print("Number of mutants created: " + str(totalMutants))

def executeMutants(files, resultPath):
    splitChar = 92
    if chr(splitChar) not in resultPath:
        splitChar = 47
    tmpPath = resultPath + chr(splitChar) + "tmp.py"
    x = 0
    while x < len(files):
        Info = getInfo(files[x])
        QubitNum = Info[0]
        CircuitName = Info[1]
        QubitName = Info[3]
        ClassicName = Info[4]
        f = open(files[x])
        g = open(tmpPath, "w")
        line = f.readline()
        y=0
        while line != "":
            g.write(line)
            line = f.readline()
        while y < QubitNum:
            g.write(
                str(CircuitName) + ".measure(" + str(QubitName) + "[" + str(y) + "], " + str(ClassicName) + "[" + str(y) + "])")
            g.write("\n")
            y = y + 1
        g.write("simulator = Aer.get_backend('qasm_simulator')")
        g.write("\n")
        g.write("job = execute(" + str(CircuitName) + ", simulator, shots=" + str(QuantumGates.numShots) + ")")  ##execute for 10 times
        g.write("\n")
        # Grab results from the job
        g.write("result = job.result()")
        g.write("\n")
        # Returns counts
        g.write("counts = result.get_counts(" + str(CircuitName) + ")")
        g.write("\n")
        g.write("print(counts)")
        g.write("\n")
        g.write("r = open(" + chr(34) + (resultPath + chr(splitChar) + "results.txt") + chr(34) + ", " + chr(34)+ "a" + chr(34)+ ")")
        g.write("\n")
        g.write("r.write(" + chr(34)+ "The result of " + files[x] + " is: " + chr(34) + " + str(counts))")
        g.write("\n")
        g.write("r.write("+ chr(34) + chr(92) + "n"+ chr(34)+")")
        g.write("\n")
        g.write("r.close()")
        f.close()
        g.close()
        command = "python3 " + tmpPath
        os.system(command)
        os.remove(tmpPath)
        x = x + 1


def add(num, gates, gaps, origin, dirPath):
    print("Add mutants function " + str(num))
    return 0


def replace(num, gateTypes, changeGates, origin, dirPath):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    dirPath = dirPath + chr(splitChar) + "ReplaceMutations"
    os.mkdir(dirPath)

    Info = getInfo(origin)
    CircuitName = Info[1]
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 0
    while ObjectiveGap not in changeGates:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum != num:
        delete = False
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + "Replace" + str(MutationNum) + ".py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if temp2[0] in gateTypes:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap and (CurrentGap in changeGates):
                        if gateTypes[CurrentGate] == temp2[0]:
                            CurrentGate = CurrentGate + 1
                            if CurrentGate >= len(gateTypes) - 1:
                                ObjectiveGap = ObjectiveGap + 1
                                while (ObjectiveGap not in changeGates) and (
                                        ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                    ObjectiveGap = ObjectiveGap + 1

                                if ObjectiveGap > changeGates[(len(changeGates)-1)]:
                                    delete = True

                                CurrentGate = 0
                        if temp2[0] in QuantumGates.ManyQubit or gateTypes[CurrentGate] in QuantumGates.ManyQubit:
                            if temp2[0] in QuantumGates.ManyQubit and gateTypes[CurrentGate] in QuantumGates.ManyQubit:
                                g.write(
                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                Mutated = True
                            else:
                                if temp2[0] in QuantumGates.ManyQubit:
                                    while gateTypes[CurrentGate] not in QuantumGates.ManyQubit:
                                        CurrentGate = CurrentGate + 1
                                    if gateTypes[CurrentGate] == temp2[0]:
                                        CurrentGate = CurrentGate + 1
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                    Mutated = True
                                else:
                                    while gateTypes[CurrentGate] in QuantumGates.ManyQubit and CurrentGate < len(gateTypes) - 1:
                                        CurrentGate = CurrentGate + 1

                        else:
                            if temp2[0] in QuantumGates.PhaseGates:
                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                    Mutated = True
                                else:
                                    temp3 = temp2[1].split(",")
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                    Mutated = True
                            else:
                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                    g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) +
                                    "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
                                    Mutated = True
                                else:
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                    Mutated = True
                            if gateTypes[CurrentGate+1] in QuantumGates.ManyQubit:
                                ObjectiveGap = ObjectiveGap + 1
                                while (ObjectiveGap not in changeGates) and (
                                        ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                    ObjectiveGap = ObjectiveGap + 1
                                CurrentGate = 0

                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()

        f.close()
        g.close()
        if Mutated == False or delete == True:
            os.remove(newPath)
            MutationNum = MutationNum - 1
        if CurrentGate == len(gateTypes) - 1:
            ObjectiveGap = ObjectiveGap + 1
            while (ObjectiveGap not in changeGates) and (ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1
        total = MutationNum
        if ObjectiveGap > changeGates[(len(changeGates) - 1)]:
            MutationNum = num

    print("The REPLACE mutated files are located in: " + dirPath)
    return total


def remove(num, gateTypes, changeGates, origin, dirPath):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    dirPath = dirPath + chr(splitChar) + "RemoveMutations"
    os.mkdir(dirPath)

    Info = getInfo(origin)
    CircuitName = Info[1]
    MutationNum = 0
    ObjectiveGap = 0
    while ObjectiveGap not in changeGates:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum != num:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + "Remove" + str(MutationNum) + ".py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if temp2[0] in gateTypes:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap and (CurrentGap in changeGates):
                        Mutated = True
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()
        x = 0
        f.close()
        g.close()
        ObjectiveGap = ObjectiveGap + 1
        while (ObjectiveGap not in changeGates) and (ObjectiveGap < changeGates[(len(changeGates)-1)]):
            ObjectiveGap = ObjectiveGap + 1

    print("The REMOVE mutated files are located in: " + dirPath)
    return MutationNum

def executeOLD(files):
    print("\n")
    for x in files:
        splitChar = 92
        if chr(splitChar) not in x:
            splitChar = 47
        tmp = x.split(chr(splitChar))
        print("Executing file " + str(tmp[len(tmp)-1]) + " result after executing it " + str(QuantumGates.numShots) + " times is:")
        command = "python3 " + x
        os.system(command)
        print("\n")
    return

def addOLD(origin):

    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47

    path = origin.split(".")
    path2 = path[0].split(chr(splitChar))
    directories = origin.split(chr(splitChar))
    dirpath = ""
    directories[len(directories) - 1] = "AddMutations"
    for x in directories:
        if x == directories[0]:
            dirpath = dirpath + x
        else:
            dirpath = dirpath + chr(splitChar) + x
    os.mkdir(dirpath)
    path[0] = dirpath + chr(splitChar) + path2[len(path2) - 1]
    Info = getInfo(origin)
    QubitNum = Info[0]
    CircuitName = Info[1]
    GateNum = Info[2]
    QubitName = Info[3]
    ClassicName = Info[4]
    GapNum = GateNum+QubitNum
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 1
    result = []
    CurrentQubit = 0
    while MutationNum != GapNum*len(QuantumGates.OneQubit):
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Add" +str(MutationNum) + "." + path[1]
        f = open(origin)
        g = open(newPath, "w")
        result.insert(MutationNum, str(newPath))
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if temp2[0] in QuantumGates.OneQubit:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap:
                        if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                            g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                                    "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
                        else:
                            g.write(str(CircuitName)+"."+str(QuantumGates.OneQubit[CurrentGate])+"("+str(temp2[1]))
                        Mutated = True
                        g.write("\n")
            g.write(line)
            line = f.readline()
        if (ObjectiveGap >= GateNum) and (Mutated is False):
            g.write("\n")
            if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                        "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(QubitName) + "[" + str(CurrentQubit) + "]" + ")")
            else:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(QubitName) + "[" + str(CurrentQubit) + "]" + ")")
            g.write("\n")
        x = 0
        while x < QubitNum:
            g.write(
                str(CircuitName) + ".measure(" + str(QubitName) + "[" + str(x) + "], " + str(ClassicName) + "[" + str(x) + "])")
            g.write("\n")
            x = x + 1
        g.write("simulator = Aer.get_backend('qasm_simulator')")
        g.write("\n")
        g.write("job = execute(" + str(CircuitName) + ", simulator, shots=" + str(QuantumGates.numShots) + ")")  ##execute for 10 times
        g.write("\n")
        # Grab results from the job
        g.write("result = job.result()")
        g.write("\n")
        # Returns counts
        g.write("counts = result.get_counts(" + str(CircuitName) + ")")
        g.write("\n")
        g.write("print(counts)")
        g.write("\n")
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit)-1:
            if (ObjectiveGap > GateNum):
                CurrentQubit = CurrentQubit + 1
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0

        else:
            CurrentGate = CurrentGate + 1

    print("The ADD mutated files are located in: " + dirpath)
    return result


def removeOLD(origin):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    path = origin.split(".")
    path2 = path[0].split(chr(splitChar))
    directories = origin.split(chr(splitChar))
    dirpath = ""
    directories[len(directories) - 1] = "RemoveMutations"
    for x in directories:
        if x == directories[0]:
            dirpath = dirpath + x
        else:
            dirpath = dirpath + chr(splitChar) + x
    os.mkdir(dirpath)
    path[0] = dirpath + chr(splitChar) + path2[len(path2) - 1]
    Info = getInfo(origin)
    QubitNum = Info[0]
    CircuitName = Info[1]
    GateNum = Info[2]
    QubitName = Info[3]
    ClassicName = Info[4]
    MutationNum = 0
    ObjectiveGap = 1
    result = []
    while MutationNum != GateNum:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Remove" + str(MutationNum) + "." + path[1]
        result.insert(MutationNum, str(newPath))
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if temp2[0] in QuantumGates.AllGates:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap:
                        Mutated = True
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()
        x = 0
        while x < QubitNum:
            g.write(
                str(CircuitName) + ".measure(" + str(QubitName) + "[" + str(x) + "], " + str(ClassicName) + "[" + str(x) + "])")
            g.write("\n")
            x = x + 1
        g.write("simulator = Aer.get_backend('qasm_simulator')")
        g.write("\n")
        g.write("job = execute(" + str(CircuitName) + ", simulator, shots=" + str(QuantumGates.numShots) + ")")  ##execute for 10 times
        g.write("\n")
        # Grab results from the job
        g.write("result = job.result()")
        g.write("\n")
        # Returns counts
        g.write("counts = result.get_counts(" + str(CircuitName) + ")")
        g.write("\n")
        g.write("print(counts)")
        g.write("\n")
        f.close()
        g.close()
        ObjectiveGap = ObjectiveGap + 1

    print("The REMOVE mutated files are located in: " + dirpath)
    return result


def replaceOLD(origin):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    path = origin.split(".")
    path2 = path[0].split(chr(splitChar))
    directories = origin.split(chr(splitChar))
    dirpath = ""
    directories[len(directories) - 1] = "ReplaceMutations"
    for x in directories:
        if x == directories[0]:
            dirpath = dirpath + x
        else:
            dirpath = dirpath + chr(splitChar) + x
    os.mkdir(dirpath)
    path[0] = dirpath + chr(splitChar) + path2[len(path2) - 1]
    Info = getInfo(origin)
    QubitNum = Info[0]
    CircuitName = Info[1]
    GateNum = Info[2]
    QubitName = Info[3]
    ClassicName = Info[4]
    GapNum = GateNum + QubitNum
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 1
    result = []
    while MutationNum != GateNum * (len(QuantumGates.OneQubit)-1):
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Replace" + str(MutationNum) + "." + path[1]
        result.insert(MutationNum, str(newPath))
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if temp2[0] in QuantumGates.OneQubit:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap:
                        if QuantumGates.OneQubit[CurrentGate] == temp2[0]:
                            CurrentGate = CurrentGate + 1
                        if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                            g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                                    "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
                        else:
                            g.write(
                                str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
                        Mutated = True
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()
        if (ObjectiveGap == GapNum) and (Mutated is False):
            g.write("\n")
            if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                        "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
            else:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
        x = 0
        while x < QubitNum:
            g.write(str(CircuitName) + ".measure(" + str(QubitName) + "[" + str(x) + "], " + str(ClassicName) + "[" + str(x) + "])")
            g.write("\n")
            x = x + 1
        g.write("simulator = Aer.get_backend('qasm_simulator')")
        g.write("\n")
        g.write("job = execute(" + str(CircuitName) + ", simulator, shots=" + str(QuantumGates.numShots) + ")")  ##execute for 10 times
        g.write("\n")
        # Grab results from the job
        g.write("result = job.result()")
        g.write("\n")
        # Returns counts
        g.write("counts = result.get_counts(" + str(CircuitName) + ")")
        g.write("\n")
        g.write("print(counts)")
        g.write("\n")
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit) - 1:
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("The REPLACE mutated files are located in: " + dirpath)
    return result


def getInfo(origin):

    f = open(origin)
    line = f.readline()
    GateNum = 0
    CircuitName = "Null"
    QubitName = "Null"
    ClasicName = "Null"
    while line != "":
        if "QuantumRegister(" in line:
            temp = line.split("(")
            temp2 = temp[1].split(",")
            temp3 = temp[0].split(" ")
            QubitName = temp3[0]
            QubitNum = int(temp2[0])
        elif "QuantumCircuit(" in line:
            temp = line.split(" ")
            CircuitName = temp[0]
        elif (CircuitName in line) and CircuitName != "Null":
            temp = line.split(".")
            temp2 = temp[1].split("(")
            if temp2[0] in QuantumGates.OneQubit:
                GateNum = GateNum + 1

        elif "ClassicalRegister(" in line:
            temp = line.split(" ")
            ClasicName = temp[0]
        line = f.readline()
    f.close()
    return QubitNum, CircuitName, GateNum, QubitName, ClasicName
