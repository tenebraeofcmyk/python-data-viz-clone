# To setup a virtual environment
# python -m venv venv
# python.exe -m pip install --upgrade pip

# pip install pandas
# pip install matplotlib

import json
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON data from the file
with open('rows.json') as file:
    data = json.load(file)

# Now `data` is a Python dictionary that contains the collision data

# Convert data into a DataFrame
# Assuming the relevant data is in a list under the key 'data'
df = pd.DataFrame(data['data'], columns=[column['name'] for column in data['meta']['view']['columns']])

# Now `df` is a DataFrame with your data


# Convert the 'date' column to datetime format (adjust column name as necessary)
df['date'] = pd.to_datetime(df['CRASH DATE'])

# Create a new column for the month
df['month'] = df['date'].dt.month

# Count the number of collisions per month
collisions_per_month = df.groupby('month').size()

# Plot
collisions_per_month.plot(kind='bar')
plt.title('Collisions Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Collisions')
plt.xticks(rotation=45)
plt.show()
