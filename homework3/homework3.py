def say_goodbye(name):
	print("Goodbye,", name)

def circle_area(radius):
	print((radius**2)*3.14)

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def return_temps(list1):
	return (min(list1), max(list1))

def is_weekend(num):
	if num == 6 or num == 7:
		return True
	else: 
		return False

def fuel_efficiency(distance, fuel):
	return distance / fuel

def encrypt(integer):
    return (integer // 10) + (10000 * (integer % 10))

def power(x, y):
	a = x
	for i in range(y):
		a *= x
	return a

def min(list1):
	a = list1[0]
	for value in list1:
		if value < a:
			a = value
	return a

def max(list1):
        a = 0
        for value in list1:
                if value > a:
                        a = value
        return a

def min2(list1):
	a = 0
	b = list1[a]
	while a < len(list1):
		if b > list1[a]:
			b = list1[a]
		a += 1
	return b

def max2(list1):
	a = 0
	b = 0
	while a < len(list1):
		if b < list1[a]:
			b = list1[a]
		a += 1
	return b

def sum(integer):
	a = 0
	b = 0
	while a < len(integer):
		b += integer[a]
		a += 1
	return b


list1 = [88, 56, 9, 43, 100, 2]

result = max2([88, 56, 9, 43, 100, 2]) #maximum of the defined list

print(f"The result of searching for the maximum of the list {list1} is {result}")




