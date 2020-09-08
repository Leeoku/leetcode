#Count the number of prime numbers less than a non-negative number, n.

#test case, n = 10

class Solution:
    def countPrimes(self, n: int) -> int:
        #Sieve of Eratosthenes
        #Make array for all integers, assume they are prime
        #Time = O(nlogn) (inner loop runs fewer runs), 
        #Space = O(n) , traverse through n numbers

        if n < 2:
            return 0
        primes = [True] * n
        #Set case scenario for 0,1 as not prime exception
        primes[0]= primes[1] = False
        for i in range(2,n):
            if primes[i]:
                #Find numbers that aren't prime up to the square (next multiple)
                for j in range(i*i, n, i):
                    primes[j] = False
                # j = i*i
                # while j < n :
                #     primes[j] = False
                #     j+=i
        print(primes)
        return primes.count(True)

        #BRUTE FORCE
        #Time O(n^2), Space O(n)
        #Loop thru all the numbers and check to see if they are divisible by each number
        # count  = 0
        # def isPrime(x):
        #     for i in range(2,x):
        #         if x % i == 0:
        #             return False
        #     return True
        # for j in range(2,n):
        #     if isPrime(j) == True:
        #         count +=1
        # return count


#         primes = []
#         count = 0
#         if n < 2:
#             return None
#         for i in range(2,n):
#             for j in range(2,i):
#                 if j == 2:z
#                     count +=1
#                 #if divisible, that means it's not a prime number    
#                 if i % j == 0:
#                     break
#             count += 1
#             primes.append(i)
#         return count, primes


n = 10
s = Solution()
total = s.countPrimes(n)
print(f"Total number of primes is {total}")
# print(s.isPrime(n))
# print(total)
# print(total.count(True))