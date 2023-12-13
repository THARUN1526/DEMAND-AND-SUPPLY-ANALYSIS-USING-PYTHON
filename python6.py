#Now let’s add a new column in the dataset by calculating the supply ratio
# Calculate the supply ratio for each level of driver activity

data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']
print(data.head())