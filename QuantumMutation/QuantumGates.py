
AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx") #All gates that are implemented
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") #Gates that only affect one qubit
ManyQubit = ("swap", "rzz", "rxx", "cx", "cz", "ccx") #Gates that affect many qubit
MoreThanTwoQubit = ("ccx",) #Gates that affect more than two qubit
PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") #Gates that affect the phase and needs to specify a phase

