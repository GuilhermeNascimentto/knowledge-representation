from manim import *


class AxesAnimate(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(tips=False)
        self.play(Create(ax))
        x_label = MathTex("x").next_to(ax.get_x_axis().get_end())
        self.add_fixed_orientation_mobjects(x_label)
        self.add(x_label)
        self.move_camera(phi=75 * DEGREES, theta=25 * DEGREES)
        self.wait()