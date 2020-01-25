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


class SolverApp(QWidget):
    def __init__(self):
        super().__init__()
        self._solver_env = SolverEnv()
        self._solver_env.add_images(
            self._solver_env.load_images_from_files(("../../assets/python-logo-transparent.png",)))
        pixmap = QPixmap("../../assets/python-logo.png")
        pixmap_t = QPixmap("../../assets/python-logo-transparent.png")

        layout = QVBoxLayout()
        self.render_area = RenderArea()
        layout.addWidget(self.render_area)
        label = QLabel("Solver App")
        label.setPixmap(pixmap_t)
        layout.addWidget(label)
        for image_rect in self._solver_env.image_rects:
            label_ = QLabel("Image")
            label_.setPixmap(QPixmap.fromImage(image_rect.qt_image))
            layout.addWidget(label_)
        self.setLayout(layout)


if __name__ == '__main__':
    q_app = QApplication([])
    app = SolverApp()
    app.show()
    q_app.exec_()
