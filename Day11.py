# Challenge - Calculate the days between two dates

from datetime import datetime
# take user input
date_format = "%Y-%m-%d"
d1_input = input("enter the first date (YYYY-MM-DD):")
d2_input = input("enter the first date (YYYY-MM-DD):")

# converting string to datetime object
date1 = datetime.strptime(d1_input, date_format)
date2 = datetime.strptime(d2_input, date_format)

# calculating the difference
difference = abs((date2-date1).days)
print("Days between:{difference}" ,difference)