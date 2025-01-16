from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit,
                             QPushButton, QComboBox, QHBoxLayout, QTextEdit,
                             QMessageBox)
from PyQt5.QtCore import Qt
from datetime import datetime

class AddTab(QWidget):
    def __init__(self, uncertainty_manager, workstreams):
        super().__init__()
        self.uncertainty_manager = uncertainty_manager
        self.workstreams = workstreams
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.workstream_combo = QComboBox()
        self.workstream_combo.addItems(self.workstreams)
        self.description_input = QLineEdit()
        self.parameter_input = QLineEdit()
        self.impact_combo = QComboBox()
        self.impact_combo.addItems(["Very Low", "Low", "Medium", "High", "Very High"])
        self.likelihood_combo = QComboBox()
        self.likelihood_combo.addItems(["Very Unlikely", "Unlikely", "Possible", "Likely", "Very Likely"])
        self.bandbreite_min_input = QLineEdit()
        self.bandbreite_max_input = QLineEdit()
        self.einheit_input = QLineEdit()
        self.verantwortlicher_input = QLineEdit()
        self.massnahmen_input = QTextEdit()
        self.status_massnahme_input = QLineEdit()
        self.kommentare_input = QTextEdit()

        input_layout = QVBoxLayout()
        input_layout.addLayout(self._create_labeled_widget("Workstream:", self.workstream_combo))
        input_layout.addLayout(self._create_labeled_widget("Description:", self.description_input))
        input_layout.addLayout(self._create_labeled_widget("Parameter:", self.parameter_input))
        input_layout.addLayout(self._create_labeled_widget("Impact:", self.impact_combo))
        input_layout.addLayout(self._create_labeled_widget("Likelihood:", self.likelihood_combo))

        bandbreite_layout = QHBoxLayout()
        bandbreite_layout.addWidget(QLabel("Bandbreite:"))
        bandbreite_layout.addWidget(self.bandbreite_min_input)
        bandbreite_layout.addWidget(QLabel(" - "))
        bandbreite_layout.addWidget(self.bandbreite_max_input)
        input_layout.addLayout(bandbreite_layout)

        input_layout.addLayout(self._create_labeled_widget("Einheit:", self.einheit_input))
        input_layout.addLayout(self._create_labeled_widget("Verantwortlicher:", self.verantwortlicher_input))
        input_layout.addLayout(self._create_labeled_widget("Massnahmen:", self.massnahmen_input))
        input_layout.addLayout(self._create_labeled_widget("Status Massnahme:", self.status_massnahme_input))
        input_layout.addLayout(self._create_labeled_widget("Kommentare:", self.kommentare_input))

        layout.addLayout(input_layout)

        self.save_button = QPushButton("Add Uncertainty")
        self.save_button.clicked.connect(self._add_uncertainty)
        layout.addWidget(self.save_button)

    def _create_labeled_widget(self, label_text, widget):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label_text))
        layout.addWidget(widget)
        return layout

    def _add_uncertainty(self):
        workstream = self.workstream_combo.currentText()
        description = self.description_input.text()
        parameter = self.parameter_input.text()
        impact = self.impact_combo.currentText()
        likelihood = self.likelihood_combo.currentText()
        bandbreite_min = self.bandbreite_min_input.text()
        bandbreite_max = self.bandbreite_max_input.text()
        einheit = self.einheit_input.text()
        verantwortlicher = self.verantwortlicher_input.text()
        massnahmen = self.massnahmen_input.toPlainText()
        status_massnahme = self.status_massnahme_input.text()
        kommentare = self.kommentare_input.toPlainText()

        new_uncertainty = {
            "Date": datetime.now(),
            "Workstream": workstream,
            "Description": description,
            "Parameter": parameter,
            "Impact": impact,
            "Likelihood": likelihood,
            "Bandbreite_Min": bandbreite_min,
            "Bandbreite_Max": bandbreite_max,
            "Einheit": einheit,
            "Verantwortlicher": verantwortlicher,
            "Massnahmen": massnahmen,
            "Status_Massnahme": status_massnahme,
            "Kommentare": kommentare,
        }

        self.uncertainty_manager.add_uncertainty(new_uncertainty)
        QMessageBox.information(self, "Success", "Uncertainty added successfully!")
        self._clear_input_fields()

    def _clear_input_fields(self):
        self.description_input.clear()
        self.parameter_input.clear()
        self.bandbreite_min_input.clear()
        self.bandbreite_max_input.clear()
        self.einheit_input.clear()
        self.verantwortlicher_input.clear()
        self.massnahmen_input.clear()
        self.status_massnahme_input.clear()
        self.kommentare_input.clear()