count = 9
number_list = []

while(count > 0):
    number_list.append(int(input()))
    count = count -1

max = number_list[0]
index_number = 0

for i in range(len(number_list)):
    if (max < number_list[i]):
        max = number_list[i]
        index_number = i

print(max, index_number + 1)

