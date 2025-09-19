equalssighn = "=" 
space = " "
student = "Student: Antwain Powell | Email: abpowell2@aggies.ncat.edu"
ffrom = ("From: Clayton, NC | Graduating: Spring 2029")
major = ("Major: Computer Science")
currentcourses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses_list = ["Biology", "chemistry", "calculus", "Spanish II", "World History"] 
currentcredits_list = [3, 3, 3, 3]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]
currentprofesor_list = ["Prof. Rhodes", "Dr. Lee", "Dr. Martinez", "Dr. Brown"]
currentclasslocation_list = ["M-Eric 300", "Marteena 201", "Crosby 121", "Crosby 210"]
curent_skill_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"} 
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interest_set = {"Software development", "Web development", "Data science", "Game development"}
Hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "incarceration", "Memento"}
course_credits_dictionary = {
    "COMP 163": 3,
    "MATH 150": 3, 
    "ENG 101": 3, 
    "HIS 105": 3 
}
course_professor_dictionary = {
    "COMP 163": "Prof. Rhodes", 
    "MATH 150": "Dr. Lee", 
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr.Brown"
}
course_room_dictionary = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}
monthly_budget_dictionary = {
    "Food":450, 
    "Entertainment": 200, 
    "Books": 125, 
    "Transportation": 100
}
studyhours_perclass_dictionary = {
    "Programming": 10, 
    "Math": 8, 
    "English": 4, 
    "History": 3
}
contact_dictionary = {
    "Mom": 7045550199, 
    "Roommate": 3365557821, 
    "Academic Advisor": 3363345000
}
emergencycontact_tuple = (
    "Hannah Smith", 
    "(Mom)",
    "704-555-0199"
)
homeadress_tuple = (
    "456 Oak Street",
    "Charlotte",
    "NC",
    28202
)
instagraminfo_tuple = (
    "Instagram",
    "@jordan_codes",
    312
)
twitterinfo_tuple = (
    "Twitter",
    "@Jordandev",
    127
)
birthday_tuple = (
    "Birthday",
    "5",
    "22",
    "2006"
)
print(f"{equalssighn*64}")
print(space*13, "PERSONAL ACADEMIC & LIFE PORTFOLIO")
print(f"{equalssighn*64}")
print(student)
print(ffrom)
print(f"{major}\n")
print(f"{equalssighn*3} ACADEMIC PROFILE {equalssighn*3}")
print(f"Current Semester: {sum(course_credits_dictionary.values())} credits across {len(course_credits_dictionary)} courses")
print(f"Cumulative GPA: {sum(gpa_history_list) / 4:.2f}")
print(f"Weekly Study Time: {sum(studyhours_perclass_dictionary.values())} hours")
print(f"Academic Investment: ${monthly_budget_dictionary["Books"] // sum(studyhours_perclass_dictionary.values()):.1f} per study hour\n")
print("Current Courses:")
print(f"{currentcourses_list[0]} - {currentcredits_list[0]} credits - {currentprofesor_list[0]} - {currentclasslocation_list[0]}")
print(f"{currentcourses_list[1]} - {currentcredits_list[1]} credits - {currentprofesor_list[1]} - {currentclasslocation_list[1]}")
print(f"{currentcourses_list[2]} - {currentcredits_list[2]} credits - {currentprofesor_list[2]} - {currentclasslocation_list[2]}")
print(f"{currentcourses_list[3]} - {currentcredits_list[3]} credits - {currentprofesor_list[3]} - {currentclasslocation_list[3]}\n")
print(f"{equalssighn*3} PERSONAL DEVELOPMENT {equalssighn*3}")  
print(f"Current Skills: {curent_skill_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interest_set}")
print(f"Skills Currently Have: {len(curent_skill_set)}") 
print(f"Skills Want to Learn: {len(skills_to_learn_set)}\n")
print(f"{equalssighn*3} FINANCIAL OVERVIEW {equalssighn*3}")
print(f"Monthly Budget: ${sum(monthly_budget_dictionary.values())}") 
print(f"Food: ${monthly_budget_dictionary["Food"]} (${monthly_budget_dictionary["Food"]/30:.1f}/day)") 
print(f"Entertainment: ${monthly_budget_dictionary["Entertainment"]}")
print(f"Books: ${monthly_budget_dictionary["Books"]}")
print(f"Transportation: ${monthly_budget_dictionary["Transportation"]}") 
print(f"Annual Projection: ${sum(monthly_budget_dictionary.values()) * 12}\n")
print(f"{equalssighn*3} CONNECTIONS & CONTACTS {equalssighn*3}")
print(f"Emergency Contact: {emergencycontact_tuple[0]} {emergencycontact_tuple[1]} - {emergencycontact_tuple[2]}")
print(f"Home Address: {homeadress_tuple[0]}, {homeadress_tuple[1]}, {homeadress_tuple[2]} {homeadress_tuple[3]}")
print(f"Social Media Presence: {twitterinfo_tuple[2] + instagraminfo_tuple[2]} followers across 2 platforms")
print(f"Key Contacts: {len(contact_dictionary)} people in directory\n")
print(f"{equalssighn*3} LIFE STATISTICS {equalssighn*3}")
print(f"Total Courses Completed: {len(completed_courses_list)}")
print(f"Current Academic Load: {sum(studyhours_perclass_dictionary.values()) + sum(currentcredits_list)} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog_set)} items")
print(f"Current Hobbies: {len(Hobbies_set)} activities")
print(f"{equalssighn*64}") 
