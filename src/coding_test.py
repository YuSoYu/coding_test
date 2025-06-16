# 입력한 숫자 만큽 입력하는 기능 

n = int(input())

number_count = n

number_list = []

while(number_count > 0):

    number_list.append(int(input()))
    number_count = number_count - 1

print(number_list)


