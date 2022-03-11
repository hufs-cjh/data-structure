import random
import time


# code for O(n^2)-time function (Naive)
def evaluate_n2(A, x, n):
    result = A[0]
    for i in range(1, n):
        result += (x ** i) * A[i]

    return result


# code for O(n)-time function (Horner's method)
def evaluate_n(A, x, n):
    result = A[n - 1]
    for i in range(n - 2, -1, -1):
        result = (result * x) + A[i]

    return result


# code for measure function time
def calc_time(func, args):
    start = time.process_time()
    func(args[0], args[1], args[2])
    end = time.process_time()

    return end - start


random.seed()                       # initialize random
x = random.randint(-1000, 1000)     # initialize x

# initialize list A and fill with randint
A = []
for i in range(100000):
    A.append(random.randint(-1000, 1000))

for i in range(1000, 100000, 1000):
    n2 = round(calc_time(evaluate_n2, [A, x, i]), 3)
    n1 = round(calc_time(evaluate_n, [A, x, i]), 3)
    print(f"n = {i}\t\tO(n^2): {n2}\t\tO(n): {n1}")
    
