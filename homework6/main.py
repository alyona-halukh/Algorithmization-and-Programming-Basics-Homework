text = input("Введіть слово: ")
shift = 3

result = ""

for char in text:
    code = ord(char)
    code = code + shift

    if code > ord('z'):
        code = code - 26

    result = result + chr(code)

print("Зашифрований текст:", result)