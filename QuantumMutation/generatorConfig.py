import math
#Mutant creation variables
maxNumberOfMutants = 100 #Max number of mutants
operators = ("Add","Replace") #Type of operators are going to use to create mutants
types = ("OneQubit",) #Types of gates the mutation will change
gateNum = (1,3) #IDNumber of the gates that mutation is going to change
gapNum = (1,5) #IDNumber of the gaps that mutation is going to change
phases = [0,0.7,1.5,3] #Phase number that is going to select randomly
allMutants = False #If this true the program will ignore all the other criteria


