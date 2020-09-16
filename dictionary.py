my_dict = {'apples': {'test':['red', 'green']}, 'oranges': '6', 'lemons': '1', 'pears': '2'}

print(my_dict['apples'])


my_dict['test'] = 9

for key in my_dict:
    print(key)

for key in my_dict:
    print('{}: {}'.format(key, my_dict[key]))




if 'apples' in my_dict:
    print('we have apples')


for entry in my_dict['apples']:
    print(entry)

my_list = [[1,2,3],[3,4,5]]
print(my_list[0][1])