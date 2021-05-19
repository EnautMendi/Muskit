import math
#Mutant creation variables
maxNumberOfMutants = 100
operators = ("",)       #Type of operators are going to use to create mutants
types = ("",)            #Types of gates the mutation will change
gateNum = (1,)          #IDNumber of the gates that mutation is going to change
gapNum = (1,)           #IDNumber of the gaps that mutation is going to change
phases = [0, (math.pi/4), (math.pi/2), math.pi] #Phase number that is going to select randomly
allMutants = True

#Mutant execution variables
numShots = 100
allInputs = True
inputs = ("001","101","110")

