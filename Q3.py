import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the depreciated value of the vehicle for each year
def calculate_depreciation(vehicle_value, depreciation_rate, num_years):
    values = []
    current_value = vehicle_value
    for year in range(num_years):
        values.append(current_value)
        current_value -= current_value * depreciation_rate / 100
    return values

# Function to calculate premiums based on depreciated vehicle value
def calculate_premiums(vehicle_value, premium_rate, depreciation_rate, num_years):
    yearly_premiums = []
    quarterly_premiums = []
    monthly_premiums = []
    
    # Calculate the depreciated value each year and corresponding premiums
    depreciated_values = calculate_depreciation(vehicle_value, depreciation_rate, num_years)
    
    for value in depreciated_values:
        yearly_premium = value * premium_rate / 100
        yearly_premiums.append(yearly_premium)
        quarterly_premiums.append(yearly_premium / 4)
        monthly_premiums.append(yearly_premium / 12)
    
    return yearly_premiums, quarterly_premiums, monthly_premiums

# Input Data
vehicle_value = 1000000  # Initial vehicle value (1 million)
premium_rate = 5         # Annual premium rate in percentage
depreciation_rate = 7    # Annual depreciation rate of vehicle in percentage
num_years = 10           # Number of years of insurance

# Calculate premiums
yearly_premiums, quarterly_premiums, monthly_premiums = calculate_premiums(vehicle_value, premium_rate, depreciation_rate, num_years)

# Create a DataFrame to hold the data
df = pd.DataFrame({
    'Year': np.arange(1, num_years + 1),
    'Yearly Premium': yearly_premiums,
    'Quarterly Premium': quarterly_premiums,
    'Monthly Premium': monthly_premiums
})

# Display the DataFrame
print(df)

# Plot the premiums over time
plt.plot(df['Year'], df['Yearly Premium'], label='Yearly Premium', marker='o')
plt.plot(df['Year'], df['Quarterly Premium'], label='Quarterly Premium', marker='s')
plt.plot(df['Year'], df['Monthly Premium'], label='Monthly Premium', marker='^')

# Add labels and title
plt.title('Premiums over Time with Vehicle Depreciation')
plt.xlabel('Year')
plt.ylabel('Premium (INR)')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
