# main.py
from scripts.data_preprocessing import load_and_clean_data
from scripts.data_visualization import visualize_data
from scripts.modeling import build_and_evaluate_model

# Load and preprocess data
df = load_and_clean_data('data/environment_data.csv')

# Perform data visualization
visualize_data(df)

# Build and evaluate machine learning models
build_and_evaluate_model(df)
