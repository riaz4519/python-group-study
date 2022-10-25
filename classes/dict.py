dict1 = {
    "shanto" : "is a name of a person",
    "shanto" : "is also a another persons name",
    1 : "the number one",
    "list" : [1,2,4,"list"],
    "dict2" : {
        "shanto" : "is a name of a person",
        "riaz" : "is also a"
    }
}

dict2 = dict1['dict2']


print(dict2['shanto'])
print(dict1["dict2"]['shanto'])

#adding new value to the existing dict
dict1["new_value"] = "this is a new value";
print(dict1)

#adding new key value with update function 
dict1.update({"update" : "updating dict with key value","shanto" :"this is update 1"})
print(dict1)

#change 

dict1["new_value"] = "bla bla"
print(dict1)




