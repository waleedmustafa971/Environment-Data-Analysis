# Environment Data Analysis
This project is an analysis of environmental data focusing on Air Quality Index (AQI) values across various cities. The project includes data preprocessing, visualization, and model building for better insights into air quality trends.

# Project Structure
<img width="532" alt="image" src="https://github.com/user-attachments/assets/9a265f31-4dc0-46b7-b114-9d3576a884ed">

# Installation
To set up the environment for this project, follow these steps:

1- Clone the repository:

git clone https://github.com/waleedmustafa971/environment-data-analysis.git
cd environment-data-analysis

2- Create a virtual environment:

python -m venv venv

3- Activate the virtual environment:

- On Windows:
.\venv\Scripts\activate

- On macOS/Linux:
source venv/bin/activate

4- Install the required dependencies:

pip install -r requirements.txt

# Usage
1- Data Preprocessing:

- The data_preprocessing.py script handles the loading and cleaning of the data.

- It drops rows with missing values and returns a cleaned DataFrame.
2- Data Visualization:


- The data_visualization.py script visualizes the cleaned data.
- The default visualization aggregates the PM2.5 AQI values by city and displays a bar plot of the top 20 cities with the highest average PM2.5 AQI values.

3- Running the Analysis:
- You can run the entire analysis by executing main.py:

python main.py


- This will load and preprocess the data, visualize it, and output the relevant plots.

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements, bug fixes, or additional features.


# License
This project is licensed under the MIT License - see the LICENSE file for details.




