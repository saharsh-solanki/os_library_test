def longest_even_sublist(numbers):
    longest = []
    current = []

    for num in numbers:
        if num % 2 == 0:
            current.append(num)
            if len(current) > len(longest):
                longest = current[:]
        else:
            current = []

    return longest


input_list = [138, 224, 152, 133, 94, 152, 4, 178, 89, 3, 77, 147, 238, 113, 176, 124]
print(longest_even_sublist(input_list))  

