from manim import *

class GetCellExample(Scene):
    def construct(self):
        tupla0 = Table(
            [["0", "1", "0", "0", "0", "0", "0", "0"]],
            row_labels=[Text("RAM-0")],
            col_labels=[Text("000"), Text("001"), Text("010"), Text("011"), Text("100"), Text("101"), Text("110"), Text("111")])
        
        tupla1 = Table(
            [["0", "0", "0", "1", "0", "0", "0", "0"]],
            row_labels=[Text("RAM-1")],
            col_labels=[Text("000"), Text("001"), Text("010"), Text("011"), Text("100"), Text("101"), Text("110"), Text("111")])

        tupla2 = Table(
            [["0", "0", "1", "0", "0", "0", "0", "0"]],
            row_labels=[Text("RAM-2")],
            col_labels=[Text("000"), Text("001"), Text("010"), Text("011"), Text("100"), Text("101"), Text("110"), Text("111")])
        
        tupla3 = Table(
            [["0", "1", "0", "0", "0", "0", "1", "0"]],
            row_labels=[Text("RAM-3")],
            col_labels=[Text("000"), Text("001"), Text("010"), Text("011"), Text("100"), Text("101"), Text("110"), Text("111")])

            
        g1 = Group(tupla0, tupla1, tupla2, tupla3).scale(0.4).arrange(buff=1).to_edge(LEFT , buff=1)
    
        tupla0.move_to(UP)
        tupla1.next_to(tupla0, DOWN) #posicionando tuplha1 em relação a tuplha0
        tupla2.next_to(tupla1, DOWN) # //
        tupla3.next_to(tupla2, DOWN) # //
        self.add(g1)