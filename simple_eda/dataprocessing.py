# import pandas as pd

# def update_csv(file_path, new_file_path):
    
#     df = pd.read_csv(file_path, sep=';', encoding='utf-8', error_bad_lines = False)
#     print(len(df.columns))
    
#     time_columns = df.columns[4:11]
#     print (time_columns)
    
# #     column_mapping = {}
# #     for i, col in enumerate(time_columns):
# #         new_col_name = f'interval_{i//6 + 1}_{col}'
# #         column_mapping[col] = new_col_name

    
# #     df.rename(columns=column_mapping, inplace=True)

    
# #     df.to_csv(new_file_path, index=False)

# original_file_path = '/home/lillian/Documents/TenAcadamyTasks/traffic_data/20181024_d1_0830_0900 (2).csv'
# new_file_path = '/home/lillian/Documents/TenAcadamyTasks/traffic_data/updated_csv.csv'

# update_csv(original_file_path, new_file_path)


# # df = pd.read_csv(new_file_path)

import pandas as pd
import csv

def update_csv(file_path, new_file_path):
    max_contents_line = None
    max_contents_count = 0
    max_contents_index = 0
    # Open the CSV file and handle inconsistent lines
    with open(file_path, 'r', encoding='utf-8') as file:

        lines = file.readlines()
    #     for index, line in enumerate(lines):
    #         line_contents = line.strip().split(';')
    #         if len(line_contents)> max_contents_count:
    #             max_contents_count = len(line_contents)
    #             max_contents_line = line
    #             max_contents_index = index

    # print(max_contents_count)   
    # print(max_contents_index)
    # print(max_contents_line.strip().split(';'))

    header = lines[0].strip().split(';')
    print(header)
    num_time_columns = len(lines[17].strip().split(';')) -4 
    print(num_time_columns)
    extended_header = header + [f'{col}_interval_{i//6 + 1}' for i, col in enumerate(header[-num_time_columns:])]
    
    # Write the lines to a new file, skipping lines with errors
    with open(new_file_path, 'w', encoding='utf-8', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=';')

        csv_writer.writerow(extended_header)
        for line in lines[1:]:
            try:
                # Try to parse the line as CSV
                row = next(csv.reader([line], delimiter=';'))
                csv_writer.writerow(row)
            except csv.Error as e:
                print(f"Error processing line: {e}")

# # Example usage:
                
original_file_path = '/home/lillian/Documents/TenAcadamyTasks/traffic_data/updated_csv.csv'
new_file_path = '/home/lillian/Documents/TenAcadamyTasks/traffic_data/updated_data.csv'
update_csv(original_file_path, new_file_path)

# # Now you can read the cleaned CSV into a DataFrame
# # df = pd.read_csv(new_file_path, sep=';')
