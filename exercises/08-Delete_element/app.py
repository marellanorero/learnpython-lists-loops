people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
new_people = []

def deletePerson(person):
    for i in people:
        if person == i:
            people.remove(person)
            new_people.append(people)
    return new_people
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))