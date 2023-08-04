# carMakes = 12 km/l

spentTime = int(input()) # in hours
averageSpeed = int(input()) # km/h

distance = spentTime * averageSpeed

litersNeeded = distance/12

print("%.3f" % litersNeeded)
