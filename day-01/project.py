def analyze(marks):
    total = sum(marks)
    avg = total / len(marks)
    
    if avg > 90:
        print("Excellent")
    elif avg>70:
        print("Normal")
    elif avg > 50:
        print("Needs improvement")
    else:
        print("Bad Result")
        
    
    for i in range(0,4):
        print(marks[i])
    
    print("Total :", total)
    print("Avg: ", round(avg, 2))
    

student_marks = [40, 80, 90, 100, 50]

analyze(student_marks)


//practice

def analyze(salaries):
    total = sum(salaries)
    avg = total / len(salaries)
    
    if avg > 90000:
        print("High Income")
    elif avg > 70000:
        print("Good Income")
    elif avg > 50000:
        print("Average Income")
    else:
        print("Low Income")
        
    for i in range(0, 4):
        print(salaries[i])
    
    print("Total :", total)
    print("Avg: ", round(avg, 2))
    

employee_salaries = [40000, 65000, 80000, 95000, 50000]

analyze(employee_salaries)
