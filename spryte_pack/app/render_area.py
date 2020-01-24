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
    QPainter,
    QPaintEvent,
    QPainterPath,
)
from PyQt5.QtCore import (
    QPoint,
    QRect,
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

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        points = (
            QPoint(10, 80),
            QPoint(20, 10),
            QPoint(80, 30),
            QPoint(90, 70),
        )
        rect = QRect(10, 20, 80, 60)
        path = QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)
        qp.drawPoints(*points)
        qp.end()
