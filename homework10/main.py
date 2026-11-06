def digital_root(n):
    if n < 10:
        return n

    total = 0

    for digit in str(n):
        total += int(digit)

    return digital_root(total)


number = 9875

result = digital_root(number)

print("Цифровий корінь:", result)