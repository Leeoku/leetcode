'''
You are building a payment reconciliation system for a payments platform. When a payment
comes in, it is encoded as a pipe-delimited string. Your job is to match that payment against a list
of outstanding invoices.
Input Format
Payment String
Always formatted as:
"PAY|<payment_id>|INV:<invoice_id>|AMT:<amount>|<currency>"
Example:
"PAY|TXN9921|INV:1042|AMT:250|USD"
Invoice List
A list of invoice dicts, each with:
[
{"invoice_id": "1042", "amount": 250, "due_date": "2024-03-15"},
{"invoice_id": "2099", "amount": 500, "due_date": "2024-01-10"},
{"invoice_id": "3301", "amount": 250, "due_date": "2024-02-01"},
]
Fields:
• invoice_id (str) — unique identifier
• amount (int) — payment amount in whole dollars
• due_date (str) — format YYYY-MM-DD
Part 1 — Match by Invoice ID
Write a function find_by_id(payment, invoices) that:
• Parses the INV:<invoice_id> field from the payment string• Returns the matching invoice dict
• Returns None if no match is found
Function Signature:
def find_by_id(payment: str, invoices: list) -> dict | None:

Part 2 — Match by Amount
Write a function find_by_amount(payment, invoices) that:
• Parses the AMT:<amount> field from the payment string
• Returns the matching invoice dict
• If multiple invoices share the same amount, return the one with the earliest due_date
• Returns None if no match is found
Function Signature:
def find_by_amount(payment: str, invoices: list) -> dict | None:
Constraints
• Payment string fields are always pipe-delimited and always present in order
• due_date strings are valid ISO 8601 and lexicographically sortable
• amount is always a positive integer
• The invoice list may be empty
• invoice_id values are unique across the list
Expected Output
payment = "PAY|TXN9921|INV:1042|AMT:250|USD"
find_by_id(payment, invoices)
# {"invoice_id": "1042", "amount": 250, "due_date": "2024-03-15"}
find_by_amount(payment, invoices)
# {"invoice_id": "3301", "amount": 250, "due_date": "2024-02-01"}
# (earliest due_date among the two $250 invoices)'''


import datetime as dt
from collections import Counter

#Part 1
invoices = [
{"invoice_id": "1042", "amount": 250, "due_date": "2024-03-15"},
{"invoice_id": "2099", "amount": 500, "due_date": "2024-01-10"},
{"invoice_id": "3301", "amount": 250, "due_date": "2024-02-01"},
]

sample_payment = "PAY|TXN1042|INV:1234|AMT:250|USD"

def find_by_id(payment: str, invoices: list) -> dict | None:
    if not payment:
        return None
    fields = payment.split("|")
    for field in fields:
        if field.startswith("INV:"):
            invoice_id = field.replace("INV:", "")
            break
    if invoice_id is None:
        return None
    
    for invoice in invoices:
        if invoice["invoice_id"] == invoice_id:
            return invoice
        
    return None


# find_by_id(sample_payment, invoices)


#Part 2
def find_by_amount(payment: str, invoices: list) -> dict | None:
    if not payment:
        return None
    fields = payment.split("|")
    for field in fields:
        if field.startswith("AMT"):
            invoice_amount = int(field.split(":")[1])

    best = None
    for invoice in invoices:
        if invoice["amount"] == invoice_amount:
            if best is None or invoice["due_date"] < best["due_date"]:
                best = invoice
    print(best)
    # print(matching_invoices)

    # # No invoices
    # if len(matching_invoices) == 0:
    #     return None
    # # Only 1 invoice
    # elif len(matching_invoices) == 1:
    #     return matching_invoices[0]
    # else:
    #     print(min(matching_invoices, key=lambda invoice:invoice["due_date"]))


find_by_amount(sample_payment, invoices)