# JU: Improve on line 5 by using "in" to cehck dict keys

hols = {"Jan 1":"New Year's Day", "Jul 1":"Canada Day","Dec 25":"Christmas Day"}
date = input("What is the date and month e.g. Jul 1:  ")
if date == 'Jan 1' or date == 'Jul 1' or date == 'Dec 25':
    print(hols[date])
else:
    print("Error Input another date")