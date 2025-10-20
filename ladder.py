def my_steps(n: int) -> int:
    if type(n) is not int or n < 1 or n > 25:
        raise ValueError("n must be an integer between 1 and 25 inclusive")

    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev, curr = 1, 2
    for step in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
