
numbers = [12, 35, 1, 10, 34, 1]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

if second_largest is None:
    print("Second largest element does not exist")
else:
    print("Second largest element:", second_largest)
