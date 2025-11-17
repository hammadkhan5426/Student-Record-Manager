from student import Students
from student_manager import Manager

manager=Manager('students.csv')



while True: 
    print("====| Student Records System |===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student via Roll Number")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    
    ch=int(input("Enter your choice(1-6):"))
    if ch==1:
        name=input("Enter Student's Name:")
        rollno=input("Enter Student's Roll Number:")
        branch=input("Enter Branch:")
        year=int(input("Enter Year:"))
        cgpa=float(input("Enter CGPA:"))
        s= Students(name,rollno,branch,year,cgpa)
        manager.addStudent(s)
        print("Student Added Successfully!")


    elif ch==2:
        students=manager.viewAll()
        if not students:
            print("No students found")
        else:
            for s in students:
                print(s)

    elif ch==3:
        roll=input("Enter the Roll Number you want to search for:")
        result= manager.Search(roll)
        if result:
            print("|Student found|", result)
        else:
            print("Student not found")

    elif ch==4:
        roll=input("Enter the Roll Number you want to update:")
        result= manager.Search(roll)
        if result:
            print("Current:", result)
            newname=input("Enter Updated Name:")
            newbranch=input("Enter Updated Branch:")
            newyear=int(input("Enter Updated Year:"))
            newcgpa=float(input("Enter Updated CGPA:"))
            if manager.Update(roll, newname,newbranch,newyear,newcgpa):
                print("Record Updated Successfully.")
            else:
                print("Failed to Update.")
        else:
            print("Student not found.")

    elif ch==5:
        rollno=input("Enter the Roll Number you want to delete:")
        confirmation= input("Are you sure you want to remove this student (YES/NO):").lower()
        if confirmation== 'yes':
            if manager.Delete(rollno):
                print("Record Deleted Successfully.")
            else:
                print("Student not found.")
        else:
            print("Deletion Cancelled")

    elif ch==6:
        print("Exited Successfully")
        break
    else:
        print("Invalid choice!")
    

          