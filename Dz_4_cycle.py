#####################    1
my_list = [100, 200, 350, 700, 554, 8, 68, 11, 0]
for value in my_list:
    if value > 100:
        print(value)

#####################     2
my_list = [100, 200, 350, 700, 554, 8, 68, 11, 0]
my_result = []
for value in my_list:
    if value > 100:
        my_result.append(value)
print(my_result)
#####################     3
my_list = [100, 5, 45, 789, 31, 1]
if len(my_list) < 5:
    my_list.append(0)
else:
    summ_value = my_list[-1] + my_list[-2]
    my_list.append(summ_value)
print(my_list)
