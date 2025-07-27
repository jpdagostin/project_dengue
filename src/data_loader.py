import pandas as pd

class DataLoader:
    @staticmethod
    def load_data(filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {filepath}")
            return None
