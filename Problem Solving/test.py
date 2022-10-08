digit1 = 0
digit2 = 0
digit3 = 0

for digit1 in range (10):
    for digit2 in range (10):
        for digit3 in range (10):
            print(digit1, digit2, digit3)
            digit3 += 1
        digit2 += 1
    digit1 += 1