from manim import *

class Trace3D(ThreeDScene):
    def construct(self):

        # Set up the camera 
        self.set_camera_orientation(phi=50 * DEGREES)

        # Construct a dot that we'll follow in an "orbit" slightly above a sphere
        dot = Dot3D()

        # Trace out the orbit of the dot by tracking it's center
        trace = TracedPath(dot.get_center,stroke_width=3,stroke_color=ORANGE)
        trace.set_shade_in_3d(True)

        # Construct the sphere above which a dot will do an "orbit"
        sphere = Sphere(
            center=(0, 0, 0),
            radius=2,
            resolution=(20, 20),
            fill_opacity=1.0
        )
        sphere.set_color(BLUE)

        # Construst a circular "orbit" for the dot that's slightly bigger than the radius of the sphere
        circle = Circle(radius=2.10)
        circle.rotate(90 * DEGREES, RIGHT)

        # Add the sphere, dot and trace to the scene - these will be visible
        self.add(dot,trace,sphere)

        # Rotate the scene as the dot orbits. Note that it doesn't matter if this is 0 or not, I still get the same behaviour
        self.begin_ambient_camera_rotation(rate=0)

        # Start the the dot on its circular "orbit"
        self.play(MoveAlongPath(dot, circle), rate_func=linear, run_time=4)