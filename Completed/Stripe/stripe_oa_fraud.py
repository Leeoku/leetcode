'''
Question 1
The fraud detection team at Stripe aims to reduce merchant fraud risk for Stripe with minimal pain to good merchants through machine learning. To provide initial data for training this machine learning model, you are tasked with developing a system to assess the fraud risk associated with transactions made to various merchants.
Description
You are given transactions_list which is a list of transactions for a certain day, merchants_list which is a list of merchants, and rules_list which is a list of rules corresponding to each transaction (more information below). A transaction denotes a payment made by a customer to a merchant. Each merchant in merchants_list is assigned a base_score. Your task is to assign each merchant a fraud score based on their transaction(s), where each transaction can have different risk factors based on certain categories (e.g., transaction amount, frequency of similar transactions, user activity). To do this:

Initialize a merchant's current_score as their base_score
For each transaction in the transactions_list, calculate and update the merchant's current_score. This should be done in separate passes over the entire list for each step:

If the transaction amount is greater than the corresponding rule's min_transaction_amount, multiply current_score by the corresponding rule's multiplicative_factor
If the same customer_id has made three or more transactions to that merchant_id (including the current transaction), add all the corresponding rules' additive_factors to current_score, cumulatively (e.g., if the merchant's score at the third transaction is X which include the first, second, and third additive_factors the fourth transaction should be X + the fourth's transaction additive_factor).
If a transaction is the third or more from the same customer_id in the same hour for the same merchant_id (including current transaction), do the following:

If the hour is between 12 to 17 (inclusive): Add the penalty each time (this includes the first and second transaction as well as all the ones after the third).
If the hour is between 9 to 11, or 18 to 21 (inclusive): Subtract the penalty each time (this includes the first and second transaction as well as all the ones after the third).
If the hour falls outside the above ranges, don't do anything.

Input
Note: You may assume that there won't be any integer overflows.

transactions_list: A list of length n (1 ≤ n ≤ 1000) where each transaction is represented as a comma-separated string.

A string merchant_id (length > 0) of the merchant who receives payment'''

from collections import defaultdict, Counter

merchants = ["M1", "M2"]
transactions = [
    {"merchant_id": "M1", "customer_id": "C1", "amount": 100, "timestamp": "2026-01-24 10:15"},
    {"merchant_id": "M1", "customer_id": "C1", "amount": 50, "timestamp": "2026-01-24 10:45"},
    {"merchant_id": "M1", "customer_id": "C2", "amount": 200, "timestamp": "2026-01-24 11:05"},
    {"merchant_id": "M2", "customer_id": "C3", "amount": 300, "timestamp": "2026-01-24 10:30"},
    {"merchant_id": "M2", "customer_id": "C3", "amount": 150, "timestamp": "2026-01-24 10:45"},
    {"merchant_id": "M2", "customer_id": "C4", "amount": 50, "timestamp": "2026-01-24 10:50"},
]

# Rule parameters
multiply_factor = 2
customer_bonus = 1
hour_threshold = 3
hour_penalty = 5
additive_factor = 0 # what is this??
base_score = 1
min_transaction_amount = 10

'''
Notes:
1. Base score initial

Transaction
- Assume minimum transaction amount = 0
-Calculate and update merchant score,  multiply current_score by the corresponding rule's multiplicative_factor

Time

'''

score_dict = {merchant:base_score for merchant in merchants}
# customer_dict = defaultdict(lambda: defaultdict(int))
# hours_dict = defaultdict(lambda:defaultdict(int))
customer_count = defaultdict(Counter)
hours_count = defaultdict(lambda:defaultdict(Counter))

values = [()]

#Pass 1
for transaction in transactions:
    amount = transaction["amount"]
    if amount > min_transaction_amount:
        score_dict[transaction["merchant_id"]] *= multiply_factor


#Pass 2
for transaction in transactions:
    customer_id = transaction["customer_id"]
    merchant_id = transaction["merchant_id"]
    customer_count[merchant_id][customer_id] += 1
    if customer_count[merchant_id][customer_id] >= 3:
        score_dict[merchant_id] += additive_factor
# print(hours_count)
#Pass 3
penalty_hours = list(range(12, 18))
non_penalty_hours = list(range(9,12)) + list(range(18, 22))
for transaction in transactions:
    customer_id = transaction["customer_id"]
    merchant_id = transaction["merchant_id"]
    hour_string = transaction["timestamp"][:13]
    hour = int(hour_string[-2:])
    hours_count[merchant_id][customer_id][hour_string] += 1
    count = hours_count[merchant_id][customer_id][hour_string]


    if count == 3:  # trigger point: retroactively apply for txns 1 and 2 as well
        if hour in penalty_hours:
            score_dict[merchant_id] += hour_penalty * 3  # covers all 3
        elif hour in non_penalty_hours:
            score_dict[merchant_id] -= hour_penalty * 3
    elif count > 3:  # subsequent transactions
        if hour in penalty_hours:
            score_dict[merchant_id] += hour_penalty
        elif hour in non_penalty_hours:
            score_dict[merchant_id] -= hour_penalty
print({merchant: score_dict[merchant] for merchant in sorted(score_dict)})
# return {merchant: score_dict[merchant] for merchant in sorted(score_dict)}