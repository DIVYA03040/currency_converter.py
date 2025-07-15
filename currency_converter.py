import requests

# Step 1: Get user inputs
amount = float(input("Enter amount: "))
from_currency = input("Convert from (e.g., USD): ").upper()
to_currency = input("Convert to (e.g., INR): ").upper()

# Step 2: Use API to get exchange rate
api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
response = requests.get(api_url)
data = response.json()

# Step 3: Calculate and print result
if to_currency in data["rates"]:
    rate = data["rates"][to_currency]
    result = amount * rate
    print(f"Converted Amount: {result:.2f} {to_currency}")
else:
    print("Invalid currency code or not supported.")


# Sample Output:
# Enter amount: 10000
# Convert from (e.g., USD): USD
# Convert to (e.g., INR): INR
# Converted Amount: 832500.00 INR
