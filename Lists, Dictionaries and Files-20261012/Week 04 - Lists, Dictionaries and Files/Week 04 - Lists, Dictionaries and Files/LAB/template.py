"""
RECORD CHECK  -  my version
===========================

Name  :YUNUS AHAMED SHAIK
Lane  :  AI 
Date  :01/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Calculates the difference, percentage, and status based on value and limit."""
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_record(label, value, limit, difference, percent, status):
    """Prints the report based on the provided values."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"label: {label}")
    print(f"value: {value:.2f}")
    print(f"limit: {limit:.2f}")
    print(f"difference: {difference:.2f}")
    print(f"percent: {percent:.2f}%")
    print(f"status: {status}")
    print("=" * 34)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "Record 1", "value": 120.0, "limit": 100.0},
    {"label": "Record 2", "value": 85.0, "limit": 100.0},
    {"label": "Record 3", "value": 95.0, "limit": 100.0}
]   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]
    
    difference, percent, status = check_record(value, limit)
    print_record(label, value, limit, difference, percent, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
