import QuantumGates


def execute(origin):
    f = open(origin)
    f.close()
    return 0


def add(origin):
    path = origin.split(".")
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
                        g.write(str(CircuitName)+"."+str(QuantumGates.OneQubit[CurrentGate])+"("+str(temp2[1]))
                        Mutated = True
            g.write(line)
            line = f.readline()
        if (ObjectiveGap == GapNum) and (Mutated is False):
            g.write("\n")
            g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit)-1:
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("Add mutation files created: ")
    print(MutationNum)
    return 1


def remove(origin):
    path = origin.split(".")
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

    print("Remove mutation files created: ")
    print(MutationNum)
    return 1


def replace(origin):
    path = origin.split(".")
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
                        g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
                        Mutated = True
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()
        if (ObjectiveGap == GapNum) and (Mutated is False):
            g.write("\n")
            g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
        f.close()
        g.close()
        if CurrentGate == len(QuantumGates.OneQubit) - 1:
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("Replace mutation files created: ")
    print(MutationNum)
    return 1


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
