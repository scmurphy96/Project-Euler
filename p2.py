# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

i = 1
j = 2
h = 0
g = 0

while i < 4000000 or j < 4000000:
    if i % 2 == 0:
        g += i / 2
    elif j % 2 == 0:
        g += j / 2

    h = i + j
    
    if i < j:
        i = h
    elif j < i:
        j = h
print(g)