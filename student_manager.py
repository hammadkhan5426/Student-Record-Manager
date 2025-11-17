from student import Students
import csv 
import os

class Manager:
    def __init__(self,filename):
        self.filename=filename

    def addStudent(self,student):
        with open(self.filename,"a",newline='') as file:
            writer=csv.writer(file)
            writer.writerow(student.to_csv())
            
    def viewAll(self):
        students=[]
        try:
            with open(self.filename, 'r',newline='') as file:
                reader=csv.reader(file)
                for line in reader:
                    if len(line)==5:
                        student=Students(line[0],line[1],line[2],line[3],line[4])
                        students.append(student)
        except FileNotFoundError:
            pass
        return students
    
    def Search(self,rollno):
        with open(self.filename, "r") as f:
            reader=csv.reader(f)
            for row in reader:
                if len(row)==5 and row[1]==rollno:
                    return Students(row[0],row[1],row[2],row[3],row[4])
    
    def Update(self,rollno,newname,newbranch,newgrade,newyear):
        updated= False
        students=[]
        with open(self.filename,'r',newline='') as f:
            reader=csv.reader(f)
            for row in reader:
                if len(row)==5 and row[1]==rollno:
                    students.append([newname,rollno,newbranch,newgrade,newyear])
                    updated=True
                else:
                    students.append(row)
        with open(self.filename,'w',newline='') as f:
            writer=csv.writer(f)
            writer.writerows(students)

        return updated
    def Delete(self,rollno):
        deleted= False
        students=[]

        try:
            with open(self.filename,'r',newline='') as f:
                reader=csv.reader(f)
                for row in reader:
                    if len(row)==5:
                        if row[1]==rollno:
                            deleted= True
                        else:
                            students.append(row)
        except FileNotFoundError:
            return False
        with open(self.filename,'w',newline='') as f:
            writer=csv.writer(f)
            writer.writerows(students)

        return deleted
     







    
    
