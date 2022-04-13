src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

true_list = []

for el in range(len(src) - 1):
    if src[el] < src[el + 1]:
        true_list.append(src[el + 1])
print(true_list)
