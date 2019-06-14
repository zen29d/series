"""
Generate a combination series of Fibonacci and Prime,
the odd place is Fibo number and
the even place is Prime number
"""

import sys

# Generate Nth Fibonacci Number
def fib(N):
    a, b = 0, 1
    for index in range(N):
        a, b = a+b, a
    return a

# Generate Nth Prime Number
def prime(N):
    p = 0
    count = 0
    val = 0
    while(count<=N):
        val += 1
        for num in range(2, (val//2)+1):
            if(val%num == 0):
                break
        else:
            p=val
            count += 1
    return p

# command line arg to intialize N
if(len(sys.argv)>1):
    N = int(sys.argv[1])
else:
    N = 1
    sys.stdout.write("try "+sys.argv[0]+" arg\n")


fp_series = []

for i in range(1, N+1):
    fp_series.append(fib(i))
    fp_series.append(prime(i))


print(fp_series)
print(fp_series[N-1])