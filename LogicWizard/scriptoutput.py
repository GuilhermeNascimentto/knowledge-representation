class test(Scene):
    def construct(self):
        
        dot = Dot([-6,-3,0]).set_color(BLUE)
        arrow = Arrow([-6,-3,0], [-4, -1.3, 0], buff=0)
        numberplane = NumberPlane()
        dot2 = Dot([-4,-3,0]).set_color(BLUE)
        line  = Line(dot,dot2)

        angle = Angle(arrow,line, radius = 0.5, quadrant=(0,-5))
        
        ax = Axes(
            x_range=[0, 4], y_range=[0, 8], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)
        
        self.play(
            Create(ax)
        )

        curve_1 = ax.plot(lambda x: 4* x - x ** 2 , x_range=[0,4], color=ORANGE)

        
        
        self.play(
            Create(dot),
            run_time=3
        )
        
        self.play(
            Create(
                curve_1
            ),
            run_time=3
        )

        self.play(
            Create(arrow
            ),
            Create(line),
            Create(angle),
            run_time=2
        )
