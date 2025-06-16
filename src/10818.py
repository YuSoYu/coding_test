n = int(input())

#print(f"현재 입력하신 값은 {n}개 입니다.")

number_list = list(map(int, input().split()))

if len(number_list) == n:

    min = number_list[0]
    max = number_list[0]

    for i in range(1, len(number_list)):
        if(min > number_list[i]):
            min = number_list[i]

        if(max < number_list[i]):
            max = number_list[i]

        #print(f"현재 최소값은 {min} 현재 최대값은 {max}")


print(min, max)


    






