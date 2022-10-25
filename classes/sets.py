
set1 = {"1",1,2,3,5,4,6,7,8,9,10,11,10,"a","b",(1,2),(1,2)}

list1 = [1,2,3,4,5,6,7,8]

set2 = set("hello")

list2 = ["h","e","l","p"]

list3 = ["hello","hi","hello"]


set3 = set(list1)

set4 = set(list2)

set5 = set(list3)

print(set5)


set_ad_value = {1,2,3}

set_ad_value.add(4)

print(set_ad_value)

set_ad_value.update([5,3,6],{9})

print(set_ad_value)


#removing

set_ad_value.remove(9)
print(set_ad_value)
set_ad_value.discard(3)

print(set_ad_value)

set_ad_value.discard(10)








