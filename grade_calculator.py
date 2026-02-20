def grade_info(score):
     #allocating grades along with encouraging message
     if score >=90 and score <=100:
         return "A" , "Outstanding "
     elif score >=80 and score <=89:
         return "B" , "Amazing work"
     elif score >=70 and score <=79:
         return "C" , "keep it up "
     elif score >=60 and score <=69:
          return "D" , "Good work"
     else :
         return "F","Fail"

while True:
     try:
        #inputs  
        name=input("Enter the Name of the Student :")  
        marks=int(input("Enter your Marks(0-100) : " ))
        #to check the valid input of Marks entered
        if marks < 0 or  marks > 100:
            print("Invalid Input")
            continue
        #disaplying Result the Student
        grade , message = grade_info(marks)
        print(f"Result for {name} :")
        print(f" Marks : {marks} ")
        print(f" Grade : {grade}")
        print(f" Message : {message}")
        break

        #Chceking for any ValueError
     except ValueError:
        print("its not a number , Enter valid Digit ")
