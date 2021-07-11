command = input().split("-")
note = [""] * 10
while command[0] != "End":
    index = int(command[0])-1
    importance = command[1]
    note.pop(index)
    note.insert(index, importance)
    command = input().split("-")
note = [x for x in note if x != ""]
print(note)