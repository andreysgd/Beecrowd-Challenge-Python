value = int(input()) # age in days
# value = 800

years = value // 365
rest1 = value - (365 * years)

# print(years)

months = rest1 // 30
rest2 = rest1 - (30 * months)

# print(months)

days = rest2

# print(days)

print("%i ano(s)" % years)
print("%i mes(es)" % months)
print("%i dia(s)" % days)