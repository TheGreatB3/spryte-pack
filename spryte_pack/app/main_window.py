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

        layout = QVBoxLayout()
        self.render_area = RenderArea(self._solver_env)
        layout.addWidget(self.render_area)

        self.setLayout(layout)

        self.resize(600, 400)


if __name__ == '__main__':
    q_app = QApplication([])
    app = SolverApp()
    app.show()
    q_app.exec_()
