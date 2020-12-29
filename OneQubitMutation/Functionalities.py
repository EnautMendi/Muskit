import QuantumGates
import random
import os

def execute(files):

    for x in files:
        command = "python3 " + x
        os.system(command)
    return

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
    QubitName = Info[3]
    ClassicName = Info[4]
    GapNum = GateNum+QubitNum
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 1
    result = []
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
        if (ObjectiveGap == GapNum) and (Mutated is False):
            g.write("\n")
            if QuantumGates.OneQubit[CurrentGate] in QuantumGates.PhaseGates:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) +
                        "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases)-1)]) + "," + str(temp2[1]))
            else:
                g.write(str(CircuitName) + "." + str(QuantumGates.OneQubit[CurrentGate]) + "(" + str(temp2[1]))
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
            ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("The ADD mutated files are located in: " + dirpath)
    return result


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
                if temp2[0] in QuantumGates.OneQubit:
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
