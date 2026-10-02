from unittest import result

number = int(input("Введіть трицифрове число: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

result = hundreds ** 2 + tens ** 2 + units ** 2

print("Сума квадратів цифр:", result)