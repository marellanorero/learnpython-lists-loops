arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
arr = []

def sumOdds(items):
    for i in items:
        if i % 2 != 0:
            arr.append(i)
        else:
            None

for x in arr:
    total = 0
    total += x
    print(total)





