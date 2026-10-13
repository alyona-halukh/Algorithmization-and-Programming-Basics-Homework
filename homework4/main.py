number = 13

mask = 1 << 3

bit = (number & mask) != 0

result = number << 3

print("3-й біт увімкнений:", bit)
print("Число * 8:", result)