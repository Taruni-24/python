year=int(input("enter the year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("given year is leap year")
        else:
            print("not an leap year")
    else:
        print("leap year")
else:
    print("given year is not a leap year")