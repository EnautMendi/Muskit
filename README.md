# Muskit: A Mutation Analysis Tool for Quantum Software Testing

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/logoblue.png" width="200">

# Description
Quantum software testing is a new area of research. Thus, there is a lack of benchmark programs and bugs repositories to assess the effectiveness of testing techniques. To this end, quantum mutation analysis focuses on systematically generating a set of faulty versions of quantum programs, called mutants, using mutation operators. Such faulty versions of quantum programs can be used as benchmarks to assess the quality of test cases in a test suite. Here, we host a tool called Muskit -- a quantum mutation analysis tool for quantum programs coded in IBM's Qiskit language. Muskit implements  a set of mutation operators on gates of quantum programs and a set of selection criteria to reduce the number of mutants to generate. Moreover, it allows for the execution of test cases on mutants and generation of results for test analyses. Muskit is provided as a command line application, a GUI application, and also as a web application. 


# Architecture of Muskit


<!---
your comment goes here
and here
![Architecture](https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png)

-->

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png" width="500">

# Extension
Muskit is provided with two types of extensions. 
- A light-weight extension mechanism, where one can specify new gates in the configuration file (QuantumGates.py). This file is read by Muskit to generate mutants. Any newly added gate in the file will be used by Muskit to generate mutants. 
- Second, one can checkout the code from GitHub and provide extensions to Muskit.

# How to use
## Assumptions:
- Mutants are for quantum circuits thus, Muskit works only with quantum circuits. 
- The code has to be structured in a secuential way without any function definition, main, or sub functions. T
- The qubits and should be declared in once and in order to measure all the Qubits correctly the clasical bits has to be the same number as Qubits. 

A sample cicuit is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/ExampleProgram.py"> here </a>.

## Configuration Files
- QuantumGate.py to select quantum gates to be used in MutantsGenerator or to specify new gates to be used by Muskit. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/QuantumGates.py"> here </a>. 
- generatorConfig.py is the configuration file for MutantsGenerator component. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/generatorConfig.py">here </a>.
- executorConfig.py is the configuration file for the MutantsExecutor. A sample file is available <a href=https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/executorConfig.py>here </a>.
- analyzerConfig.py. A sample file is available <a href="">here</a>.


## Test Cases
- testcase.py to specify test cases. A sample is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/testCases.py">here </a>
- ProgramSpecifications...

## Command Line
- Command 1
- Command 2

## GUI
- Screenshot

## Online
- <a href="https://qiskitmutantcreatorsrl.pythonanywhere.com/"> Web Application </a>

# Video Demonstration
Video demo is available here

# Experimental Data
Experimental data including quantum programs, and program specifications can be downloaded <a href=""> here</a>. 



