from typing import List

from spryte_pack.image_rect import ImageRect


class SolverEnv:
    """
    Hosts the solver and images.
    """
    def __init__(self):
        self._image_rects: List[ImageRect] = []
