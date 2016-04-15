sum = 0
number1 = 1
number2 = 2
while number2 < 4000000:
    number2 = number1 + number2
    number1 = number2 - number1
    if number2 % 2 == 0:
        sum += number2
print(num)
    
