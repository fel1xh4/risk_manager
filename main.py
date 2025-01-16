import sys
from PyQt5.QtWidgets import QApplication
from risk_tracker.gui.main_window import UncertaintyTracker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tracker = UncertaintyTracker()
    tracker.show()
    sys.exit(app.exec_())