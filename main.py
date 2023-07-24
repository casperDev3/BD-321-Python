def fib(first_number, second_number, end_number):
    fib_numbers = []
    while second_number <= end_number:
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
        if second_number <= end_number:
            fib_numbers.append(next_number)

    return fib_numbers


if __name__ == "__main__":
    print(fib(1, 2, 100))





