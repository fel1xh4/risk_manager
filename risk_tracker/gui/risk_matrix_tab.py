from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGridLayout, QLabel,
                             QComboBox, QHBoxLayout, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class RiskMatrixTab(QWidget):
    def __init__(self, uncertainty_manager, workstreams):
        super().__init__()
        self.uncertainty_manager = uncertainty_manager
        self.workstreams = workstreams
        self.impact_options = ["Very Low", "Low", "Medium", "High", "Very High"]
        self.likelihood_options = ["Very Unlikely", "Unlikely", "Possible", "Likely", "Very Likely"]
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.risk_matrix_workstream_label = QLabel("Workstream:")
        self.risk_matrix_workstream_combo = QComboBox()
        self.risk_matrix_workstream_combo.addItem("All")
        self.risk_matrix_workstream_combo.addItems(self.workstreams)
        self.risk_matrix_workstream_combo.currentIndexChanged.connect(self._update_risk_matrix_tab)

        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.risk_matrix_workstream_label)
        controls_layout.addWidget(self.risk_matrix_workstream_combo)
        layout.addLayout(controls_layout)

        self.risk_grid_layout = QGridLayout()
        layout.addLayout(self.risk_grid_layout)

        for col, impact in enumerate(self.impact_options):
            header_label = QLabel(impact)
            header_label.setAlignment(Qt.AlignCenter)
            self.risk_grid_layout.addWidget(header_label, 0, col + 1)

        for row, likelihood in enumerate(reversed(self.likelihood_options)):
            header_label = QLabel(likelihood)
            header_label.setAlignment(Qt.AlignCenter)
            self.risk_grid_layout.addWidget(header_label, row + 1, 0)
            for col in range(len(self.impact_options)):
                cell_label = QLabel()
                cell_label.setFrameShape(QLabel.Panel)
                cell_label.setLineWidth(1)
                cell_label.setMidLineWidth(1)
                cell_label.setStyleSheet("border: 1px solid black;")
                cell_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.risk_grid_layout.addWidget(cell_label, row + 1, col + 1)

        self.refresh_risk_matrix_button = QPushButton("Refresh Risk Matrix")
        self.refresh_risk_matrix_button.clicked.connect(self._update_risk_matrix_tab)
        layout.addWidget(self.refresh_risk_matrix_button)

    def _update_risk_matrix_tab(self):
        selected_workstream = self.risk_matrix_workstream_combo.currentText()

        for i in range(1, self.risk_grid_layout.rowCount()):
            for j in range(1, self.risk_grid_layout.columnCount()):
                widget = self.risk_grid_layout.itemAtPosition(i, j).widget()
                if widget is not None:
                    widget.setText("")
                    widget.setStyleSheet("border: 1px solid black;")

        df = self.uncertainty_manager.get_all_uncertainties()
        for index, row in df.iterrows():
            if selected_workstream == "All" or row['Workstream'] == selected_workstream:
                impact = row['Impact']
                likelihood = row['Likelihood']

                try:
                    col = self.impact_options.index(impact) + 1
                    row_idx = len(self.likelihood_options) - self.likelihood_options.index(likelihood)
                    cell_widget = self.risk_grid_layout.itemAtPosition(row_idx, col).widget()
                    if cell_widget is not None:
                        current_text = cell_widget.text()
                        cell_widget.setText(f"{current_text}\n- {row['Description']}")
                        self._set_risk_color(cell_widget, likelihood, impact)
                except ValueError:
                    print(f"Warning: Impact '{impact}' or Likelihood '{likelihood}' not found in options.")

    def _set_risk_color(self, label, likelihood, impact):
        likelihood_rank = self.likelihood_options.index(likelihood)
        impact_rank = self.impact_options.index(impact)

        risk_score = (likelihood_rank + 1) * (impact_rank + 1)

        if risk_score >= 16:
            label.setStyleSheet("background-color: red; border: 1px solid black;")
        elif risk_score >= 8:
            label.setStyleSheet("background-color: yellow; border: 1px solid black;")
        else:
            label.setStyleSheet("background-color: lightgreen; border: 1px solid black;")