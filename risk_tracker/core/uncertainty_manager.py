import pandas as pd

class UncertaintyManager:
    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.df = self.data_handler.load_data()
        self.data_file = self.data_handler.data_file  # Speichern für späteren Zugriff

    def add_uncertainty(self, uncertainty_data):
        self.df = pd.concat([self.df, pd.DataFrame([uncertainty_data])], ignore_index=True)

    def get_all_uncertainties(self):
        return self.df

    def save_data(self):
        return self.data_handler.save_data(self.df)