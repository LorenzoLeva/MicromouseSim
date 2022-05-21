from Mouse import Mouse
from Maze import Maze

class MouseA(Mouse):
    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)
        