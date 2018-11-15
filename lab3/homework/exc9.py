def get_even_list(list):
    even_list = []
    for i in list:
        if i%2 == 0:
            even_list.append(i)
    return even_list

print(get_even_list([1, 4, 5, -1, 10]))