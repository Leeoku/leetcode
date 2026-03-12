'''
You are given a CSV string containing transaction records. Parse the data, calculate each user's
fees based on transaction status, and aggregate results by user_id. This question is a dual test of
detail precision and business logic decomposition.
Input Format — CSV String
csv_data = """user_id,amount,provider,country,status
U01,100.00,visa,US,payment_completed
U01,200.00,card,US,dispute_won
U02,500.00,paypal,EU,payment_completed
U02,150.00,card,JP,dispute_lost
U03,300.00,visa,US,dispute_won
U03,80.00,paypal,US,payment_completed"""
Fee Rules
Apply the following rules based on the status field:
• payment_completed → fee = amount * 0.021 + 30
• dispute_lost → fee = 15 (fixed)
• dispute_won → fee = 15 if provider == 'card', else 0
Common pitfalls flagged by interviewers:
• Use 0.021, not 2.1 — percentage must be converted to decimal
• amount is a string in the CSV — cast to float before arithmetic
• String matching is case-sensitive: 'card' != 'Card'
• Trim whitespace from all fields after splitting
• Parse the header row to build a field-index mapping, do not hardcode indices
Part 1 — Calculate and Aggregate Fees
Implement calculate_fees(csv_data) that parses the CSV, applies the fee rules above, and returns
a dict mapping each user_id to their total fees.
def calculate_fees(csv_data: str) -> dict:
# returns {user_id: total_fee (float)}
Expected output:
{"U01": 47.10, # (100 * 0.021 + 30) + 15
"U02": 55.50, # (500 * 0.021 + 30) + 15
"U03": 36.3, # (300 * 0.021 + 30) + 0
}

Part 2 — Multi-Country Rate Extension
Extend Part 1: for payment_completed transactions, replace the fixed 2.1% rate with variable rates
based on the provider + country combination. All other fee rules remain unchanged.
Rate map:
rate_map = {
("visa", "US"): 0.021,
("visa", "JP"): 0.024,
("paypal", "EU"): 0.019,
("paypal", "US"): 0.022,
("card", "US"): 0.020,
}
If a provider+country combination is not in the rate map, fall back to the default rate of 0.021.
def calculate_fees_v2(csv_data: str, rate_map: dict) -> dict:
# same return type as Part 1
Implementation Notes
• Use tuples as rate_map keys — lists are unhashable
• Standardize provider and country case before lookup
• Extract fee calculation into a separate function for clean structure
• Keep if/elif branches flat — avoid deep nesting
• Follow-up question (common): How would you scale this to support more rules? Answer:
store rules in a config or database; avoid hardcoding; use a rule engine.
Constraints
• CSV always has a header row; parse it dynamically
• amount is always a valid positive decimal string
• status is always one of: payment_completed, dispute_lost, dispute_won• provider and country matching is case-sensitive
'''
from collections import defaultdict

csv_data = """
user_id,amount,provider,country,status
U01,100.00,visa,US,payment_completed
U01,200.00,card,US,dispute_won
U02,500.00,paypal,EU,payment_completed
U02,150.00,card,JP,dispute_lost
U03,300.00,visa,US,dispute_won
U03,80.00,paypal,US,payment_completed
"""

rate_map = {
("visa", "US"): 0.021,
("visa", "JP"): 0.024,
("paypal", "EU"): 0.019,
("paypal", "US"): 0.022,
("card", "US"): 0.020,
}

#part 1
def calculate_fees(csv_data: str) -> dict:
    rows = csv_data.strip().split("\n")
    column_names = [column.strip() for column in rows[0].split(',') ]
    data = []
    for entry in rows[1:]:
        fields = [field.strip() for field in entry.split(',')]
        row = dict(zip(column_names, fields))
        data.append(row)
    # print(data)

    fees = defaultdict(float)
    for transaction in data:
        if transaction["status"] == "payment_completed":
            print(float(transaction["amount"])*0.021+30)
            fees[transaction["user_id"]] += float(transaction["amount"]) * 0.021 + 30
            print(fees)
        elif transaction["status"] == "dispute_won":
            if transaction["provider"] == "card":
                fees[transaction["user_id"]] += 15
        elif transaction["status"] == "dispute_lost":
            fees[transaction["user_id"]] += 15
    print(dict(fees))
    return dict(fees)
calculate_fees(csv_data)
#part 2

def calculate_transaction_fee(amount, status, provider, country, rate_map):
    country = country.upper()
    provider = provider.lower()

    if status == "payment_completed":
        rate = rate_map.get((provider, country), 0.021)
        return round(float(amount) * rate + 30, 2)
    elif status == "dispute_won":
        if provider == "card":
            return 15
    elif status == "dispute_lost":
        return 15
    return 0

def calculate_fees_v2(csv_data: str, rate_map: dict) -> dict:
    rows = csv_data.strip().split("\n")
    column_names = [column.strip() for column in rows[0].split(',') ]
    data = []
    for entry in rows[1:]:
        fields = [field.strip() for field in entry.split(',')]
        row = dict(zip(column_names, fields))
        data.append(row)
    # print(data)

    fees = defaultdict(float)
    for transaction in data:
        transaction_fee = calculate_transaction_fee(
            transaction["amount"],
            transaction["status"],
            transaction["provider"],
            transaction["country"],
            rate_map
        )
        fees[transaction["user_id"]] += transaction_fee

    print(dict(fees))
    return dict(fees)
calculate_fees_v2(csv_data, rate_map)
