class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average_marks(self):
        return sum(self.marks) / len(self.marks)

def get_top_performer(students):
    top_student = None
    highest_avg = -1
    
    for student in students:
        avg = student.average_marks()
        if avg > highest_avg:
            highest_avg = avg
            top_student = student.name
    
    return top_student

def main():
    
    students_data = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    
    
    students = [Student(name, marks) for name, marks in students_data.items()]
    
    avg_marks = {student.name: round(student.average_marks(), 2) for student in students}
    
    
    top_performer = get_top_performer(students)
    

    print(f"Average Marks: {avg_marks}")
    print(f"Top Performer: {top_performer}")


main()
