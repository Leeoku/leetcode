# Re-ID
# =====

# There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, 
# Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

# She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, 
# and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

# Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. 
# Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) n = 0
# Output:
#     (string) "23571"

# Inputs:
#     (int) n = 3
# Output:
#     (string) "71113"

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

max = 10000
digits = 5


def primes(n):
    #Sieve of Eratosthene
    primes = [True] * n
    primes [0] =  primes [1] = False
    # print(primes)

    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n , i):
                primes[j] = False
    
    #Make a list of all the prime numbers
    # print([i for i, x in enumerate(primes) if x])
        
    prime_list = []
    for count, number in enumerate(primes) :
        if number:
            prime_list.append(count)
    return prime_list

def getString():
    #make a string of all the prime numbers
    id_full = ''.join(str(num) for num in primes(max))
    return id_full

def answer(n):
    #Get the full string
    id_string = getString()
    #Get just the nth digit and 5 digits after
    id = id_string[n:n+digits]
    print(id)
    return(id)

# primes(max)
# getString(max)
answer(3)

