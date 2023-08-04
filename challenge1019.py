value = int(input()) # seconds
# value = 556

hours = value // 3600
rest1 = value - (3600 * hours)

# print(hours)

minutes = rest1 // 60
rest2 = rest1 - (60 * minutes)

# print(minutes)

seconds = rest2

# print(seconds)

# hours:minutes:seconds
print(hours, minutes, seconds, sep=':')