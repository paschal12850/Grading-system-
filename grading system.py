def grade_student(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

# Example usage:
score = int(input("Enter student's score: "))
grade = grade_student(score)
print(f"Grade: {grade}")
