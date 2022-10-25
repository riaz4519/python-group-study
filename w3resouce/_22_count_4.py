def count_occurance(lst, niddle):

    count = 0
    for i in lst:
        if i == niddle:
            count = count + 1
    return count


print(count_occurance([1, 2, 3, 4, 5, 4,6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
