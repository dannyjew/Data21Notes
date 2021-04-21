def doublefunction(x: int):
    return x*2


def fizzbuzz(divisor1, divisor2, max_number: int):
    result = []
    for number in range(1, max_number):
        if number % divisor1 == 0 and number % divisor2 == 0:
            result.append("FizzBuzz "+str(number))
        else:
            continue
    return result


for x in fizzbuzz(3, 5, 20):
    print(x)




