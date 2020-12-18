OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx")
ManyQubit = ("CONTROL", "SWAP")

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