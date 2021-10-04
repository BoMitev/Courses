def age_assignment(*names, **ages):
    dict = {}
    for name in names:
        for k,v in ages.items():
            if k == name[0]:
                dict[name] = v
    return dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))