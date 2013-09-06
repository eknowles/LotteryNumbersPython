import random

numbers = [] 
stars = []

def rollnumber(a, b, type):
	roll = random.randint(a, b)
	if roll not in type:
		return roll
	else:
		roll = random.randint(a, b)
		if roll not in type:
			return roll

for i in range(0,5):
	numbers.append(rollnumber(1,50, numbers))

for i in range(0,2):
	stars.append(rollnumber(1,11, stars))

stars.sort()
numbers.sort()

print numbers, stars