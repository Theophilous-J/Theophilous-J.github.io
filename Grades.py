#This Code will average out your last five test scores!
#Good Luck!!!
#User input

def main():
    test1 = int(input("Enter score 1: "))
    test2 = int(input("Enter score 2: "))
    test3 = int(input("Enter score 3: "))
    test4 = int(input("Enter score 4: "))
    test5 = int(input("Enter score 5: "))

#Test Averaging
    
    average_grade = calc_average(test1, test2, test3, test4, test5)
    
    letter1 = determine_grade(test1)
    print(test1,"     ",letter1)
    
    letter2= determine_grade(test2)
    print(test2,"     ",letter2)
    
    letter3= determine_grade(test3)
    print(test3,"     ",letter3)
    
    letter4= determine_grade(test4)
    print(test4,"     ",letter4)
    
    letter5= determine_grade(test5)
    print(test5,"     ",letter5)

def calc_average(test1, test2, test3, test4, test5):
    SUM = test1 + test2 + test3 + test4 + test5
    mean = SUM / 5
    print(mean)
            

def determine_grade(test1):
    if test1 >=90:
        return "A"
    elif test1 >=80:
        return "B"
    elif test1 >=70:
        return "C"
    elif test1 >=60:
        return "D"
    else:
        return "F"
    



main()
