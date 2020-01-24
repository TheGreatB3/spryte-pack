from enum import Enum, unique, auto
from typing import Any

from PyQt5.QtWidgets import (
    QWidget,
)
from PyQt5.QtGui import (
    QPen,
    QBrush,
    QPixmap,
    QPalette,
)


class RenderArea(QWidget):
    @unique
    class Shape(Enum):
        LINE = auto()
        IMAGE = auto()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._shape: RenderArea.Shape
        self._pen: QPen
        self._brush: QBrush
        self._antialiased = False
        self._transformed = False

        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)
