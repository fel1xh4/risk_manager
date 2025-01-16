from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTableView,
                             QPushButton)
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class ViewTab(QWidget):
    def __init__(self, uncertainty_manager):
        super().__init__()
        self.uncertainty_manager = uncertainty_manager
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self._update_view_tab)
        layout.addWidget(self.refresh_button)

    def _update_view_tab(self):
        df = self.uncertainty_manager.get_all_uncertainties()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)
        for index, row in df.iterrows():
            items = [QStandardItem(str(row[col])) for col in df.columns]
            model.appendRow(items)
        self.table_view.setModel(model)
        self.table_view.resizeColumnsToContents()