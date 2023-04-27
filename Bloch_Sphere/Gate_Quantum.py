from manim import *

from numpy import matrix
import math 
import cmath


#Qubit transformation matrices
I = matrix([[1+0j,0],[0,1]]) #Inverse
H = 1/math.sqrt(2) * matrix( [[1+0j,1],[1,-1]]) #Hadamard
X = matrix([[0,1+0j],[1,0]]) #PauliX
Y = matrix([[0,-1j],[1j,0]]) #PauliY
Z = matrix([[1+0j,0],[0,-1]]) #PauliZ
S = matrix([[1+0j,0],[0,1j]]) #Phase
T = matrix([[1,0],[0, math.exp(1j*(math.pi/4))]]) #PI/8
sN = 1/math.sqrt(2) * matrix( [[1+0j,-1],[1,1]]) #Sqrt Not

class QubitGate(Scene):
    def construct(self):
        # Create qubit basis vectors
        ket_0 = MathTex(r"|0\rangle").scale(1.5)
        ket_1 = MathTex(r"|1\rangle").scale(1.5)
        qubit_basis = VGroup(ket_0, ket_1).arrange(DOWN, buff=1)
        self.play(Create(qubit_basis))
        # Define X gate
        x_gate = MathTex(r"X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}").scale(1.5)
        x_gate.to_edge(RIGHT)
        self.play(Create(x_gate))
        
        # Apply X gate to qubit
        qubit = ket_0.copy()
        qubit.shift(2*LEFT)
        self.play(Create(qubit))
        self.wait(1)
        self.play(ApplyMatrix([[0, 1], [1, 0]], qubit))
        self.wait(1)
        
        # Define Y gate
        y_gate = MathTex(r"Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}").scale(1.5)
        y_gate.to_edge(RIGHT)
        self.play(Transform(x_gate, y_gate))
        
        # Apply Y gate to qubit
        qubit.next_to(qubit_basis[1], LEFT)
        self.play(Create(qubit))
        self.wait(1)
        self.play(ApplyMatrix([[0, -1j], [1j, 0]], qubit))
        self.wait(1)
        
        # Define Z gate
        z_gate = MathTex(r"Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}").scale(1.5)
        z_gate.to_edge(RIGHT)
        self.play(Transform(x_gate, z_gate))
        
        # Apply Z gate to qubit
        qubit.next_to(qubit_basis[0], LEFT)
        self.play(Create(qubit))
        self.wait(1)
        self.play(ApplyMatrix([[1, 0], [0, -1]], qubit))
        self.wait(1)
        
        # Define H gate
        h_gate = MathTex(r"H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}").scale(1.5)
        h_gate.to_edge(RIGHT)
        self.play(Transform(x_gate, h_gate))
        # Apply H gate to qubit
        qubit.next_to(qubit_basis, LEFT)
        self.play(Create(qubit))
        self.wait(1)
        self.play(ApplyMatrix([[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]], qubit))
        self.wait(1)