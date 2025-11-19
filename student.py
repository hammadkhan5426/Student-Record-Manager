class Students:
    def __init__(self, name, rollno, branch, year, cgpa):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        # Ensure types are consistent
        try:
            self.year = int(year)
        except (ValueError, TypeError):
            self.year = year
        try:
            self.cgpa = float(cgpa)
        except (ValueError, TypeError):
            self.cgpa = cgpa

    def __str__(self):
        return f"Name: [bold]{self.name}[/bold]\nRoll Number: [bold]{self.rollno}[/bold]\nBranch: {self.branch}\nYear: {self.year}\nCGPA: {self.cgpa}"

    def to_csv(self):
        # store as simple strings so csv is consistent
        return [self.name, self.rollno, str(self.branch), str(self.year), str(self.cgpa)]
