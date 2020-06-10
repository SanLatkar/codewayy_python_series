# Declaring variables
# Personal Details
first_name = "Sanket"
middle_name = "Santosh"
last_name = "Latkar"
marks_Atharvaveda = 78
marks_Rigveda = 97
marks_Yajurveda = 91
marks_Samveda = 96
marks_Vedant = 84

#College Deatails
college_name = "Yeshwantrao Chavan College of Engineering"
college_address = "Wanadongri,Nagpur,441110"

# Concatenation to get Full name of student
full_name = f"My Full Name is {first_name} {middle_name} {last_name}"       #For using this format type we need  python2.6 or more latest version than2.6
print(full_name)            # Print Full name

# Contactenation to get College name with address
college_name_with_address = college_name +',' + college_address         #This is basic method of concatenatio.But bit probematic when we need to concatenate many strings
print("I am from ",college_name_with_address)

# Printing Marks obtained in each subject

print("\nMarks Obtained in Each subject")
print("Atharvaveda\t",marks_Atharvaveda)
print("Rigveda\t",marks_Rigveda)
print("Yajurveda\t",marks_Yajurveda)
print("Samveda\t",marks_Samveda)
print("Vedant\t",marks_Vedant)

# Calculating total marks

Total_marks = marks_Atharvaveda + marks_Rigveda + marks_Yajurveda + marks_Samveda + marks_Vedant            #Adding marks of all subjects
print("Total marks =" , Total_marks)            # Printing Total Marks

# Calculating Percentage
Percentage = round((Total_marks/5),2)           #Rounding off the Percentage till 2 decimal point
Percentage = "{}%".format(Percentage)           # Using format() function to concatenate '%' sign with percentage
print("\nPercentage : ",Percentage)             # Printing Percentage
