from enum import Enum, unique, auto

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
    QColor,
)
from PyQt5.QtCore import (
    QPoint,
    QRect,
)

from spryte_pack.image_rect import ImageRect
from spryte_pack.solver_env import SolverEnv


class RenderArea(QWidget):

    @unique
    class Shape(Enum):
        LINE = auto()
        IMAGE = auto()

    def __init__(self, solver_env: SolverEnv, parent=None):
        super().__init__(parent)
        self._solver_env = solver_env
        self._transparency_checkerboard = QPixmap("../../assets/transparency_checkerboard.png")
        self._shape: RenderArea.Shape
        self._pen = QPen()
        self._brush = QBrush()
        self._antialiased = False
        self._transformed = False

        self.setMinimumSize(100, 100)

        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter()
        qp.begin(self)

        self.draw_checkerboard(qp)
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
        for image_rect in self._solver_env.image_rects:
            self.draw_image_rect(qp, image_rect)
        qp.end()

    @staticmethod
    def draw_image_rect(qp: QPainter, image_rect: ImageRect):
        outer_rect = QRect(image_rect.pos_x, image_rect.pos_y, image_rect.total_width, image_rect.total_height)
        inner_rect = QRect(image_rect.pos_x + image_rect.padding_x, image_rect.pos_y + image_rect.padding_y,
                           image_rect.width, image_rect.height)
        qp.drawRect(outer_rect)
        qp.drawImage(inner_rect, image_rect.qt_image)

    def draw_checkerboard(self, qp: QPainter):
        qp.drawTiledPixmap(self.rect(), self._transparency_checkerboard)

