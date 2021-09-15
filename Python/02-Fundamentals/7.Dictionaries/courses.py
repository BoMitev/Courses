command = input()
courses = {}

while command != "end":
    course_name, student = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student)
    command = input()

for k,v in sorted(courses.items(), key= lambda x: -len(x[1])):
    print(f"{k}: {len(v)}")
    for i in sorted(v):
        print(f"-- {i}")