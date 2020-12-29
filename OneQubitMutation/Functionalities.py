import QuantumGates
import random
import os


def add(origin):
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
    GapNum = GateNum+QubitNum
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 1
    while MutationNum != GapNum*len(QuantumGates.OneQubit):
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Add" +str(MutationNum) + "." + path[1]
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
                        if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                            g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                                    "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
                        else:
                            g.write(str(CircuitName)+"."+str(QuantumGates.OneQubit[CurrentGate])+"("+str(temp2[1]))
                        Mutated = True
                        g.write("\n")
            g.write(line)
            line = f.readline()
        if (ObjectiveGap == GapNum) and (Mutated is False):
            g.write("\n")
            if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                        "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
            else:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit)-1:
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("The ADD mutated files are located in: " + dirpath)
    return MutationNum


def remove(origin):
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
    CircuitName = Info[1]
    GateNum = Info[2]
    MutationNum = 0
    ObjectiveGap = 1
    while MutationNum != GateNum:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Remove" + str(MutationNum) + "." + path[1]
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
                        Mutated = True
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()
        f.close()
        g.close()
        ObjectiveGap = ObjectiveGap + 1

    print("The REMOVE mutated files are located in: " + dirpath)
    return MutationNum


def replace(origin):
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
    GapNum = GateNum + QubitNum
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 1
    while MutationNum != GateNum * (len(QuantumGates.OneQubit)-1):
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = path[0] + "Replace" + str(MutationNum) + "." + path[1]
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
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit) - 1:
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("The REPLACE mutated files are located in: " + dirpath)
    return MutationNum


def getInfo(origin):

    f = open(origin)
    line = f.readline()
    GateN = 0
    CircuitName = "Null"
    while line != "":
        if "QuantumRegister(" in line:
            temp = line.split("(")
            temp2 = temp[1].split(",")
            QubitN = int(temp2[0])
        elif "QuantumCircuit(" in line:
            temp = line.split(" ")
            CircuitName = temp[0]
        elif (CircuitName in line) and CircuitName != "Null":
            temp = line.split(".")
            temp2 = temp[1].split("(")
            if temp2[0] in QuantumGates.OneQubit:
                GateN = GateN + 1

        line = f.readline()
    f.close()
    return QubitN, CircuitName, GateN
