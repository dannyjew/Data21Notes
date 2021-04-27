def addition(num1, num2):
    return num1 + num2


add = lambda num1, num2: num1 + num2

print(add(5,9))



savings = [234, 555, 674, 78]
bonus = [0, 0 ,0 ,0 ,0]

bonus = list(map(lambda  number1: number1*1.1, savings)) # takes the savings list and adds 10% to each entry and saves to another list

print(bonus)
