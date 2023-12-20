import pandas as pd
# from logger import Logger
from datetime import datetime
import json
import sys

class DataLoader:

    def __init__(self):
        # self.logger = Logger().get_app_logger()
        # self.logger.info('Data loader object initialized')
        pass
    def load_file_lines(self, file_path):
      
        # Loads the lines from the specified csv

        try:
            with open(f'../data/{file_path}', 'r') as f:
                return f.readlines()
            
        except Exception as e:
            self.handle_error("Failed to read data", e)

    def process_trajectory_row(self, row):
       # proccess a row of trajectory data and addes a prefix to it(trajectory data are the ones that are not time dependent)   
       try:
         
         processed_rows = []
         for r in row:
            items = r.replace('\n', '').split(';')
            processed_rows.append(items[:4])
         return processed_rows
       
       except Exception as e:
        self.handle_error(f"Failed processing row for pandas at {row}", e)

    def prepare_data_for_pandas(self, columns, all_data, id_prefix):

        #prepares the data for creating pandas dataframe

        try:
            trajectory_cols = columns[:4]
            timed_vehicle_cols = ['track_id'] + columns[4:]

            trajectory_rows = [self.process_trajectory_row(row, id_prefix) for row in all_data]
            timed_vehicle_rows = [item for row in all_data for item in self.split_list(row.split(';')[4:], 6, row.split(';')[0])]

            return (trajectory_cols, trajectory_rows), (timed_vehicle_cols, timed_vehicle_rows)
        
        except Exception as e:
            self.handle_error("Failed to prepare data for pandas", e)

    def create_data_frame(self, data_cols, data_rows):

        #creates a Pandas Dataframe

        try:
            data_df = pd.DataFrame(columns=data_cols, data=data_rows)
            return data_df
        
        except Exception as e:
            self.handle_error("Failed to create data frame", e)

    def extract_data(self, file_name, return_json=False):

        # extracts the data and processes it and saves it to json
        try:
            id_prefix = f"{file_name.split('.')[0]}"
            lines = self.load_file_lines(file_name)
            columns, all_data = lines[0].replace('\n', '').split(';'), lines[1:20]

            trajectory_data, timed_vehicle_data = self.prepare_data_for_pandas(columns, all_data, id_prefix)

            if not return_json:
                return self.create_data_frame(*trajectory_data), self.create_data_frame(*timed_vehicle_data)

            tr_df = self.create_data_frame(*trajectory_data)
            vh_df = self.create_data_frame(*timed_vehicle_data)

            tr_file_name = self.save_to_json(tr_df, "trajectory")
            vh_file_name = self.save_to_json(vh_df, "vehicle_data")

            return tr_file_name, vh_file_name
        except Exception as e:
            self.handle_error("Failed to extract data", e)

    def save_to_json(self, df, data_type):

        # saves the dataframe into a Json file

        try:
            file_name = f"{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}{data_type}.json"
            df.to_json(f'../temp_storage/{file_name}', orient='records')
            return file_name
        except Exception as e:
            self.handle_error(f"Failed to save {data_type} data to JSON", e)

    def split_list(self, input_list, chunk_size, default_first_val=None):

        #splits the list into chuncks of a size of requried amount

        return [input_list[i:i + chunk_size] if not default_first_val else [default_first_val] + input_list[i:i + chunk_size]
                for i in range(0, len(input_list), chunk_size)]

    def handle_error(self, message, exception):

        # a function to handle error
        try:
           print("error occured")
        except:
            pass
        sys.exit(1)
