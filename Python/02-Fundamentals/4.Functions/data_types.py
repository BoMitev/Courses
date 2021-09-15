def data_types(type: str, input: str):
    if type == "int":
        print(int(input)*2)
    elif type == "real":
        real = int(input) * 1.5
        print(f"{real:.2f}")
    elif type == "string":
        print(f"${input}$")

data_type = input()
string = input()

data_types(data_type, string)