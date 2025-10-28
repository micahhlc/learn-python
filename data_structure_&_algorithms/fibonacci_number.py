# W3CSchool samples
# https://www.w3schools.com/dsa/dsa_algo_simple.php 

import time

# fibonacci through loop
def fibonacci_loop(n):
    prev2 = 0
    prev1 = 1
    newFibo = 0
    # print(prev2)
    # print(prev1)
    for fibo in range(n):
        newFibo = prev1 + prev2
        # print(newFibo)
        prev2 = prev1
        prev1 = newFibo
    return(newFibo)

# fibonacci_recursion from loop
def fibonacci_recursion(n):
    # print(0)
    # print(1)
    prev_n = 0
    curr_n = 1
    count = 2
    final_list = [0,1]

    def inner_function(n, prev_n, curr_n, count, final_list):
        if count <= n:
            newFibo = prev_n + curr_n
            # print(newFibo)
            final_list.append(newFibo)
            prev_n = curr_n
            curr_n = newFibo
            count += 1
            return inner_function(n, prev_n, curr_n, count, final_list)
        else:
            return final_list
        
    return inner_function(n, prev_n, curr_n, count, final_list)

# full recursion
def fibonacci_fullrecursion(n):    
    if n <= 1: 
        return n
    else:
        return (fibonacci_fullrecursion(n - 1) + fibonacci_fullrecursion(n - 2))

# recursion without counter
def fibo(n, flist = [0, 1]):
    flist_qty = len(flist)
    if n <= 1: 
        return n
    elif n == flist_qty:
        new_fibon_no = flist[n-1] + flist[n-2]
        return new_fibon_no
    else:
        flist.append(flist[flist_qty - 1] + flist[flist_qty - 2])
        print(flist)
        return fibo(n)

def fibo_runtime(func_name):
    start_time = time.time()
    for i in range(20):
        print(f"F{i+1}: {func_name(i)}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(func_name, ": Elapsed time:", elapsed_time * 1000, "milliseconds")

fibo_runtime(fibonacci_loop)

# Nth	Fibonacci number	Total
# 1	0	
# 2	1	1
# 3	1	2
# 4	2	3
# 5	3	5
# 6	5	8
# 7	8	13
# 8	13	21
# 9	21	34
# 10	34	55
# 11	55	89
# 12	89	144
# 13	144	233
# 14	233	377
# 15	377	610