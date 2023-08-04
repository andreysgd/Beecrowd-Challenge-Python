a, b, c = map(int, input().split())

numbers = [a, b, c]
numbers_sorting = numbers

numbers_sorting.sort()

print("{}\n{}\n{}\n".format(numbers_sorting[0], numbers_sorting[1], numbers_sorting[2]))
print("{}\n{}\n{}".format(a, b, c))