from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton,
                             QFileDialog, QMessageBox)

class ConfigTab(QWidget):
    def __init__(self, config_handler):
        super().__init__()
        self.config_handler = config_handler
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.config_file_label = QLabel("No file selected")
        self.browse_button = QPushButton("Browse Excel File")
        self.browse_button.clicked.connect(self._browse_config_file)
        self.load_config_button = QPushButton("Load Workstreams")
        self.load_config_button.clicked.connect(self._load_workstreams)

        layout.addWidget(QLabel("Load Workstreams from Excel:"))
        layout.addWidget(self.config_file_label)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.load_config_button)

    def _browse_config_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Workstream Configuration File", "", "Excel Files (*.xlsx *.xls)", options=options)
        if file_name:
            self.config_file_label.setText(file_name)

    def _load_workstreams(self):
        config_file = self.config_file_label.text()
        if config_file and config_file != "No file selected":
            try:
                workstreams = self.config_handler.load_workstreams(config_file)
                # Hier müsstest du noch die Workstreams in den anderen Tabs aktualisieren,
                # z.B. über Signale und Slots oder eine zentrale Datenhaltung.
                QMessageBox.information(self, "Success", "Workstreams loaded successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error loading workstreams: {e}")
        else:
            QMessageBox.warning(self, "Warning", "Please select a configuration file first.")