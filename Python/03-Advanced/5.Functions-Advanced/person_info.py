def get_info(**dict):
    return f"This is {dict.get('name')} from {dict.get('town')} and he is {dict.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))