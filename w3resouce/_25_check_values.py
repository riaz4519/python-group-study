from optparse import check_choice


def check_values(group, value):

    for i in group:
        if value == i:
            return True
    return False

    # return value in group


print(check_values([1, 5, 8, 3], 3))
print(check_values([1, 5, 8, 3], -1))
