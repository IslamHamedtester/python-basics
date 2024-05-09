my_dict = {"first_name" : "islam", "age" : 31, "title" : "software_tester"}
print(my_dict)

print(f"{my_dict['first_name']} is {my_dict['age']} years old")

my_dict["language"] = "pyhon"
print(my_dict)

my_dict["language"] = "java"
print(my_dict)

del my_dict["language"]
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
