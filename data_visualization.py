import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(df):
    # Aggregate data by calculating the mean AQI value for each city
    city_avg_aqi = df.groupby('City')['PM2.5 AQI Value'].mean().reset_index()

    # Sort the cities by average AQI value and select the top 20
    top_cities = city_avg_aqi.sort_values(by='PM2.5 AQI Value', ascending=False).head(20)

    # Plotting using a bar plot for clarity
    sns.barplot(x='City', y='PM2.5 AQI Value', data=top_cities)
    plt.xticks(rotation=90)  # Rotate city names for better readability
    plt.title("Top 20 Cities by Average PM2.5 AQI Value")
    plt.xlabel("City")
    plt.ylabel("Average PM2.5 AQI Value")
    plt.show()
