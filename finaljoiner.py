import os
import pandas as pd

def process_csv_files(input_folder, output_file):
    # Initialize an empty list to store data from all CSVs
    combined_data = []

    # Loop through all CSV files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(input_folder, filename)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(filepath)

            # Separate the values in the "Dataset Name" column
            df[['Workspace', 'Dataset Name']] = df['Dataset Name'].str.split('-', n=1, expand=True)

            # Append the DataFrame to the combined_data list
            combined_data.append(df)

    # Concatenate all DataFrames in combined_data into a single DataFrame
    combined_df = pd.concat(combined_data, ignore_index=True)

    # Save the combined DataFrame to the output file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSVs successfully and saved to {output_file}")

if __name__ == "__main__":
    # Set the input folder where the CSVs are located
    input_folder = "input"

    # Set the output file name for the combined CSV
    output_file = "AllDatasetTablesAndColumns.csv"

    # Call the function to process the CSV files and combine them
    process_csv_files(input_folder, output_file)
