import QuantumGates
import random
import os


def createMutants(maxNum, operators, types, gateIDs, gapIDs, originPath, savePath, all):
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
    if "Add" in operators:
        num = restquantity / len(operators)
        rest = restquantity % len(operators)
        addnum = num + rest
        if addnum > GapNum * len(gates):
            addnum = GapNum * len(gates)
        if all == True:
            addnum = GapNum * len(gates)
        restquantity = restquantity - addnum
        totalMutants = totalMutants + add(addnum, gates, gapIDs, originPath, savePath)
        first = False
    if "Remove" in operators:
        if first == True:
            num = restquantity / len(operators)
            rest = restquantity % len(operators)
            removenum = num + rest
            if removenum > gateNum:
                removenum = gateNum
            if all == True:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
        else:
            removenum = restquantity / (len(operators) - 1)
            if removenum > gateNum:
                removenum = gateNum
            if all == True:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
    if "Replace" in operators:
        replacenum = restquantity
        if replacenum > (gateNum * len(gates))-gateNum:
            replacenum = (gateNum * len(gates))-gateNum
        if all == True:
            replacenum = (gateNum * len(gates)) - gateNum
        totalMutants = totalMutants + replace(replacenum, gates, gateIDs, originPath, savePath)


    print("Number of mutants created: " + str(totalMutants))

def createInputs(QubitNum):
    inputs = ("",)
    x = 0
    while x < 2 ** QubitNum:
        binariInput = str(bin(x))
        binariInput = binariInput[2:len(binariInput)]
        if len(binariInput) < QubitNum:
            y = len(binariInput)
            tmp = ""
            while y < QubitNum:
                tmp = tmp + str(0)
                y = y + 1
            binariInput = tmp + binariInput
        inputs = inputs + (binariInput,)
        x = x + 1
    return inputs[1:len(inputs)]

def executeMutants(files, resultPath, numShots, allInputs):
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
        if allInputs == True:
            inputs = createInputs(QubitNum)
        else:
            inputs = QuantumGates.inputs
        for init in inputs:
            f = open(files[x])
            g = open(tmpPath, "w")
            line = f.readline()
            y=0
            while line != "":
                g.write(line)
                if "QuantumCircuit" in line:
                    g.write("\n")
                    z=1
                    while z <= len(init):
                        if init[z-1]=="1":
                            g.write(str(CircuitName) + ".x(" + str(QubitName) + "[" + str(QubitNum-z) + "])")
                            g.write("\n")
                        z = z + 1
                line = f.readline()
            g.write("\n")
            while y < QubitNum:
                g.write(
                    str(CircuitName) + ".measure(" + str(QubitName) + "[" + str(y) + "], " + str(ClassicName) + "[" + str(y) + "])")
                g.write("\n")
                y = y + 1
            g.write("simulator = Aer.get_backend('qasm_simulator')")
            g.write("\n")
            g.write("job = execute(" + str(CircuitName) + ", simulator, shots=" + str(numShots) + ")")  ##execute for 10 times
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
            g.write("r.write(" + chr(34)+ "The result of " + files[x] + "with input [" + str(init) +"] is: " + chr(34) + " + str(counts))")
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


def add(max, gateTypes, Gaps, origin, dirPath):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    dirPath = dirPath + chr(splitChar) + "AddMutations"
    os.mkdir(dirPath)
    Info = getInfo(origin)
    QubitNum = Info[0]
    CircuitName = Info[1]
    TotalGateNum = Info[2]
    QubitName = Info[3]
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 0
    while ObjectiveGap not in Gaps:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum < max:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + "Add" + str(MutationNum) + ".py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if ((CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False)):
                temp = line.split(".")
                temp2 = temp[1].split("(")
                if ObjectiveGap > TotalGateNum:
                    temp2 = QubitName + "[" + str(ObjectiveGap-TotalGateNum-1) + "]"
                if temp2[0] in QuantumGates.AllGates:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap:
                        if gateTypes[CurrentGate] in QuantumGates.ManyQubit:
                            if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                if temp2[0] in QuantumGates.ManyQubit:
                                    if temp2[0] in QuantumGates.PhaseGates:
                                        temp3=temp2[1].split(",",1)
                                        g.write(str(CircuitName) + "." + str(
                                            gateTypes[CurrentGate]) + "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases) - 1)]) + "," + str(temp3[1]))
                                        Mutated = True
                                    else:
                                        g.write(str(CircuitName) + "." + str(
                                            gateTypes[CurrentGate]) + "(" + str(QuantumGates.phases[
                                                                                                random.randint(0, len(
                                                                                                    QuantumGates.phases) - 1)]) + "," + str(
                                            temp2[1]))
                                        Mutated = True
                                else:
                                    temp3 = temp2[1].split(",")
                                    temp4 = temp3[len(temp3) - 1].split("[")
                                    temp4 = temp4[1].split("]")
                                    num = int(temp4[0])
                                    if num == QubitNum:
                                        num = num - 1
                                    else:
                                        num = num + 1
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                            QuantumGates.phases[
                                                random.randint(0, len(QuantumGates.phases) - 1)]) + ", " + str(
                                            QubitName) + "[" + str(num) + "]" ", " + str(temp3[len(temp3) - 1]))
                                    Mutated = True

                            else:
                                if temp2[0] in QuantumGates.ManyQubit:
                                    if temp2[0] in QuantumGates.PhaseGates:
                                        temp3 = temp2[1].split(",", 1)
                                        g.write(str(CircuitName) + "." + str(
                                            gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                        Mutated = True
                                    else:
                                        g.write(str(CircuitName) + "." + str(
                                            gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                        Mutated = True
                                else:
                                    temp3 = temp2[1].split(",")
                                    temp4 = temp3[len(temp3) - 1].split("[")
                                    temp4 = temp4[1].split("]")
                                    num = int(temp4[0])
                                    if num == QubitNum:
                                        num = num - 1
                                    else:
                                        num = num + 1
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                            QubitName) + "[" + str(num) + "]" ", " + str(temp3[len(temp3) - 1]))
                                    Mutated = True
                        else:
                            if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                temp3 = temp2[1].split(",")
                                g.write(
                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases) - 1)]) + "," + str(temp3[len(temp3) - 1]))
                                Mutated = True
                            else:
                                temp3 = temp2[1].split(",")
                                g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                    temp3[len(temp3) - 1]))
                                Mutated = True
            g.write(line)
            line = f.readline()
            if Mutated is False and line == "":
                qubit = ObjectiveGap - TotalGateNum - 1
                if qubit == QubitNum - 1:
                    qubit2 = qubit - 1
                else:
                    qubit2 = qubit + 1
                if gateTypes[CurrentGate] in QuantumGates.ManyQubit:
                    if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                            QuantumGates.phases[random.randint(0, len(QuantumGates.phases) - 1)]) + "," + str(
                            QubitName) + "[" + str(
                            qubit2) + "]" + "," + str(
                            QubitName) + "[" + str(
                            qubit) + "]" + ")")
                        Mutated = True
                    else:
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                            QubitName) + "[" + str(
                            qubit2) + "]" + "," + str(
                            QubitName) + "[" + str(
                            qubit) + "]" + ")")
                        Mutated = True
                else:
                    if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(QuantumGates.phases[random.randint(0, len(QuantumGates.phases) - 1)]) + "," + str(QubitName) + "[" + str(
                            qubit) + "]" + ")")
                        Mutated = True
                    else:
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(QubitName) + "[" + str(qubit)+ "]" + ")")
                        Mutated = True

        f.close()
        g.close()
        if CurrentGate >= len(gateTypes) - 1:
            ObjectiveGap = ObjectiveGap + 1
            while (ObjectiveGap not in Gaps) and (ObjectiveGap < Gaps[(len(Gaps) - 1)]):
                ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1



    print("The ADD mutated files are located in: " + dirPath)
    return MutationNum



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
                            if CurrentGate >= len(gateTypes):
                                ObjectiveGap = ObjectiveGap + 1
                                while (ObjectiveGap not in changeGates) and (
                                        ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                    ObjectiveGap = ObjectiveGap + 1

                                if ObjectiveGap > changeGates[(len(changeGates)-1)]:
                                    delete = True
                                CurrentGate = 0
                        if temp2[0] in QuantumGates.ManyQubit or gateTypes[CurrentGate] in QuantumGates.ManyQubit:
                            if temp2[0] in QuantumGates.ManyQubit and gateTypes[CurrentGate] in QuantumGates.ManyQubit:
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
                            else:
                                if temp2[0] in QuantumGates.ManyQubit:
                                    while gateTypes[CurrentGate] not in QuantumGates.ManyQubit:
                                        CurrentGate = CurrentGate + 1
                                    if gateTypes[CurrentGate] == temp2[0]:
                                        CurrentGate = CurrentGate + 1
                                    if temp2[0] in QuantumGates.PhaseGates:
                                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                        else:
                                            temp3 = temp2[1].split(",")
                                            qubits = temp3[1]
                                            for x in temp3:
                                                if x != temp3[0] and x != temp3[1]:
                                                    qubits = qubits + "," + x
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(qubits))
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
                            if CurrentGate < len(gateTypes)-1:
                                if gateTypes[CurrentGate+1] in QuantumGates.ManyQubit:
                                    ObjectiveGap = ObjectiveGap + 1
                                    while (ObjectiveGap not in changeGates) and (
                                            ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                        ObjectiveGap = ObjectiveGap + 1
                                    CurrentGate = -1
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
            CurrentGate = CurrentGate - 1
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

def getInfo(origin):
    x=0
    gates = ("",)
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
            temp3 = temp2[1].split("[")
            temp4 = temp3[len(temp3)-1].split("]")
            if temp2[0] in QuantumGates.AllGates:
                GateNum = GateNum + 1
                gate = str(GateNum) + " Gate: " + temp2[0] + " in Qubit " + temp4[0]
                if GateNum == 1:
                    gates = (gate,)
                else:
                    gates = gates + (gate,)

        elif "ClassicalRegister(" in line:
            temp = line.split(" ")
            ClasicName = temp[0]
        line = f.readline()
    while x < QubitNum:
        gates = gates + ((str(GateNum+x+1) + " Qubit " + str(x)) + " Last Gap",)
        x = x + 1
    f.close()
    return QubitNum, CircuitName, GateNum, QubitName, ClasicName, gates
