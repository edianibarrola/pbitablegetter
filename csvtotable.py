import os
import pandas as pd

# Put all the csvs into the input folder.
# then run this to combine them.

# if you need to rip the html use pbitableripper.py with the html from the site.



# Function to read and merge CSV files in the input folder
def merge_csv_files(input_folder):
    dataset_name = input_folder.split(os.path.sep)[-1]
    dataframes = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_folder, filename)
            df = pd.read_csv(filepath)
            df['Dataset Name'] = dataset_name
            dataframes.append(df)
    
    if not dataframes:
        raise ValueError("No CSV files found in the input folder.")
    
    return pd.concat(dataframes, ignore_index=True)




if __name__ == "__main__":
    input_folder = "input"  # Change this to the correct path if needed
    
    try:
        result_df = merge_csv_files(input_folder)
        output_filename = "All Datasets Tables and Columns.csv"
        result_df.to_csv(output_filename,index=False)
        print(f"data merged and saved")
    except ValueError as e:
        print(e)