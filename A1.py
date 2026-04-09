#write a python program to input student name and marks of three subjects.print name and percentage into output

name = input( "write your name:" )
marks_1 = input ("write your marks in English: ")
marks_2 = input ("write your marks in Computer: ")
marks_3 = input ("write your marks in Math: ")
percentage =  (int(marks_1) + int(marks_2) + int(marks_3))*100/300
print (f"The result of {name} is {int(percentage)}%. Welldone ")