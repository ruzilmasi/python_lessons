src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
repeated_numbers = set()
for number in src:
    if number in repeated_numbers:
        continue
    if number in unique_numbers:
        unique_numbers.discard(number)
        repeated_numbers.add(number)
        continue
    unique_numbers.add(number)
print([number for number in src if number in unique_numbers])
