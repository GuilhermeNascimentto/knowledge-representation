from manim import *
#codigo fonte retirado da comunidade manim no discord 
class XGate(Scene):
    def construct(self):
        # Create qubit with label
        qubit = MathTex("\\vert 0 \\rangle").shift(UP*1.5)
        label = MathTex("X").next_to(qubit, DOWN)

        # Show initial state
        self.play(Create(qubit))
        self.play(Create(label))

        # Apply X gate
        x_gate = MathTex("\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}").next_to(label, RIGHT)
        self.play(Create(x_gate))
        self.play(Transform(qubit, MathTex("\\vert 1 \\rangle").shift(UP*1.5)))
        self.wait(0.5)

        # Reverse X gate
        self.play(Transform(qubit, MathTex("\\vert 0 \\rangle").shift(UP*1.5)))
        self.wait(0.5)
        self.play(FadeOut(x_gate))

        # Clean up
        self.play(FadeOut(qubit), FadeOut(label))