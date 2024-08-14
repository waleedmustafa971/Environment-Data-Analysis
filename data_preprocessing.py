# scripts/data_preprocessing.py
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    print("Columns in the DataFrame:", df.columns)
    df = df.dropna()  # Dropping rows with any missing values

    # No date conversion since there's no date column in the dataset

    return df
