import sys
from dialog import Ui_VisualizerDialog
from PyQt5 import QtWidgets

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    app = QtWidgets.QApplication(sys.argv)
    VisualizerDialog = QtWidgets.QDialog()
    ui = Ui_VisualizerDialog()
    ui.setupUi(VisualizerDialog)
    VisualizerDialog.show()
    # visualizer.run(35, "DIJKSTRA", visualizer.QUICK_SOLVE)  # 21, 27, 35, 45, 63, 105, 135

    sys.exit(app.exec_())
