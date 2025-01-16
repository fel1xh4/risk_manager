import pandas as pd

class DataHandler:
    def __init__(self):
        # Define the Excel file path directly in the code
        self.data_file = "/Users/felixhalemba/Desktop/register.xlsx"  # Replace "data.xlsx" with your actual file path
        self.sheet_name = "Risikoregister"  # Replace "Sheet1" with the actual sheet name

    def load_data(self):
        """
        Loads data from an Excel file. If the file or sheet is not found, it creates an empty DataFrame with predefined columns.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the loaded or newly created data.
        """
        try:
            df = pd.read_excel(self.data_file, sheet_name=self.sheet_name, parse_dates=['Date'])
        except FileNotFoundError:
            print(f"File not found: {self.data_file}")
            df = pd.DataFrame(columns=[
                "Date", "Workstream", "Description", "Parameter", "Impact", "Likelihood",
                "Bandbreite_Min", "Bandbreite_Max", "Einheit", "Verantwortlicher",
                "Massnahmen", "Status_Massnahme", "Kommentare"
            ])
        except ValueError as e:
            if "Worksheet named" in str(e):
              print(f"Sheet '{self.sheet_name}' not found in the Excel file.")
              df = pd.DataFrame(columns=[
                  "Date", "Workstream", "Description", "Parameter", "Impact", "Likelihood",
                  "Bandbreite_Min", "Bandbreite_Max", "Einheit", "Verantwortlicher",
                  "Massnahmen", "Status_Massnahme", "Kommentare"
              ])
            else:
              print(f"Error during Excel data loading: {e}")
              df = pd.DataFrame(columns=[
                  "Date", "Workstream", "Description", "Parameter", "Impact", "Likelihood",
                  "Bandbreite_Min", "Bandbreite_Max", "Einheit", "Verantwortlicher",
                  "Massnahmen", "Status_Massnahme", "Kommentare"
              ])

        return df

    def save_data(self, df):
        """
        Saves a pandas DataFrame to an Excel file.

        Args:
            df (pd.DataFrame): The DataFrame to be saved.

        Returns:
            bool: True if the data was saved successfully, False otherwise.
        """
        try:
            df.to_excel(self.data_file, sheet_name=self.sheet_name, index=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False