

#Parameters for
#        center (Sequence[float]) – Center of the Sphere.
#        radius (float) – The radius of the Sphere.
#        resolution (Sequence[int]) – The number of samples taken of the Sphere. A tuple can be used to define different resolutions for u and v respectively.
#       u_range (Sequence[float]) – The range of the u variable: (u_min, u_max).
#        v_range (Sequence[float]) – The range of the v variable: (v_min, v_max).

from manim import *

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

        #criando eixo do tips=false é sem as setas de sentido
        axes = ThreeDAxes(tips=False)

        #criando e definindo o vetor PSI
        vector = Arrow3D(start= np.array([0,0,0]),
                    end= np.array([3,1,3]),
                    resolution = 10)

        #criando labels do estado basico do qubit e posicionando no eixo
        ket0 = axes.get_z_axis_label(Tex(r"$| 0 \rangle$"))
        ket1 = axes.get_z_axis_label(Tex(r"$| 1 \rangle$")).next_to(axes.z_axis, -1.0)
        #adicionando os objetos na cena
        self.add(axes, sphere, vector, ket0, ket1)            

