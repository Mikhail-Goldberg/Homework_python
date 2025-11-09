n = int(input('Введите число: '))

def fizz_buzz(n):
     for element in range(1, n + 1):   
        if element % 3 == 0 and element % 5 == 0:
            print('FizzBuzz')
        elif element % 3 == 0:
            print('Fizz')
        elif element % 5 == 0:
            print('Buzz')
        else:
            print(element)

fizz_buzz(n)
