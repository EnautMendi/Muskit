import math

AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx")
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx")
PhaseGates = ("p", "rx", "ry", "rz")
ManyQubit = ("CONTROL", "SWAP")
phases = [0, (math.pi/4), (math.pi/2), math.pi]
numShots = 10
