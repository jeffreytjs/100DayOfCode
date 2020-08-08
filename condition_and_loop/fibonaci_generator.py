# Day 14 - Problem 17

# Challenge
# Write a Python program to get the Fibonacci series between 0 to 50


def find_fibo(first, last):
    results = []
    i = first
    while i <= last:
        if len(results) <= 1:
            results.append(i)
            i += 1
        else:
            next_fib = results[-1] + results[-2]
            if next_fib <= last:
                results.append(next_fib)
                i = next_fib
            else:
                print(results)
                return results


first = 0
last = 50
find_fibo(first, last)
