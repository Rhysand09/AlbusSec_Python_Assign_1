# Data Cleaning Program

This program reads data from a CSV file and performs basic data cleaning operations.

## Operations Performed

1. **Removing Duplicates**: The program removes any duplicate rows in the dataset.
2. **Handling Missing Values**: The program replaces any missing values with the string 'Unknown'.

## How to Run

1. Ensure that you have Python and the pandas library installed on your system.
2. Place the CSV file you want to clean in the same directory as this program.
3. Replace 'data.csv' in the `pd.read_csv('data.csv')` line with the name of your CSV file.
4. Run the program. The cleaned data will be saved in the same directory as 'cleaned_data.csv'.
