import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(file_path):
    return pd.read_csv(file_path)


def display_basic_info(df):
    print("The Basic Information about the Data:")
    print(df.info())

def display_summary_stats(df):
    print(df.describe())

def display_first_few_rows(df):
    print(df.head())

def plot_numerical_histogram(df):
    df.hist(figsize=(12,10), bins = 20)
    plt.suptitle("Histogram")
    plt.show
def plot_correlation_heatmap(df):
    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_trajectory_paths(df):
    # Plot trajectory paths
    plt.figure(figsize=(12, 8))
    for track_id, group in df.groupby('track_id'):
        plt.plot(group['lon'], group['lat'], label=f'Track {track_id}')
    plt.title("Trajectory Paths")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.show()

def analyze_vehicle_types(df):
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='type', data=df)
    plt.title("Distribution of Vehicle Types")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Count")
    plt.show()

def analyze_speed_distribution(df):
   
    plt.figure(figsize=(10, 6))
    sns.histplot(df['speed'], bins=30, kde=True)
    plt.title("Speed Distribution")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Frequency")
    plt.show()
