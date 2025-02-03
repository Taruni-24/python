# program to remove punctuations from a string
punctuations="'!@#$%^&*()_:;.,?"
str=input("Enter a string: ")
newstr=""
for c in str:
    if c not in punctuations:
        newstr+=c
print(newstr)