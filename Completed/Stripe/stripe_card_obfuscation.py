'''
Stripe's card metadata API maps intervals within each BIN range to card brands. Gaps in the
returned intervals can be exploited by fraudsters. Fill those gaps so the entire BIN range is
covered with no holes.
Input Format
bin_prefix = "123456"
intervals = [
{"start": "1234561000000000", "end": "1234563999999999", "brand": "VISA"},
{"start": "1234565000000000", "end": "1234567999999999", "brand": "MASTERCARD"},
]
Part 1 — Fill Edge Gaps
Extend the lowest interval to the BIN range start and the highest to the BIN range end.
def fill_edge_gaps(bin_prefix: str, intervals: list) -> list:
Part 2 — Fill Middle Gaps
Fill gaps between intervals by extending the lower interval's end.
def fill_all_gaps(bin_prefix: str, intervals: list) -> list:
Part 3 — Handle Subset Intervals
Input may contain intervals that are subsets of other intervals. Only extend the covering interval,
not any subset within it.
def fill_gaps_with_subsets(bin_prefix: str, intervals: list) -> list:
Constraints
• BIN prefix is always 6 digits; card numbers are always 16 digits
• If input already covers full range, return it sorted
• Intervals are non-overlapping in Parts 1 and 2
'''
bin_prefix = "123456"
intervals = [
{"start": "1234561000000000", "end": "1234563999999999", "brand": "VISA"},
{"start": "1234565000000000", "end": "1234567999999999", "brand": "MASTERCARD"},
]
subset_intervals = [
    {"start": "1234561000000000", "end": "1234567999999999", "brand": "VISA"},
    {"start": "1234563000000000", "end": "1234565999999999", "brand": "MASTERCARD"},
]
#part 1
# def fill_edge_gaps(bin_prefix: str, intervals: list) -> list:
#     minimum_bin = int(bin_prefix+'0'*10)
#     maximum_bin = int(bin_prefix+'9'*10)
#     lowest = None
#     highest = None
#     print(minimum_bin, maximum_bin)
#     for interval in intervals:
#         if lowest is None or interval["start"] < lowest["start"]:
#             lowest = interval
#         if highest is None or interval["end"] > highest["end"]:
#             highest = interval
#     lowest["start"] = minimum_bin
#     highest["end"] = maximum_bin
#     return sorted(intervals, key = lambda x: x["start"])
    
def fill_edge_gaps(bin_prefix: str, intervals: list) -> list:
    minimum_bin = bin_prefix+'0'*10
    maximum_bin = bin_prefix+'9'*10

    lowest = min(intervals, key=lambda x: x["start"])
    highest = max(intervals, key=lambda x: x["end"])
    lowest["start"] = minimum_bin
    highest["end"] = maximum_bin
    return sorted(intervals, key = lambda x: x["start"])
# fill_edge_gaps(bin_prefix, intervals)

#part 2
def fill_all_gaps(bin_prefix: str, intervals: list) -> list:
    filled_intervals = fill_edge_gaps(bin_prefix, intervals)
    for i in range(len(filled_intervals) - 1):
        current_end = int(filled_intervals[i]["end"])
        next_start  = int(filled_intervals[i + 1]["start"])
        if current_end != next_start - 1:
            filled_intervals[i]["end"] = str(next_start - 1)
    return filled_intervals

#Part3

def is_subset(interval:list, intervals: list) -> bool:
    for other in intervals:
        if interval is other:
            continue
        if other["start"] <= interval["start"] and other["end"] >= interval["end"]:
            return True
    return False
def fill_gaps_with_subsets(bin_prefix: str, intervals: list) -> list:
    subsets = []
    remaining = []
    for interval in intervals:
        if is_subset(interval, intervals):
            subsets.append(interval)
        else:
            remaining.append(interval)
    filled = fill_all_gaps(bin_prefix, remaining)
    print(f"subset{subsets}, remaining{remaining}")
    print(sorted(filled+subsets, key=lambda x: x["start"]))
    # return sorted
    return sorted(filled+subsets, key=lambda x: x["start"])

fill_gaps_with_subsets(bin_prefix, subset_intervals)