from math import factorial

def compute_series(val1, val2):
    series = [val1 ** i / factorial(i) for i in range(val2 + 1)]
    return series

def compute_sum(series):
    sum_series = sum(series)
    return sum_series

value1 = float(input("Enter the value of the first parameter: "))
value2 = int(input("Enter the value of the second parameter: "))

series = compute_series(value1, value2)
result = compute_sum(series)

print(f"The result of the series calculation is: e^{value1} = {result:.3f}")


def compute_sum_recursive(n, total=0):
    if n == 0:
        return total
    term = (-1) ** (n + 1) / n
    total += term
    return compute_sum_recursive(n - 1, total)


n_value = 6
total = compute_sum_recursive(n_value)
print(f"The sum of the recursive series calculation is: {total:.4f}")
