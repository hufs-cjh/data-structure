import random
import time


# code for O(n^2)-time function (Naive)
def evaluate_n2(A, x):
    result = A[0]
    for i in range(1, len(A)):
        result += (x ** i) * A[i]

    return result


# code for O(n)-time function (Horner's method)
def evaluate_n(A, x):
    result = A[len(A) - 1]
    for i in range(len(A) - 2, -1, -1):
        result = (result * x) + A[i]

    return result


# code for measure function time
def calc_time(func, args):
    start = time.process_time()
    func(args[0], args[1])
    end = time.process_time()

    return end - start

for i in range(1000, 100000, 1000):
    random.seed()
    x = random.randint(-1000, 1000)
    A = []
    for j in range(i):
        A.append(random.randint(-1000, 1000))

    n2 = calc_time(evaluate_n2, [A, x])
    n = calc_time(evaluate_n, [A, x])

    print(f"n = {i}\t\tn2:{n2}\tn1:{n}")
