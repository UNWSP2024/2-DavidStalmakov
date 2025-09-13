def average_age():
    # Program that calculates the average age of five friends
    # David Stalmakov, 9/12/2025
    # Input the ages
    age1=float(input("Enter the age of friend 1"))
    age2=float(input("Enter the age of friend 2"))
    age3=float(input("Enter the age of friend 3"))
    age4=float(input("Enter the age of friend 4"))
    age5=float(input("Enter the age of friend 5"))
    #calculate the average age
    age_sum= age1 + age2 + age3 + age4 + age5
    age_average=age_sum/5
    print("Average Age: ", age_average)

