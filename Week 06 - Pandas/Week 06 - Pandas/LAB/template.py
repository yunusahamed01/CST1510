"""
RECORD CHECK  -  my version
===========================
Name  : Yunus Ahamed Shaik
Lane  :  AI       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).


data = pd.read_csv("C:\\Users\\skyun\\Downloads\\Week 06 - Pandas\\Week 06 - Pandas\\LAB\\mydata.csv")

print(data)



# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
data['percent'] = (data['value'] / data['limit']) * 100

#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".
data['status'] = data['percent'].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")    
# your column(s) go here
print(data)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
print(data[data['status'] != "OK"])
print(data[data['status'] != "OK"])
#    Excellent : also group by "status" and print a count per group, save
data.to_csv("final_data.csv", index=False)
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
import matplotlib.pyplot as plt
data['status'].value_counts().plot(kind='bar')
plt.title('Count of Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.show()



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
print(data.iloc[0])  # Check the first row for correctness
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
print(data.columns)  # Print column names to verify
print(data)