

#Parameters for
#        center (Sequence[float]) – Center of the Sphere.
#        radius (float) – The radius of the Sphere.
#        resolution (Sequence[int]) – The number of samples taken of the Sphere. A tuple can be used to define different resolutions for u and v respectively.
#       u_range (Sequence[float]) – The range of the u variable: (u_min, u_max).
#        v_range (Sequence[float]) – The range of the v variable: (v_min, v_max).

from manim import *

import numpy as np
class ExampleSphere(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=PI /2.5, theta=PI / 4)
        sphere = Sphere(
            center=(0, 0, 0),
            radius=3,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )

        #definindo cor e opacidade. 
        sphere.set_fill(BLUE, 0.01) 
        sphere.set_stroke(width=1)

        #criando eixo do tips=false é sem as setas de sentido
        axes = ThreeDAxes(tips=False)

        theta = 90 * DEGREES
        phi = 45 * DEGREES

        estado = (3.0, 2.0, 3.0)
        #criando e definindo o vetor PSI
        arrow = Arrow3D(start= ORIGIN,
                    end= np.array(estado),
                    color=YELLOW,
                    resolution = 8
                    )

        #end= [3*np.cos(theta), 3*np.sin(theta), 3*np.cos(phi)],

        #criando labels do estado basico do qubit e posicionando no eixo
        ket0 = axes.get_z_axis_label(Tex(r"$| 0 \rangle$"))
        ket1 = axes.get_z_axis_label(Tex(r"$| 1 \rangle$")).next_to(axes.z_axis, -1.0)
        #adicionando os objetos na cena
        sphere.
        estado = (0, 0, 3.0)
        
        self.wait()
        arrow.target = Arrow3D(start= ORIGIN,
                    end= np.array(estado),
                    color=YELLOW,
                    resolution = 8
                    )
       
        self.add(axes, sphere, ket0, ket1)
        self.wait()
        self.play(Create(arrow))
        self.play(MoveToTarget(arrow))
        self.wait(5)

        #self.play(Rotate(arrow.end_to, PI/2))
        #self.play(ApplyMethod(arrow,shift, LEFT*2))
