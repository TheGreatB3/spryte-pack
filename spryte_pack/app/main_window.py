from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
)
from PyQt5.QtGui import (
    QPainter,
    QPixmap,
)

from spryte_pack.solver_env import SolverEnv
from spryte_pack.app.render_area import RenderArea


class SolverApp:
    def __init__(self):
        self._q_app = QApplication([])
        self._solver_env = SolverEnv()
        self._solver_env.add_images(
            self._solver_env.load_images_from_files(("../../assets/python-logo-transparent.png",)))
        pixmap = QPixmap("../../assets/python-logo.png")
        pixmap_t = QPixmap("../../assets/python-logo-transparent.png")

        self._window = QWidget()
        layout = QVBoxLayout()
        render_area = RenderArea()
        layout.addWidget(render_area)
        label = QLabel("Solver App")
        label.setPixmap(pixmap_t)
        layout.addWidget(label)
        for i in self._solver_env._image_rects:
            label_ = QLabel("Image")
            label_.setPixmap(QPixmap.fromImage(i.qt_image))
            layout.addWidget(label_)
        self._window.setLayout(layout)
        self._window.show()
        self._q_app.exec_()


if __name__ == '__main__':
    SolverApp()
