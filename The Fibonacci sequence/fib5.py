from sys import argv


def fib5(n: int) -> int:
    # special case
    if n == 0:
        return n
    last: int = 0  # initially set to fib5(0)
    next: int = 1  # initially set to fib5(!)
    for _ in range(1, n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fib5(int(argv[1])))
