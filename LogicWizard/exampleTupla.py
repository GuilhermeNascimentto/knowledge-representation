from manim import *

class Tuplas(Scene):
    def construct(self):
        
        tupla0 = MathTable(
            [["", "000", "001", "010", "011", "100", "101", "111"],
            ["RAM-0", 0, 1, 0, 0, 0, 0, 0]],
            include_outer_lines=True)
        tupla0.add(tupla0.get_cell((2,3), color=RED))
        tupla0.add_highlighted_cell((2,3), color=GREEN)    

        tupla1 = MathTable(
            [["", "000", "001", "010", "011", "100", "101", "111"],
            ["RAM-0", 0, 0, 0, 1, 0, 0, 0]],
            include_outer_lines=True)
        tupla1.add(tupla1.get_cell((2,5), color=RED))
        tupla1.add_highlighted_cell((2,5), color=GREEN) 

        tupla2 = MathTable(
            [["", "000", "001", "010", "011", "100", "101", "111"],
            ["RAM-0", 0, 0, 1, 0, 0, 0, 0]],
            include_outer_lines=True)
        tupla2.add(tupla2.get_cell((2,4), color=RED))
        tupla2.add_highlighted_cell((2,4), color=GREEN) 

        tupla3 = MathTable(
            [["", "000", "001", "010", "011", "100", "101", "111"],
            ["RAM-0", 0, 0, 0, 0, 0, 1, 0]],
            include_outer_lines=True)
        tupla3.add(tupla3.get_cell((2,6), color=RED))
        tupla3.add_highlighted_cell((2,6), color=GREEN) 
        g1 = Group(tupla0, tupla1, tupla2, tupla3).scale(0.4).arrange(buff=1).to_edge(LEFT , buff=1)
        
        tupla0.move_to(UP)
        tupla1.next_to(tupla0, DOWN) #posicionando tuplha1 em relação a tuplha0
        tupla2.next_to(tupla1, DOWN) # //
        tupla3.next_to(tupla2, DOWN) # //
        self.add(g1)