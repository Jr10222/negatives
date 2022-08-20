numbers = [-2, -9, 72, -23, -3, 7, 91, 12, -12, 0, -6, 3, 18, -50, 11]
doubled_negatives = []


for number in numbers:
    if number >= 0:
        continue
    doubled_negatives.append(number * 2)
print(doubled_negatives)
