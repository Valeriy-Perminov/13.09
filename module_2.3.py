my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = 0
while numbers < len(my_list):
    if my_list[numbers] < 0:
        break
    if my_list[numbers] != 0:
        print(my_list[numbers])
    numbers += 1