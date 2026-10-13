import math

a = 3.0
b = 4.0
expected_c = 5.0

c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c

matches = abs(c - expected_c) <= 1e-6

print("Гіпотенуза:", c)
print("Периметр:", perimeter)
print("Збігається:", matches)