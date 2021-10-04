total_points = {}
submissions = {}
data = input()

while not data == "exam finished":
    data = data.split("-")
    if "banned" not in data:
        username = data[0]
        language = data[1]
        points = int(data[2])
        if username not in total_points:
            total_points[username] = points
        else:
            if total_points[username] < points:
                total_points[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        username = data[0]
        total_points.pop(username)
    data = input()

print(total_points)
print(submissions)

print("Results:")
[print(f"{k} | {v}") for k, v in sorted(total_points.items(), key=lambda x: (-x[1], x[0]))]
print("Submissions:")
[print(f"{k} - {v}") for k, v in sorted(submissions.items(), key=lambda x: (-x[1], x[0]))]