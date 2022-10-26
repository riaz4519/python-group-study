# def create_histogram(array):
#     total = ""
#     for hist_num in array:
#         total += "@ "*hist_num + "\n"

#     return total


# print(create_histogram([8, 3, 10, 20]))

# def create_histogram(array_hist):
#     for hist_num in array_hist:
#         for _ in range(0, hist_num):
#             print("@", end=" ")
#         print()


# create_histogram([2, 4, 6, 5])


def create_histogram(array_hist):
    for hist in array_hist:
        for i in range(0, hist):
            print("@", end=" ")
        print()


create_histogram([2, 3, 5, 7, 9, 5, 15])
