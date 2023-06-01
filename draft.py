# num1 = 11

# num2 = num1 

# print("Before num2 value is update:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# num2 = 22

# print("Before num2 value is update:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

dic_one = {'value': 1}
dic_two = {'value' : 2}

print("dic_one points to", id(dic_one))
print("dic_two points to", id(dic_two))

dic_one = dic_two

print("dic_one points to", id(dic_one))
print("dic_two points to", id(dic_two))

print('the value in dic_one is:', dic_one['value'])
