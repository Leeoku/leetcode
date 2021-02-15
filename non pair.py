#Given an array of items in pairs, there is one exception. Find it and return that value.
#[1 2 1 3 3] -> 2
#[1 1 3 2 3] -> 2

#### Searching:

def find_lonely(arr: [int]) -> int:
    for i in range(len(arr)):
        for j in range(len(arr)): #range(0,2) -> [0,1]
            if arr[i] == arr[j] and i != j:
                break
        return arr[i]

n: number of elements in arr, or length of arr
Time: O(n^2)
Space: O(n)

#### Sorting:

def find_lonely(arr: [int]) -> int:
    arr = sorted(arr) #returns sorted copy of arr O(nlogn)
    #arr.sort() #will modify arr


    for i in range(len(arr)): O(n)
        #check for odd indices
        if i % 2 = 1:
            continue 
        if i = len(arr)-1 or arr[i] == arr[i+1]: 
            break
    return arr[i]

#O(nlogn + n) = (nlogn)

Time: O(nlogn)
Space: O(n)

#### Dictionaries (in Python) = Hash Tables = Hash Maps (in Java):

d = {}
d['whatever'] = 12398712
d[myVariable] = ['2312',21]
d['whatever'] -= 1

for key, value in d.items():
    d[key] = value

for x in d.items():
    x[0], x[1]

d.get(item, default)
d[pedro] += 1 #IndexError
->
d[pedro] = d.get(pedro, 0) + 1
defaultdict(int)
d[pedro] += 1


from collections import defaultdict

def find_lonely(arr: [int]) -> int:
    d = defaultdict()
    for elt in arr:
        d[elt] += 1

    for val, count in d.items():
        if count == 1:
            return val

    return sorted(d.items(), key = lambda x: x[1])[0][0]

Time: O(n)
Space: O(n)

#### 

def find_lonely(arr: [int]) -> int:
    xor = 0
    for elt in arr: 
        xor ^= arr
    return xor

O(n)
O(1)

# Inputs: 
# Input of type array, 
# all integers, 
# always have one output,
# Length of array is always odd 
# Possible to have more than two instances of the same integer

# Output:
# Return one integer value

# Exception:
# array of size 0,
# array of size 1

Analysis:
 Given length n array
 Take the value of i and divide by n

Brute Force
 Given arr
Loop through all values in the array, 
    for each one, then i will compare to the next value
        if the value at i = value i+next
            then I can
























def test_cases():
    t = [([1],2),([1,1,2,3,3],2),([1,3,2,1,3],2),([1,1,2,2,3,3,4,4,5,5,6,6,7],7)]

    for case, ans in t:
        print(ans == find_lonely(case))