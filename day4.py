
numbers = [10, 20, 10, 30, 20, 10]

visited = []

for num in numbers:

    if num not in visited:

        count = 0

        for value in numbers:
            if num == value:
                count = count + 1

        print(num, "appears", count, "times")

        visited.append(num)
