def manage_courses():
    # Step 1: Create the dictionary with the initial courses
    courses = {
        "CSE101": {"Course name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"},
    }

    # Step 2: Update the instructor's name for CSE102
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."

    # Step 3: Add a new course CSE104
    courses["CSE104"] = {"Course name": "Algorithms", "Credits": 4, "Instructor": "Dr. Dave"}

    # Step 4: Remove the course CSE101
    courses.pop("CSE101")

    # Step 5: Loop through the dictionary and print the course details
    for course_code, details in courses.items():
        print(f"{course_code}: {details}")


# Call the function
manage_courses()