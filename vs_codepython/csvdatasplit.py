import pandas as pd


# df.loc[df['GPU Model'] == 'RTX4090 ', 'GPU Model'] += '150W'
# df.loc[df['GPU Model'] == 'RTX4060 ', 'GPU Model'] += '115W'
# df.loc[df['GPU Model'] == 'RTX4070', 'GPU Model'] += ' 120W'
# df.loc[df['GPU Model'] == 'RTX4080', 'GPU Model'] += ' 140W'
# df.loc[df['GPU Model'] == 'RTX4050', 'GPU Model'] += ' 115W'

# df.loc[df['GPU Model'] == 'RTX3070Ti', 'GPU Model'] += ' 125W'
# df.loc[df['GPU Model'] == 'RTX3070', 'GPU Model'] += ' 125W'
# df.loc[df['GPU Model'] == 'RTX3060', 'GPU Model'] += ' 115W'
# df.loc[df['GPU Model'] == 'RTX3050Ti', 'GPU Model'] += ' 60W'
# df.loc[df['GPU Model'] == 'RTX3050', 'GPU Model'] += ' 45W'

# df.loc[df['GPU Model'] == 'GTX2060', 'GPU Model'] += ' 90W'
# df.loc[df['GPU Model'] == 'GTX2050', 'GPU Model'] += ' 45W'

# df.loc[df['GPU Model'] == 'GTX1660Ti', 'GPU Model'] += ' 80W'
# df.loc[df['GPU Model'] == 'GTX1650 ', 'GPU Model'] += '50W'
# df.loc[df['GPU Model'] == 'GTX1650Ti', 'GPU Model'] += ' 50W'
# df.loc[df['GPU Model'] == 'GTX1050 ', 'GPU Model'] += '40W'


# power_rating_mapping = {
#     'RTX 4090': '150W',
#     'RTX 4060': '115W',
#     'RTX 4070': '120W',
#     'RTX 4080': '140W',
#     'RTX 4050': '115W',
#     'RTX 3070 Ti': '125W',
#     'RTX 3070': '125W',
#     'RTX 3060': '115W',
#     'RTX 3050 Ti': '60W',
#     'RTX 3050': '45W',
#     'GTX 2060': '90W',
#     'GTX 2050': '45W',
#     'GTX 1660 Ti': '80W',
#     'GTX 1650': '50W',
#     'GTX 1650 Ti': '50W'
# }


# Read the CSV file into a DataFrame
input_file = 'laptop-data-lastv6.csv'
output_file = 'laptop-data-lastv6-2.csv'
df = pd.read_csv(input_file)

# Split the data in the specified column
split_data = df['GPU Model'].str.split(expand=True)

# Assign the split data to new columns
df['Model'] = split_data[0]
df['Power'] = split_data[1]
# Drop the original column if needed
# df = df.drop(columns=['ColumnName'])

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Data has been split and saved to {output_file}.")
