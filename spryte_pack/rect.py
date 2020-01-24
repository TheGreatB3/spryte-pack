from typing import Union, Tuple


class Rect:
    def __init__(self, width: int, height: int, pos_x: int = 0, pos_y: int = 0,
                 padding: Union[int, Tuple[int, int]] = (0, 0)):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        if isinstance(padding, int):
            self.padding_x = padding
            self.padding_y = padding
        else:
            self.padding_x, self.padding_y = padding
