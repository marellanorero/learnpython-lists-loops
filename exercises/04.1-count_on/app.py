my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list = []
for i in my_list:
    if type(i) == dict:
        new_list.append(i)
    elif type(i) == list:
        new_list.append(i)
    else:
        None

print(new_list)