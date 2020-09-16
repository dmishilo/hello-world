my_list = ['red', 'green', 'yellow']

print(my_list)
print("the length {}".format(len(my_list)))

for i in range(0, len(my_list)):
    print(my_list[i])

for i in range(0, len(my_list)):
    my_list.append(i)

print(my_list.pop())
print(my_list)


