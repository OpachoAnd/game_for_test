import pandas as pd

class ML_model:
    data_df: pd.DataFrame
    results_df: = pd.DataFrame()
    metrics_df: = pd.DataFrame()

    def __init__(self):
        self.data_df = pd.DataFrame()
        self.results_df = pd.DataFrame()
        self.metrics_df = pd.DataFrame()

        self.metrics_df = None

    def train(self):
        pass

    def predict(self):
        pass

    def evaluate(self):
        pass

    def load_model(self):
        pass

    def save_model(self):
        pass

    def save_metrics_and_result(self):
        pass

    def save_data_df(self):
        pass
