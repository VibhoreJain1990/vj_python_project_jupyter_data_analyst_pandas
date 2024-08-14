import pandas as pd

# Load the Excel file
df = pd.read_excel(r'C:\Users\HP 1030 G4\Downloads\SampleData.xlsx', sheet_name='SalesOrders')

# Display the first few rows of the dataframe
print(df.head())

# Example analysis: Get summary statistics
print(df.describe())

# Example analysis: Filter data
#filtered_df = df[df['Column_Name'] > value]

# Save the filtered data to a new Excel file
#filtered_df.to_excel('filtered_data.xlsx', index=False)
