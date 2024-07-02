import random


def bubble(numbers):
    n = len(numbers)
    for j in range(0, n-1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j+1] = numbers[j + 1], numbers[j]
    return numbers
        


def main():
    numbers = [2, 3, 0, 5, 4]
    print(numbers)
    bubble(numbers)
    print(numbers)    # must be [2, 0, 3, 4, 5]

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
