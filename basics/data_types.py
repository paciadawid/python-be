a_string = "test"
a_string2 = 'test'
selector_example = "//button[id='login']"
a_char = "t"
print(a_string[1])

a_int = 1  # no upper/lower limit, no double type
a_float = 1.0
digit_string = "1"
digit_int = int(digit_string)

a_bool = True

bool_test = []  # False -> 0, "", [], (), {}, None
if bool_test:  # if bool_0 == True
    print("This is true")
else:
    print("This is false")

a_list = [1, 1.0, "test", [1, 2]]
print(a_list[3][0])
a_list.pop(3)
a_list.append("new text")
a_list[0] = "edited element"
print(a_list)

a_tuple = (1, 1.0, "test", [1, 3])
# a_tuple[0] = 1 -> immutable

a_dict = {
    "key": "value",
    0: 0
}
print(a_dict[0])
a_dict["new_key"] = "new_value"
print(a_dict)

a_set = {1, 2, 3, 4, 1}  # not ordered, unique values
print(a_set)


pajton = {
    "animal": "cat",
    "weight": 4.5,
    "age": 3,
    "alive": True,
    "colors": ("white", "black", "grey"),
    "food": ["cat food", "everything"]
}
print(pajton)

print("My cat's age is {}".format(pajton["age"]))
print(f"My cat's age is {pajton['age']}")

