# Cell 1: Import the DataLoader class
from your_module_name import DataLoader  # Replace 'your_module_name' with the actual name of your module

# Cell 2: Function to simulate data loading and extraction
def simulate_data_loading_and_extraction(file_name, return_json=False):
    # Create DataLoader instance
    data_loader = DataLoader()

    # Load and extract data
    try:
        trajectory_df, timed_vehicle_df = data_loader.extract_data(file_name, return_json)
        print("Data loading and extraction successful!")
        return trajectory_df, timed_vehicle_df

    except Exception as e:
        print(f"Error during data loading and extraction: {e}")
        return None, None

# Cell 3: Function to display DataFrames
def display_dataframes(trajectory_df, timed_vehicle_df):
    print("Trajectory DataFrame:")
    print(trajectory_df.head())

    print("\nTimed Vehicle DataFrame:")
    print(timed_vehicle_df.head())

# Cell 4: Function to simulate saving data to JSON
def simulate_saving_to_json(file_name, return_json=False):
    # Create DataLoader instance
    data_loader = DataLoader()

    # Load and extract data
    try:
        tr_file, vh_file = data_loader.extract_data(file_name, return_json)
        print("Data loading and extraction successful!")

        # Display file names if return_json is True
        if return_json:
            print(f"Trajectory JSON File: {tr_file}")
            print(f"Timed Vehicle JSON File: {vh_file}")

    except Exception as e:
        print(f"Error during data loading and extraction: {e}")

# Cell 5: Example usage
file_name = "your_data_file.csv"  # Replace with the actual file name

# Simulate data loading and extraction
trajectory_data, timed_vehicle_data = simulate_data_loading_and_extraction(file_name, return_json=True)

# Display DataFrames
if trajectory_data is not None and timed_vehicle_data is not None:
    display_dataframes(trajectory_data, timed_vehicle_data)

# Simulate saving data to JSON
simulate_saving_to_json(file_name, return_json=True)
