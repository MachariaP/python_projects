#!/usr/bin/python3

# A python script to display calender.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)
