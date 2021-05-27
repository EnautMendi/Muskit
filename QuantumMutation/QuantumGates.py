
AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx", "cswap") #All gates that are implemented
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") #Gates that only affect one qubit
ManyQubit = ("swap", "rzz", "rxx", "cx", "cz") #Gates that affect two qubit
MoreThanTwoQubit = ("ccx", "cswap") #Gates that affect more than two qubit
PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") #Gates that affect the phase and needs to specify a phase

