import math

AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx")
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx")
ManyQubit = ("swap", "rzz", "rxx")
PhaseGates = ("p", "rx", "ry", "rz")
phases = [0, (math.pi/4), (math.pi/2), math.pi]
numShots = 10
