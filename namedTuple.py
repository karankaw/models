person1 = ("Rohit", 23, "IT Programmer")
person2 = ("Rahul", 45, "Call Centre")

for a in [person1, person2]:
	print("%s is %d old and works as %s" % a)

print(person1[2])

import collections
person = collections.namedtuple('Personified', 'name, age, profession')
p1 = person(name="Vikas", age=31, profession="Driver")
p2 = person(name="Shilpa", age="19", profession="HR")

print(type(p1))
print(p1.age) 
print(p2.name)
print(p2.age)


