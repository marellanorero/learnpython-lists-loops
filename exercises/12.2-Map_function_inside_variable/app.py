names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
#Your code go here:
new_names = list(map(prepender, names))
print(new_names)