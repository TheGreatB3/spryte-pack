from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
)

from spryte_pack.solver_env import SolverEnv


class SolverApp:
    def __init__(self):
        self._q_app = QApplication([])
        self._solver_env = SolverEnv()

        self._window = QWidget()
        self._layout = QVBoxLayout()
        self._layout.addWidget(QLabel("Solver App"))
        self._window.setLayout(self._layout)
        self._window.show()
        self._q_app.exec_()


if __name__ == '__main__':
    SolverApp()
