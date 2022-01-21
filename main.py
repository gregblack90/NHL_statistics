#
# NHL betting decisions GUI
#
# IMPORT STATEMENTS
# Import GUI from designer file (ui.py)
from ui import Ui_MainWindow
# Import things for PyQt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
# Import functions from other files
from setup_ui import UiSetup
from compare_teams import GetSeasonData


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        # Create UI
        self.setupUi(self)

        # COMPARE TEAMS TAB
        # setup UI
        UiSetup.compare_teams_ui(self)
        # get data
        self.get_data_to_compare_button.clicked.connect(lambda: GetSeasonData(self))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_menu = Main()
    main_menu.show()
    sys.exit(app.exec_())
