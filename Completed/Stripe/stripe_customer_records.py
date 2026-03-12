'''
Background
You are onboarding a batch of new customers onto a payments platform. Customer data is stored
in a local JSON file. Read the file and register each customer via the Stripe API using the requests
library.
Input File — customers.json
[
{
"name": "Alice Nguyen",
"email": "alice@example.com",
"phone": "+15141234567",
"metadata": {"internal_id": "USR-001", "plan": "premium"}
},
{
"name": "Bob Smith",
"email": "bob@example.com",
"phone": "+15149876543",
"metadata": {"internal_id": "USR-002", "plan": "basic"}
}
]
Part 1 — Create Customers
Read customers.json and POST each customer to:
POST https://api.stripe.com/v1/customers
Part 2 — Print Confirmation
After each successful request print internal_id and the returned Stripe customer ID:
USR-001 -> cus_ABC123
USR-002 -> cus_DEF456
Constraints
• Use the requests library; API key in STRIPE_API_KEY env variable
• Use data= (form-encoded), not json=
• Nested metadata sent as metadata[key]=value
• On request failure: print the error and continue to next customer
Stripe API ReferencePOST https://api.stripe.com/v1/customers
Authorization: Bearer <STRIPE_API_KEY>
Fields: name, email, phone, metadata[key]
Response: {"id": "cus_ABC123", "object": "customer", ...}
'''

import json, os #requests



url = 'https://api.stripe.com/v1/customers'

#Part 1
def create_customers(filepath:str) -> None:
    api_key = os.environ.get("STRIPE_API_KEY")
    try:
        with open('customers.json', 'r') as file:
            customers = json.load(file)
    except FileNotFoundError:
        print("File not found")
    for customer in customers:
        data = {
            "name": customer["name"],
            "email": customer["email"],
            "phone": customer["phone"]
        }
        for key, value in customer["metadata"].items():
            data[f"metadata[{key}]"] = value
        try:
            headers = {
                'Authorization': f"Bearer {api_key}"
            }
            response = requests.post(url, data=customer, headers = headers)
            response.raise_for_status()
            response_data = response.json()
            customer_id = customer["metadata"]["internal_id"]
            stripe_id = response_data["id"]
            print(f"{customer_id} -> {stripe_id}")
        except requests.exception.RequestException as e:
            print(e)
create_customers('customers.json')