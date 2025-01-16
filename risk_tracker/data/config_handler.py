import pandas as pd
from PyQt5.QtWidgets import QMessageBox

class ConfigHandler:
    def __init__(self, config_file):
        self.config_file = config_file

    def load_workstreams(self, filename=None):
        if filename is None:
            filename = self.config_file
        try:
            df = pd.read_excel(filename)
            return df.iloc[:, 0].tolist()
        except FileNotFoundError:
            QMessageBox.warning(None, "Warning", f"Configuration file '{filename}' not found. Using default workstreams.")
            return [f"Workstream {i+1}" for i in range(30)]
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error loading workstreams from '{filename}': {e}")
            return [f"Workstream {i+1}" for i in range(30)]