people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
arr = []
def deletePerson(person_name):
    #Your code go here:
    for person_name in people:
        if person_name == people:
            del(people)
    return people
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))