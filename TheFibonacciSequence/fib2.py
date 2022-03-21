from sys import argv


def fib2(n: int) -> int:
    # specify base case
    if n < 2:
        return n
    # specify recursive case
    return fib2(n - 1) + fib2(n - 2)


if __name__ == "__main__":
    print(fib2(int(argv[1])))
