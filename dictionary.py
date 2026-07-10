print("Q1_Student Profile System:")
Student = {
     "Name" : "Yumna Maryam",
     "Age" : 18,
     "City" : "Karachi",
     "Hobbies":["Reading","Cooking","Coding"],
     "Skills":["Driving","Designing","Typing"]
}
print("Student Name:",Student["Name"])
print("First Hobby:",Student["Hobbies"][0])
print("Skills:",Student["Skills"])

print("Q2_Students Marks System:")
Student = {
     "Name" : "Yumna Maryam",
     "Age" : 18,
     "City" : "Karachi",
     "Hobbies":["Reading","Cooking","Coding"],
     "Skills":["Driving","Designing","Typing"],
     "Marks" : {
         "Math" : 85,
         "Science" : 80,
         "English" : 88,
         "Computer" : 85
     }
}
print("All Subject Marks:",Student["Marks"])
TotalMarks = Student["Marks"]["Math"] + Student["Marks"]["Science"] + Student["Marks"]["English"] + Student["Marks"]["Computer"]
print("Total Marks:", TotalMarks)
AverageMarks = TotalMarks / len(Student["Marks"])
print("Average Marks:", AverageMarks)

print("Q3_Grade Checking System:")
if(AverageMarks >= 80):
    Grade = "Grade: A"
elif(AverageMarks >= 70):
    Grade = "Grade: B"
elif(AverageMarks >= 60):
    Grade = "Grade: C"
else:
    Grade = "Fail"
print("Final Result:", Grade)

if(AverageMarks >= 60):
    Status = "Pass"
else:
    Status = "Fail"
print("Status:", Status)

print("Q4_Attendance Management System:")
Attendance = {
    "Total Classes" : 100,
    "Present Classes" : 80
}
AttendancePercentage = (Attendance["Present Classes"] / Attendance["Total Classes"]) * 100
print("Attendance Percentage:", AttendancePercentage)

if(AttendancePercentage < 75):
    print("Short Attendance")
else:
    print("Eligible For Exam")

print("Q5_Fee Management System:")
Student["Fees Paid"] = True

if(Student["Fees Paid"]):
    print("Fees Cleared")
else:
    print("Fees Pending")

print("Q6_Skills Management System:")
Student["Skills"].append("Programming")
Student["Skills"].remove("Typing")
print("Updated Skills:", Student["Skills"])
print("Total Skills:", len(Student["Skills"]))

print("Q7_Login Authentication System:")
User = {
    "Username" : "YumnaMaryam",
    "Password" : "Yumna@123"
}
if(User["Username"] == "YumnaMaryam" and User["Password"] == "Yumna@123"):
    print("Login Successful")
else:
    print("Invalid Credentials")

print("Q8_Address Management System:")
Student = {
    "Name" : "Yumna Maryam",
    "Age" : 18,
    "Address" : {
        "Area" : "Gulshan-e-Iqbal",
        "Street" : "123 Main Street",
        "House Number" : "456"
    }
}
print("Address:", Student["Address"])
UpdateArea = "Clifton"
Student["Address"]["Area"] = UpdateArea
print("Updated Address:", Student["Address"])
ZipCode = "12345"
Student["Address"]["Zip Code"] = ZipCode
print("Zip Code:", Student["Address"])

print("Q9_Multiple Students Database:")
Students = {
    "Student1" : {
        "Name" : "Yumna Maryam",
        "Age": 18,
        "City":"Karachi",
        "Marks":449
    },
    "Student2" : {
        "Name":"Hadia Aiman",
        "Age": 17,
        "City":"Lahore",
        "Marks":378
    }
}
print("Student1 Name:",Students["Student1"]["Name"])
print("Student2 Name:",Students["Student2"]["Marks"])
UpdateCity = "Islamabad"
UpdateCity = Students["Student1"]["City"] 
print("Student1 City:", UpdateCity)

print("Q10_Final Student Report Card System:")
Student = {
    "Profile": {
        "Name" : input("Enter Your Name: "),
        "Age" : int(input("Enter Your Age: ")),
        "Class" : input("Enter Your City: "),
        "Roll Number" : input("Enter Your Roll Number:"),
        "Hobbies":["Reading","Cooking","Coding"],
        "Skills":["Driving","Designing","Typing"]
    },
    "Marks": {
        "Math" : int(input("Enter Math Marks: ")),
        "Science" : int(input("Enter Science Marks: ")),
        "English" : int(input("Enter English Marks: ")),
        "Computer" : int(input("Enter Computer Marks: "))
    },
    "Attendance": {
        "Total Classes" : int(input("Enter Total Classes: ")),
          "Present Classes" : int(input("Enter Present Classes: "))
     },
     "Fees Paid" : input("Have You Paid Your Fees? (Yes/No): ").lower(),
     "Address": {
         "Area" : input("Enter Your Area: "),
         "Street" : input("Enter Your Street: "),
         "House Number" : input("Enter Your House Number: "),
         "Zip Code" : input("Enter Your Zip Code: ")
     }, 
}
TotalMarks = sum(Student["Marks"].values())
AverageMarks = TotalMarks / len(Student["Marks"])

if(AverageMarks >= 80):
    Grade = "Grade: A"
elif(AverageMarks >= 70):
    Grade = "Grade: B"
elif(AverageMarks >= 60):
    Grade = "Grade: C"
else:
    Grade = "Fail"

AttendancePercentage = (Student["Attendance"]["Present Classes"] / Student["Attendance"]["Total Classes"]) * 100

print("__________ REPORT CARD __________")
print("_____ PROFILE:_____")
print("Name:", Student["Profile"]["Name"])
print("Age:", Student["Profile"]["Age"])
print("Class:", Student["Profile"]["Class"])
print("Roll Number:", Student["Profile"]["Roll Number"])


print("_____ MARKS:_____")
for subject, marks in Student["Marks"].items():
    print(f"{subject}: {marks}")

print("Total Marks:", TotalMarks)
print("Average Marks:", AverageMarks)
print("Final Result:", Grade)

if(AverageMarks >= 60):
    Status = "Pass"
else:
    Status = "Fail"

print("Attendance Percentage:", AttendancePercentage)

if (AttendancePercentage >= 75):
    print("Exam Status: Eligible For Exam")
else:
    print("Exam Status: Not Eligible For Exam Because Attendance is Less Than 75")

if(Student["Fees Paid"] == "yes"):
    print("Fees Status: Fees Cleared")
else:
    print("Fees Status: Fees Pending")

print("Hobbies:", ", ".Student["Profile"]["Hobbies"])
print("Skills:", ", ".Student["Profile"]["Skills"])

print("_____ ADDRESS:_____")
print("Area:",Student["Address"]["Area"])
print("Street:",Student["Address"]["Street"])
print("House Number:",Student["Address"]["House Number"])
print("Zip Code:",Student["Address"]["Zip Code"])