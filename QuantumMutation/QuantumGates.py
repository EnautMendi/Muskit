import math

AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx") #All gates that are implemented
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") #Gates that only affect one qubit
ManyQubit = ("swap", "rzz", "rxx") #Gates that affect many qubit
PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") #Gates that affect the phase and needs to specify a phase
phases = [0, (math.pi/4), (math.pi/2), math.pi] #Phase number that is going to select randomly
inputs = ("001","101","110")