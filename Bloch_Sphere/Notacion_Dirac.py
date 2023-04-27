from manim import *

class Dirac(Scene):
    def construct(self):
        # Display statement text
        statement1 = Tex("Dirac Notation").to_edge(UP)
        statement2 = Tex("Kets and Bras")
        statement3 = Tex("Inner Product")
        self.play(Write(statement1))

        # Display Dirac notation expression
        dirac_notation = Tex(r"$| \psi \rangle$").next_to(statement1, DOWN)
        self.play(Write(dirac_notation))

        # Add explanation text

        explanation101 = Tex(
            r"{8cm}In quantum mechanics, we use Dirac notation to represent the state of a quantum system. "
            r"This notation is based on vectors, and consists of a \textit{ket} and a \textit{bra}. "
            r"Here, we have a ket vector $|\psi \rangle$, which represents the state of a quantum system.\\ "
            r"A \textit{bra} is the complex conjugate of a ket vector, represented as $\langle \psi |$. "
            r"The \textit{inner product} of two kets is defined as $\langle \phi | \psi \rangle$. "
            r"It is a complex number that represents the overlap between the two states. ",
            tex_environment='minipage'
        ).next_to(dirac_notation, DOWN)

        self.play(Write(explanation101))
        self.play(explanation101[0][86:].animate.shift(0.5*DOWN))
        self.wait()