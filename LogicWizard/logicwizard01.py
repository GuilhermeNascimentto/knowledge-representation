from manim import *


class CreateTableExample(Scene):
    def construct(self):
        table = Table(
            [["0", "1"],
            ["0","0"]],
            row_labels=[Text("RAM-0"), Text("RAM-1")],
            col_labels=[Text("000"), Text("0001")],
            include_outer_lines=True)
        self.play(table.create())
        self.wait(10)