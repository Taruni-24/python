marks={"abc":91,"def":78,"ghi":56,"jkl":34}
s_grades={}
for i in marks:
    mark=marks[i]
    if mark>90:
        s_grades[i]="A"
    elif mark>70:
        s_grades[i]="B"
    elif mark>50:
        s_grades[i]="C"
    else:
        s_grades[i]
print(s_grades)