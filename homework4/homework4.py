list1 = ["brownies", "matcha", "yogurt", "coffee", "poke"]

print(list1[1])
print(list1[-1])
list1.append("pizza")
list1.insert(0, "apple")
list1.remove(list1[2])
print(len(list1))
for word in list1:
	print(word.upper())

list2 = [list1[0], list1[-1]]

if "potato" in list1:
	print("A potato!")
else:
	print("No potato!")

numbers = []
for i in range(21):
	numbers.append(i)
def get_first_15_numbers(nums):
	return nums[:15]
def get_every_5th(nums):
	return get_first_15_numbers(nums)[::5]
def reverse_and_stride(nums):
	return get_every_5th(nums)[::-3]
numbers2 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers2[2])
print(numbers2[2][1])
numbers2.append([10, 11, 12])
def sum_nested(nums):
	sums = []
	for i in range(len(nums)):
		a = 0
		for e in range(len(nums[i])):
			a += nums[i][e]
		sums.append(a)
	return sums

def num_by_num(a, b):
	the_list = []
	index = 0
	for i in range(a):
		inside_list = []
		for i in range(b):
			index += 1
			inside_list.append(index)
		the_list.append(inside_list)
	return the_list

five_by_five = num_by_num(5, 5)

def question(list1):
    the_list = []
    for item in list1:
        row = []
        for i in range(len(item)):
            if (item[i] % 3) == 0:
                row.append("?")
            else:
                row.append(item[i])
        the_list.append(row)

    return the_list

five_by_q = question(five_by_five)

def not_equal_sum(listy):
	s = 0
	for item in listy:
		for i in range(len(item)):
			if item[i] != "?":
				s += item[i]
	return s

sum_five_by_q = not_equal_sum(five_by_q)

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mariam"] = 100
ages["Milana"] = 52
ages.pop("Mariam")

for key in ages:
	print(key, ages[key])

print(num_by_num(2, 9))
