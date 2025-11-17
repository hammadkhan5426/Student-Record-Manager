class Students:
    def __init__(self,name,rollno,branch,year,cgpa):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.year=year
        self.cgpa=cgpa
    
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.rollno}, Branch:{self.branch}, year:{self.year}, CGPA: {self.cgpa}"

    def to_csv(self):
        return [self.name,self.rollno,self.branch,self.year,self.cgpa]
    
    
