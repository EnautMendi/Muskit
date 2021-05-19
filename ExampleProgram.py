import qiskit
from qiskit import *
import math

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.id(qreg_q[1])
circuit.swap(qreg_q[2],qreg_q[1])
circuit.p(pi,qreg_q[1])
circuit.cx(qreg_q[1],qreg_q[0])
