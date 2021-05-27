import math
#Mutant creation variables
maxNumberOfMutants = 100 #Max number of mutants
operators = ("ADD","REPLACE")       #Type of operators are going to use to create mutants
types = ("OneQubit",)            #Types of gates the mutation will change
gateNum = (1,3)          #IDNumber of the gates that mutation is going to change
gapNum = (1,5)           #IDNumber of the gaps that mutation is going to change
phases = [0, (math.pi/4), (math.pi/2), math.pi] #Phase number that is going to select randomly
allMutants = True        #If this true the program will ignore all the other criteria


