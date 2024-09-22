import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate EMI based on loan amount, interest rate, and tenure
def calculate_emi(loan_amount, interest_rate, tenure_years):
    tenure_months = tenure_years * 12
    monthly_rate = interest_rate / (12 * 100)
    emi = (loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months)) / (((1 + monthly_rate) ** tenure_months) - 1)
    return emi

# Function to calculate the total interest paid for the entire tenure
def calculate_total_interest(emi, tenure_years, loan_amount):
    tenure_months = tenure_years * 12
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    return total_interest

# Function to calculate remaining balance and interest lost if closing earlier
def early_closure(loan_amount, emi, interest_rate, tenure_years, close_after_years):
    tenure_months = tenure_years * 12
    close_after_months = close_after_years * 12
    remaining_balance = loan_amount
    total_interest_paid = 0
    
    # Loop through each month up to the early closure point
    for month in range(close_after_months):
        monthly_rate = interest_rate / (12 * 100)
        interest_for_month = remaining_balance * monthly_rate
        principal_for_month = emi - interest_for_month
        remaining_balance -= principal_for_month
        total_interest_paid += interest_for_month

    # Calculate interest lost for remaining months
    remaining_interest = calculate_total_interest(emi, tenure_years, loan_amount) - total_interest_paid
    remaining_months = tenure_months - close_after_months
    monthly_interest_loss = remaining_interest / remaining_months

    return remaining_balance, remaining_interest, monthly_interest_loss

# Input data
loan_amount = 5000000  # 50 lakh loan
interest_rate = 7.5    # Annual interest rate in percentage
tenure_years = 20      # Loan tenure in years
close_after_years = 10 # Customer wants to close after 10 years

# Calculate EMI
emi = calculate_emi(loan_amount, interest_rate, tenure_years)
total_interest = calculate_total_interest(emi, tenure_years, loan_amount)

# Calculate early closure details
remaining_balance, remaining_interest, monthly_interest_loss = early_closure(loan_amount, emi, interest_rate, tenure_years, close_after_years)

# Display results
print(f"Loan Amount: {loan_amount}")
print(f"Interest Rate: {interest_rate}%")
print(f"EMI: {emi:.2f}")
print(f"Total Interest over {tenure_years} years: {total_interest:.2f}")
print(f"Remaining Balance after {close_after_years} years: {remaining_balance:.2f}")
print(f"Interest Lost over remaining {tenure_years - close_after_years} years: {remaining_interest:.2f}")
print(f"Monthly Interest Loss after closure: {monthly_interest_loss:.2f}")

# Plot EMI for different interest rates
interest_rates = np.arange(6.0, 10.0, 0.5)
emis = [calculate_emi(loan_amount, rate, tenure_years) for rate in interest_rates]

plt.plot(interest_rates, emis, marker='o')
plt.title("EMI vs Interest Rate")
plt.xlabel("Interest Rate (%)")
plt.ylabel("EMI (INR)")
plt.grid(True)
plt.show()
