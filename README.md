# Muskit: A Mutation Analysis Tool for Quantum Software Testing

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/logoblue.png" width="200">

# Description
Quantum software testing is a new area of research. Thus, there is a lack of benchmark programs and bugs repositories to assess the effectiveness of testing techniques. To this end, quantum mutation analysis focuses on systematically generating a set of faulty versions of quantum programs, called mutants, using mutation operators. Such faulty versions of quantum programs can be used as benchmarks to assess the quality of test cases in a test suite. Here, we host a tool called Muskit -- a quantum mutation analysis tool for quantum programs coded in IBM's Qiskit language. Muskit implements  a set of mutation operators on gates of quantum programs and a set of selection criteria to reduce the number of mutants to generate. Moreover, it allows for the execution of test cases on mutants and generation of results for test analyses. Muskit is provided as a command line application, a GUI application, and also as a web application. 
A preprint of the paper describing Muskit and its feature can be download from <a href="">here</a>.


# Architecture of Muskit


<!---
your comment goes here
and here
![Architecture](https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png)

-->

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png" width="500">

# Extension
Muskit can be extended in two ways: 
- A light-weight extension mechanism, where one can specify new gates in the configuration file (QuantumGates.py). This file is read by Muskit to generate mutants. Any newly added gate in the file will be used by Muskit to generate mutants. 
- Second, one can checkout the code from GitHub and provide extensions to Muskit.

# How to use
## Assumptions:
- Mutants are for quantum circuits thus, Muskit works only with quantum circuits in the code. 
- The code has to be structured in a sequential way without any function definition, main, or sub functions. 
- The qubits should be declared once. 
- In order to measure all the qubits correctly, an equal number of clasical bits must be defined. 

A sample cicuit is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/ExampleProgram.py"> here </a>.

## Configuration Files
- QuantumGate.py has two purposes: 1) It can be used to configure Muskit to use quantum gates to be used in MutantsGenerator; 2) To specify newly implemented gates to be used by Muskit. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/QuantumGates.py"> here </a>. 
- generatorConfig.py is the configuration file for the MutantsGenerator component. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/generatorConfig.py">here </a>.
- executorConfig.py is the configuration file for the MutantsExecutor component. A sample file is available <a href=https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/executorConfig.py>here </a>.
- analyzerConfig.py. A configuration file for Test Analyzer. A sample file is available <a href="">here</a>.
Note that within each file, we provide more details for variable and its possible valid values.

## Test Cases
- testcase.py to specify test cases. A sample is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/testCases.py">here </a>
- ProgramSpecifications required for test analzyer. A smaple file is available <a href="">here</a>.

## Command Line
- Command 1
- Command 2

## GUI
- A screenshot of the GUI is available below:
<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/gui.png" width="600">

The GUI has two main panels, one for mutants generation and the second for mutants execution.
- Mutants Generation: A user can: 1) Specify the quantum program, whose mutants will be generated; 2) destination where the generated mutants will be output; 3) Various selection criteria that can be used by Muskit to generate mutants. Through the GUI, one can select a) all mutants; b) set a limit on maximum number of mutants to be generated; c) selection based on operator types (i.e., add, remove, or delete); d) selection based on gate tyes (one qubit or multiple qubit); e) selection of exact gates on a circuit for replace and deleting, f) selection a location to add new gates.
- Mutants Execution: A user can '1) Select the mutants to be executed; 2) Specify the location, where the results will be saved ; 3) Number of repetitions for each test case; 4) Specify test cases.

In addition a user can also specify the gates (e.g., hadmard, CNOT, etc) in the QuantumGate.py file to instruct Muskit, which gates to be used for mutants generation.

## Online
An online version of Muskit is available here: <a href="https://qiskitmutantcreatorsrl.pythonanywhere.com/"> Web Application </a>
The online only allows a user to generate mutants and execution is not supported. For generation, a user can:  1) Specify the quantum program, whose mutants will be generated; 3) Various selection criteria that can be used by Muskit to generate mutants. One can select a) all mutants; b) set a limit on maximum number of mutants to be generated; c) selection based on operator types (i.e., add, remove, or delete); d) selection based on gate tyes (one qubit or multiple qubit). 
A screenshot is available here:
<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/web.png" width="600">


# Video Demonstration
Video demo is available <a href=""> here</a>.

# Experimental Data
Experimental data including quantum programs, and program specifications can be downloaded <a href=""> here</a>. 



