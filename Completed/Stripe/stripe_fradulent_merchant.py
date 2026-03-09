'''
Background
Each merchant is assigned a Merchant Category Code (MCC). Each MCC has a configurable
fraud threshold. Process a stream of CHARGE and DISPUTE events in real time and flag
merchants as fraudulent based on their dispute history.
Input Format
MCC Configuration:
[
{"mcc": "5411", "threshold": 3, "threshold_type": "count"},
{"mcc": "7995", "threshold": 0.5, "threshold_type": "ratio"},
]
• count: fraudulent if disputes >= threshold (int)
• ratio: fraudulent if disputes/charges >= threshold (float)
Event Stream:
[
{"event": "CHARGE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "CHARGE", "merchant_id": "M01", "mcc": "5411", "amount": 80},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 80},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "CHARGE", "merchant_id": "M02", "mcc": "7995", "amount": 200},
{"event": "DISPUTE", "merchant_id": "M02", "mcc": "7995", "amount": 200},
]
Part 1 — Track Charges and Disputes
def process_events(events: list) -> dict:
# returns {merchant_id: {"charges": int, "disputes": int, "mcc": str}}
Part 2 — Flag by Count Threshold
def flag_by_count(stats: dict, mcc_config: list) -> list:
Part 3 — Flag by Ratio Threshold
Handle division by zero: skip merchants with 0 charges.
def flag_by_ratio(stats: dict, mcc_config: list) -> list:
Part 4 — Combined Fraud Report
def get_fraudulent_merchants(events: list, mcc_config: list) -> list:
Expected Output
get_fraudulent_merchants(events, mcc_config)
# ["M01", "M02"]
# M01: 3 disputes >= count threshold 3 -> fraudulent
# M02: 1/1 = 1.0 >= ratio threshold 0.5 -> fraudulent
Constraints
• Events processed in order; each merchant has exactly one MCC
• Merchant with 0 charges: skip ratio evaluation
• Return sorted list of fraudulent merchant IDs
'''

from collections import defaultdict, Counter

configuration = [
{"mcc": "5411", "threshold": 3, "threshold_type": "count"},
{"mcc": "7995", "threshold": 0.5, "threshold_type": "ratio"},
]

events = [
{"event": "CHARGE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "CHARGE", "merchant_id": "M01", "mcc": "5411", "amount": 80},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 80},
{"event": "DISPUTE", "merchant_id": "M01", "mcc": "5411", "amount": 120},
{"event": "CHARGE", "merchant_id": "M02", "mcc": "7995", "amount": 200},
{"event": "DISPUTE", "merchant_id": "M02", "mcc": "7995", "amount": 200},
]

#Part 1
# def process_events(events: list) -> dict:
#     stats = {}
#     for event in events:
#         merchant_id = event["merchant_id"]
#         mcc = event["mcc"]
#         if merchant_id not in stats:
#             stats[merchant_id] = {"charges": 0, "disputes": 0, "mcc": mcc}
#         if event["event"] == "CHARGE":
#             stats[merchant_id]["charges"] += 1
#         if event["event"] == "DISPUTE":
#             stats[merchant_id]["disputes"] += 1
#     print(stats)

def process_events(events: list) -> dict:
    # returns {merchant_id: {"charges": int, "disputes": int, "mcc": str}}
    stats = defaultdict(lambda: {"charges": 0, "disputes": 0, "mcc": ""})
    for event in events:
        merchant_id = event["merchant_id"]
        stats[merchant_id]["mcc"] = event["mcc"]
        if event["event"] == "CHARGE":
            stats[merchant_id]["charges"] += 1
        if event["event"] == "DISPUTE":
            stats[merchant_id]["disputes"] += 1
    # print(dict(stats))
    return dict(stats)
stats = process_events(events)

# print(stats)
#Part 2
def flag_by_count(stats: dict, mcc_config: list) -> list:
    flagged_merchants = []
    for merchant_id, data in stats.items():
        for config in mcc_config:
            if config["mcc"] == data["mcc"] and config["threshold_type"] == "count":
                if data["disputes"] >= 3:
                    flagged_merchants.append(merchant_id)
    # print(flagged_merchants)
    return flagged_merchants

# def flag_by_count(stats: dict, mcc_config: list) -> list:
#     flagged_merchants = []
#     threshold_map = {}
#     for config in mcc_config:
#         if config["threshold_type"] == "count":
#             threshold_map[config["mcc"]] = config["threshold"]
#     print(threshold_map)

#     for merchant_id, data in stats.items():
#         mcc = data["mcc"]
#         if mcc in threshold_map and data["disputes"] >= threshold_map[mcc]:
#             flagged_merchants.append(merchant_id)
#     print(flagged_merchants)
#     return flagged_merchants

# flag_by_count(stats, configuration)

#Part 3
def flag_by_ratio(stats: dict, mcc_config: list) -> list:
    flagged_merchants = []
    for merchant_id, data in stats.items():
        if data["charges"] == 0:
            continue
        for config in mcc_config:
            ratio = data["disputes"]/data["charges"]
            if config["mcc"] == data["mcc"] and config["threshold_type"] == "ratio" and ratio >= config["threshold"]:
                flagged_merchants.append(merchant_id)
    # print(flagged_merchants)
    return flagged_merchants
                


# flag_by_ratio(stats, configuration)

#Part 4
def get_fraudulent_merchants(events: list, mcc_config: list) -> list:
    stats = process_events(events)
    fraudulent_merchants_by_ratio = flag_by_ratio(stats, configuration)
    fraudulent_merchants_by_count = flag_by_count(stats, configuration)
    return sorted(fraudulent_merchants_by_count + fraudulent_merchants_by_ratio)

get_fraudulent_merchants(events, configuration)