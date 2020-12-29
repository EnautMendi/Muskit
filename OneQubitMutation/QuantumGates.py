import math


OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx")
PhaseGates = ("p", "rx", "ry", "rz")
ManyQubit = ("CONTROL", "SWAP")
phases = [0, (math.pi/4), (math.pi/2), math.pi]

# Dictionary= "name" : "QiskitCode"
GatesDictionary = {
    "X": ".x()",
    "H": ".h()",
    "P": ".p()",
    "T": ".t()",
    "S": ".s()",
    "Z": ".z()",
    "Y": ".y()",
    "I": ".id()",
    "RX": ".rx()",
    "RY": ".ry()",
    "RZ": ".rz()",
    "SX": ".sx()",
    "CONTROL NOT": ".cx()",
    "SWAP": ".swap()"
}