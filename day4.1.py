
numbers = [5, 2, 5, 3, 2, 5, 2, 2]

visited = []

max_count = 0
most_frequent = None

for num in numbers:

    if num not in visited:

        count = 0

        for value in numbers:
            if num == value:
                count = count + 1

        if count > max_count:
            max_count = count
            most_frequent = num

        visited.append(num)

print("Most frequent element:", most_frequent)
print("Frequency:", max_count)
