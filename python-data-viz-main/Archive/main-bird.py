import pandas as pd
import matplotlib.pyplot as plt

def analyze_h5n1_data(csv_file_path, specific_county=None):
    # Load the H5N1 data from the CSV file
    df = pd.read_csv(csv_file_path)

    # Convert the 'Outbreak Date' column to datetime format
    df['Outbreak Date'] = pd.to_datetime(df['Outbreak Date'])

    # Create a new column for the month in 'YYYY-MM' format
    df['year_month'] = df['Outbreak Date'].dt.to_period('M')

    if specific_county:
        # Filter the dataframe for the specific county
        df = df[df['County'].str.lower() == specific_county.lower()]

    # Count the number of H5N1 detections per 'year_month'
    detections_per_year_month = df.groupby('year_month').size()

    # Convert the period index back to string for plotting
    detections_per_year_month.index = detections_per_year_month.index.astype(str)

    # Plot
    detections_per_year_month.plot(kind='bar', figsize=(10, 6))
    title = 'H5N1 Detections Per Month' + (f' in {specific_county}' if specific_county else '')
    plt.title(title)
    plt.xlabel('Month')
    plt.ylabel('Number of Detections')
    plt.xticks(rotation=90)
    plt.show()

# Example usage:
csv_file_path = 'data-h5n1-set2.csv'  # Change this to your actual file path
analyze_h5n1_data(csv_file_path)  # To see total detections
# analyze_h5n1_data(csv_file_path, specific_county='Edmunds')  # To see detections for a specific county
