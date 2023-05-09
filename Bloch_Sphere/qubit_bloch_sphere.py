from manim import *

import numpy as np

#in construcion
class BlochSphere(Scene):
    def construct(self):
        # Define colors for the axes
        x_color = RED
        y_color = GREEN
        z_color = BLUE

        # Create the axes
        axes = ThreeDAxes(
            x_range=(-1.2, 1.2),
            y_range=(-1.2, 1.2),
            z_range=(-1.2, 1.2),
            x_length=3,
            y_length=3,
            z_length=3,
            axis_config={"include_tip": False},
        )

        # Create the Bloch sphere
        sphere = Sphere(radius=1, checkerboard_colors=[WHITE, BLUE_E])
        sphere.set_stroke(width=1)

        # Create the labels
        x_label = Text("X", font_size=0.5).next_to(axes.x_axis, direction=RIGHT, buff=0.2)
        y_label = Text("Y", font_size=0.5).next_to(axes.y_axis, direction=UP, buff=0.2)
        z_label = Text("Z", font_size=0.5).next_to(axes.z_axis, direction=OUT, buff=0.2)

        # Add everything to the scene
        self.add(axes, x_label, y_label, z_label, sphere)

        # Define the initial qubit state
        theta = 30 * DEGREES
        phi = 45 * DEGREES
        #psi = np.cos(theta/2)*UP + np.exp(complex(0, phi))*np.sin(theta/2)*DOWN
        #psi = np.cos(theta/2)+ np.exp(complex(0, phi))*np.sin(theta/2)
        # Create the qubit arrow
        ORIGIN = np.array([0, 0, 0])
        arrow = Arrow3D(
            start=ORIGIN,
            end=np.cos(theta/2),
            color=YELLOW,
            resolution=8,

        )

        # Add the qubit arrow to the sphere
        self.play(Create(arrow))

        # Update the qubit arrow to rotate around the Bloch sphere
        self.play(
            Rotating(
                arrow,
                axis=phi*OUT,
                angle=theta,
                about_point=ORIGIN,
                run_time=3,
                rate_func=smooth,
            ),
        )
