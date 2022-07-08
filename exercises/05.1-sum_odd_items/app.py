arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
new_param = []

for i in arr:
    if i % 2 != 0:
        new_param.append(i)

print(new_param)

def sumOdds(items):
    total= 0
    for i in items:
        total += i
    return total

print(sumOdds(new_param))






