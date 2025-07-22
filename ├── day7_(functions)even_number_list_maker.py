def even_num_list_maker(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
print(even_num_list_maker([1,2,3,4,5,6,7,8,9]))