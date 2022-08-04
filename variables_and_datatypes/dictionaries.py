print("-----------DICTIONARIES-----------")
# Unordered mappings of key value pairs

dictionary = {"key1": "value1", "key2": "value2"}
print(dictionary["key1"])

# All keys must be strings, values can be all data types
d = {
    "k1": 123,
    "k2": ["a", "b", "c"],
    "k3": {"anotherKey": 456},
    "k4": True
}
# Adding and selecting values
d["k5"] = 789
d["k1"] = "123"
print(d)
# print(d['k7']) Not an existing key, it will throw an error

# Methods
print("---Methods---")
d_keys = d.keys()
d_values = d.values()
d_items = d.items()
print(d_keys)
print(d_values)
print(d_items)
