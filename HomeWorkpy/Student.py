#-----------------Created Class Name: Student---------------
# : צור מחלקה בשם סטודנט המכילה את המאפיינים הבאים
#ציון
#גיל
#סוכם ציונים סטטי
#סוכם גילאים סטטי
#סוכם מספר סטודנטים סטטי
class Student:
    age=0
    grade=0
    sumGrades=0 #Static property
    sumAges=0 #Static property
    sumStudents=0 #Static property
#---------------Functions-----------------    
# : פונקציות
#1.יש ליצור בנאי המקבל את הגיל והציון 
# ובנוסף להשמה למשתני הגיל והציון הוא סוכם אותם לתוך המשתנים הסטטיים
#2.פונקציה סטטית המחזירה את ממוצע הציונים
#3.פונקציה סטטית המחזירה את ממוצע הגילאים
    def __init__ (self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
        Student.sumAges+=age
        Student.sumGrades+=grade
        Student.sumStudents+=1
    #average grades
    def averageGrades(self):
        a=self.sumGrades/Student.sumStudents
        print("Average grades-> ",a)
    #Average Ages
    def averageAges(self):
        b=self.sumAges/Student.sumStudents
        print("Average ages-> ",b)
#---------------CODE Main------------------
# : בקוד הראשי
#1.צור ארבעה סטודנטים עם נתונים כרצונך
#הדפס את נתוני כל סטודנט ואת ממוצע הציונים וממוצע הגילאים2
student1= Student('Bob',20,85)
print("Bob:")
student1.averageGrades()
student1.averageAges()
print('\n')
student2= Student('Alice',25,90)
print("Alice:")
student2.averageGrades()
student2.averageAges()
print('\n')
student3= Student('Tom',23,75)
print("Tom:")
student3.averageGrades()
student1.averageAges()
print('\n')
student3= Student('Shadi',20,99.5)
print("Shadi:")
student3.averageGrades()
student3.averageAges()