def mark_attendance(name, present):
    if present == True:
        return "Marked Present"
    if present == False:
        print("Student is absent")

def main():
    name = str(input("Enter the student name: "))
    presents = input("Enter True if present if not then False: ").capitalize()
    if presents == "True":
        present = presents
    attendance = mark_attendance(name, present)
    if attendance == "Marked Present":
        print("Attendance saved")
    else:
        print("Attendance not saved")


main()