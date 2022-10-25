# first input the comma separated number
# split them by commma
# if splited we got the list
# then from that list make it a tuple

string = input("insert number seprated by comma : ")
separate_by_comma = string.split(",")
tuple_list = tuple(separate_by_comma)

print("List :", separate_by_comma)
print("Tuple :", tuple_list)
