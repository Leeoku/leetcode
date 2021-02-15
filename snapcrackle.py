# From n = 1 to 100, write a program that does the following: 
# - if n is divisible by 3 or contains a 3, output the number and the word "snap"
# - if n is divisible by 7 or contains a 7, output the number and the word "crackle"
# - if n is divisible by 3 or contains a 3 and is divisible by 7 or contains a 7, output the number and the words "snap" and "crackle"

# Example":
# 1
# 2
# 3 snap
# 4
# 5
# 6
# 7 crackle
# ...
# 21 snap crackle
# ...
# 100


#Python solution
def SnapCrackle(n):
    if n < 1 or n > 100:
        return ('Invalid value of n')
    return [str(i) + " snap"*(not i%3 or '3' in str(i)) +" crackle"*(not i%7 or '7' in str(i)) or str(i) for i in range(1,n+1)]

if __name__ == "__main__":
    print(SnapCrackle(100))