import pandas as pd
import os
working_dir = r"C:\Users\eyale\Desktop\datasets"

def get_next_year_columns(df):
    # Extract years from the 'Date' column
    years = pd.DatetimeIndex(df['Date']).year.unique()
    next_year_columns = {}

    for year in years:
        # Get columns that include the next year in their name
        next_year = year + 1
        next_year_cols = [col for col in df.columns if str(next_year) in col]
        if next_year_cols:
            next_year_columns[year] = next_year_cols

    return next_year_columns


# Define a function to check if all columns for the next year exist and have no NaNs
def check_next_year_columns(row, next_year_cols):
    year = row['Date'].year
    for column in next_year_cols[year]:
        if column not in df.columns or pd.isna(row[column]):
            return False
    return True


errors = 0
for file_name in os.listdir(working_dir):
    print(file_name)
    df = pd.read_excel(os.path.join(working_dir, file_name))
    df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y', errors='coerce')
    next_year_columns = get_next_year_columns(df)
    print(next_year_columns)
    df['Valid'] = df.apply(lambda row: check_next_year_columns(row, next_year_columns), axis=1)
    invalid_rows = df[~df['Valid']]
    if not invalid_rows.empty:
        print("Rows with missing next year columns or NaN values:")
        print(invalid_rows)
        errors += 1
    else:
        print("All rows meet the condition.")
    print()
if errors == 0:
    print("No errors")
else:
    print(f"There are {errors} errors")

