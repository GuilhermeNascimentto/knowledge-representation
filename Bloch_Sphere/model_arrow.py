from manim import *

from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip
class ArrowTipsShowcase(Scene):
    def construct(self):
        a00 = Arrow(start=[-2, 3, 0], end=[2, 3, 0], color=YELLOW)
        a11 = Arrow(start=[-2, 2, 0], end=[2, 2, 0], tip_shape=ArrowTriangleTip)
        a12 = Arrow(start=[-2, 1, 0], end=[2, 1, 0])
        a21 = Arrow(start=[-2, 0, 0], end=[2, 0, 0], tip_shape=ArrowSquareTip)
        a22 = Arrow([-2, -1, 0], [2, -1, 0], tip_shape=ArrowSquareFilledTip)
        a31 = Arrow([-2, -2, 0], [2, -2, 0], tip_shape=ArrowCircleTip)
        a32 = Arrow([-2, -3, 0], [2, -3, 0], tip_shape=ArrowCircleFilledTip)
        b11 = a11.copy().scale(0.5, scale_tips=True).next_to(a11, RIGHT)
        b12 = a12.copy().scale(0.5, scale_tips=True).next_to(a12, RIGHT)
        b21 = a21.copy().scale(0.5, scale_tips=True).next_to(a21, RIGHT)
        #self.add(a00, a11, a12, a21, a22, a31, a32, b11, b12, b21)
        self.play(Create(arrow))
from manim import Arrow

arrow = Arrow3D(np.array([0, 0, 0]), np.array([2, 1, 1]), buff = 0)

round(arrow.tip.tip_angle, 5) == round(PI/4, 5)
True