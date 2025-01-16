from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel)

class SummaryTab(QWidget):
    def __init__(self, uncertainty_manager):
        super().__init__()
        self.uncertainty_manager = uncertainty_manager
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.summary_labels = {
            "workstream": QLabel(),
            "parameter": QLabel(),
            "impact": QLabel(),
            "likelihood": QLabel()
        }
        layout.addWidget(QLabel("Uncertainties per Workstream:"))
        layout.addWidget(self.summary_labels["workstream"])
        layout.addWidget(QLabel("Uncertainties per Parameter:"))
        layout.addWidget(self.summary_labels["parameter"])
        layout.addWidget(QLabel("Distribution of Impact:"))
        layout.addWidget(self.summary_labels["impact"])
        layout.addWidget(QLabel("Distribution of Likelihood:"))
        layout.addWidget(self.summary_labels["likelihood"])

    def _update_summary_tab(self):
        df = self.uncertainty_manager.get_all_uncertainties()
        if not df.empty:
            workstream_summary = df['Workstream'].value_counts().to_string()
            parameter_summary = df['Parameter'].value_counts().to_string()
            impact_summary = df['Impact'].value_counts().to_string()
            likelihood_summary = df['Likelihood'].value_counts().to_string()

            self.summary_labels["workstream"].setText(workstream_summary)
            self.summary_labels["parameter"].setText(parameter_summary)
            self.summary_labels["impact"].setText(impact_summary)
            self.summary_labels["likelihood"].setText(likelihood_summary)
        else:
            for label in self.summary_labels.values():
                label.setText("No uncertainties recorded yet.")