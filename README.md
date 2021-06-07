# Muskit: A Mutation Analysis Tool for Quantum Software Testing

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/logoblue.png" width="200">

# Description
Quantum software testing is a new area of research. Thus, there is a lack of benchmark programs and bugs repositories to assess the effectiveness of testing techniques. To this end, quantum mutation analysis focuses on systematically generating a set of faulty versions of quantum programs, called mutants, using mutation operators. Such faulty versions of quantum programs can be used as benchmarks to assess the quality of test cases in a test suite. Here, we host a tool called Muskit -- a quantum mutation analysis tool for quantum programs coded in IBM's Qiskit language. Muskit implements a set of mutation operators on gates of quantum programs and a set of selection criteria to reduce the number of mutants to generate. Moreover, it allows for the execution of test cases on mutants and generation of results for test analyses. Muskit is provided as a command line application, a GUI application, and also as a web application. 
A preprint of the paper describing Muskit and its features can be download from <a href="">here</a>.


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

# How to use Muskit?
## Assumptions:
- Mutants are for quantum circuits, thus Muskit works only with quantum circuits in the code. 
- The code has to be structured in a sequential way without any function definition, main, or sub functions. 
- The qubits should be declared once. 
- In order to measure all the qubits correctly, an equal number of classical bits must be defined. 

A sample circuit is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/ExampleProgram.py"> here </a>.

### Configuration Files
The main configuration files are described below. Note that within each file, we provide more details for variable and its possible valid values.

#### QuantumGate.py
QuantumGate.py has two purposes: 1) It can be used to configure Muskit to use quantum gates to be used in MutantsGenerator; 2) To specify newly implemented gates to be used by Muskit. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/QuantumGates.py"> here </a>. 

One can specify the gates in the following five categories:

- AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx", "cswap") # All the gates that are currently supported
- OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") # All the supported gates that affect one qubit
- ManyQubit = ("swap", "rzz", "rxx", "cx", "cz") # All the supported gates that affect two qubits
- MoreThanTwoQubit = ("ccx", "cswap") # All the supported gates that affect more than two qubits
- PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") # All the supported gates that affect the phases of qubits requires a user to specify exact phase value to be used, i.e., a value between 0.0 to 360.0

A user can consult Qiskit documentation to read about description of each of the gates <a href="https://qiskit.org/documentation/">here</a>. 

#### generatorConfig.py

This configuration file provides instructions to the MutantsGenerator component. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/generatorConfig.py">here </a>.

In particular, it allows a user to provide various selection criteria that will be taken into account while generating mutants. One can select 1) all mutants; 2) set a limit on maximum number of mutants to be generated; 3) selection based on operator types (i.e., add, remove, or delete); 4) selection based on gate types (one qubit or multiple qubit); 5) selection of exact gates on a circuit for replace and deleting, 6) selection a location to add new gates.

#### executorConfig.py
- This configuration provides instructions to the MutantsExecutor component that will be taken into account for executing the mutants. A sample file is available <a href=https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/executorConfig.py>here </a>.

In particular, one can specify the number of times a test case must be executed to account for probabilistic nature of quantum programs. Also, a user can set a variable, i.e., allInputs to true, if the user does not have the test cases to be executed. In this case, a mutant will be executed with all possible inputs, i.e., All Input Coverage criteria. If this variable is set to false, then a user must specify test cases in testcase.py file.

#### analyzerConfig.py
This is a configuration file for Test Analyzer. A sample file is available <a href="">here</a>.

In particular, one needs to specify a chosen significance level for a statistical test, e.g., p-value=0.05. In addition, a user also has to specify the qubits that should be used as inputs and also the qubits that should be measured. 

### Program Specification and Test Cases

#### testcase.py 
In this file, one can specify the test cases to be executed by Muskit on mutants. A test case is simply the initialization of circuit.  A sample is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/testCases.py">here </a>

The format is: inputs = ("001","101","110"), where we have three test case 001, 101, and 110 that will be used for testing.

#### ProgramSpecifications 
This file is required for test analyzer to determine killing of a mutant with a test case. A sample file is available <a href="">here</a>.
Simply, we specify, for each input its corresponding outputs with their associated expected probabilities. 

To determine whether a mutant is killed, Muskit implements two types of test oracles from <a href="https://ieeexplore.ieee.org/abstract/document/9438603"> Quito </a>: 1) Whether an observed output is correct according to program specification. If not, the mutant is killed; 2) If all the observed outputs corresponding to an input are valid, then we compare their observed probabilities with the ones specified in the Program Specification file. If the differences are statistically significant (i.e., a p-value lower than the chosen significance level), the mutant is killed.

# Muskit Implementations

Muskit is available in the following three implementations described below:

## Command Line
The command line version has all the features supported and it is more flexible to be used for experimentation. In particular, the following two commands are used.

- Mutants Generation: Command 1
- Mutants Execution: Command 2

Through the configuration files described above, users can configure both mutant generator and mutants executor for their specific needs. 

## GUI
- A screenshot of the GUI is available below:
<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/gui.png" width="600">

The GUI has two main panels, one for mutants generation and the second for mutants execution.
- Mutants Generation: A user can: 1) Specify the quantum program, whose mutants will be generated; 2) destination where the generated mutants will be output; 3) Various selection criteria that can be used by Muskit to generate mutants. Through the GUI, one can select a) all mutants; b) set a limit on maximum number of mutants to be generated; c) selection based on operator types (i.e., add, remove, or delete); d) selection based on gate types (one qubit or multiple qubit); e) selection of exact gates on a circuit for replace and deleting, f) selection a location to add new gates.
- Mutants Execution: A user can '1) Select the mutants to be executed; 2) Specify the location, where the results will be saved ; 3) Number of repetitions for each test case; 4) Specify test cases.

In addition, a user can also specify the gates (e.g., hadmard, CNOT, etc) in the QuantumGate.py file to instruct Muskit, which gates to be used for mutants generation.

## Online
An online version of Muskit is available here: <a href="https://qiskitmutantcreatorsrl.pythonanywhere.com/"> Web Application </a>
The online only allows a user to generate mutants and execution is not supported. For generation, a user can:  1) Specify the quantum program, whose mutants will be generated; 3) Various selection criteria that can be used by Muskit to generate mutants. One can select a) all mutants; b) set a limit on maximum number of mutants to be generated; c) selection based on operator types (i.e., add, remove, or delete); d) selection based on gate types (one qubit or multiple qubit). 
A screenshot is available here:

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/web.png" width="600">


# Video Demonstration
Video demo is available <a href=""> here</a>.

# Experimental Data
Experimental data including quantum programs, and program specifications can be downloaded <a href=""> here</a>. 



