def find_gcd(first_number, second_number):

    first_number_set = set()
    second_number_set = set()

    for i in range(1, first_number + 1 if first_number > second_number else second_number + 1):

        if first_number >= i and second_number >= i:
            if first_number % i == 0 and second_number % i == 0:
                first_number_set.add(i)
                second_number_set.add(i)
            elif first_number % i == 0:
                first_number_set.add(i)
            elif second_number % i == 0:
                second_number_set.add(i)
        elif first_number >= i:
            if first_number % i == 0:
                first_number_set.add(i)

        elif second_number >= i:
            if second_number % i == 0:
                second_number_set.add(i)

    print(first_number_set, second_number_set)

    return max(list(first_number_set.intersection(second_number_set)))


print(find_gcd(14, 8))
