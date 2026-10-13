numbers = [12, 45, 2, 89, 34, 6, 90, 23]

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

    if num > maximum:
        maximum = num

difference = maximum - minimum

print("Мінімум:", minimum)
print("Максимум:", maximum)
print("Різниця:", difference)