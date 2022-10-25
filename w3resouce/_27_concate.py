# def concate(elements):
#     return "".join(list(map(str, elements)))


# print(concate([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def concate(elemetns):
    result = ""
    for element in elemetns:
        result += str(element)
    return result


print(concate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
