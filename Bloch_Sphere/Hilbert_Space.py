from manim import *
#in construction
class HilbertSpace(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            tips=False,
            axis_config={"include_numbers": True},
        )

        hilbert_space = VGroup(axes)

        for i in range(4):
            circle = Circle(radius=0.4)
            circle.move_to([np.cos((2 * np.pi * i) / 4), np.sin((2 * np.pi * i) / 4), 0])
            label = Tex("q{}".format(i + 1)).scale(0.5)
            label.next_to(circle, UP, SMALL_BUFF)
            hilbert_space.add(circle, label)

        self.play(Create(hilbert_space))
        self.wait(2)
