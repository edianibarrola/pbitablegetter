import os
import pandas as pd





# Function to read and merge CSV files in the input folder
def merge_csv_files(input_folder):
    dataframes = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_folder, filename)
            dataset_name = filename.split(".csv")[0]  # Extract dataset name from the file name
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
        output_filename = "all_Dataset_Tables_and_Columns.csv"
        result_df.to_csv(output_filename, index=False)
        print(f"Data merged and saved to '{output_filename}'.")
    except ValueError as e:
        print(e)