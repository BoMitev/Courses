data = input()
courses = {}

while ":" in data:
    name, id, course = data.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][id] = name
    data = input()
else:
    data = data.replace("_", " ")
    for course in courses:
        if course == data:
            for id, name in courses[course].items():
                print(f"{name} - {id}")