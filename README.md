
# 🎓 Student Record Management System (Python, OOP)

A simple command-line application to manage student records using Python's Object-Oriented Programming principles and file handling. Built as a personal learning project to strengthen OOP design, data persistence, and CLI interaction.

---

## 🚀 Features

- ✅ Add new student records  
- ✅ View all student entries  
- ✅ Search student by roll number  
- ✅ Update existing student data  
- ✅ Delete student by roll number  
- ✅ Persistent CSV-based data storage  
- ✅ Clean class-based design (Student + Manager)

---

## 🧠 Concepts Used

- Object-Oriented Programming  
- File I/O (CSV)  
- Encapsulation  
- Modular Code Structure  
- Basic CLI interaction

---

## 🗃 File Structure

```
student_record_system/
├── main.py                # CLI Menu logic
├── student.py             # Student class definition
├── student_manager.py     # Handles file operations & student management
├── students.csv           # Data file (created automatically)
└── README.md              # Project description
```

---

## 🧪 How to Run

1. Make sure Python 3.x is installed on your system
2. Clone this repository or download the files
3. Open a terminal and run:

```bash
python main.py
```

4. Follow the on-screen menu options

---

## 🔧 Example CLI Flow

```
====| Student Records System |====
1. Add Student
2. View All Students
3. Search Student via Roll Number
4. Update Student Record
5. Delete Student Record
6. Exit

Enter your choice(1-6): 1
Enter Student's Name: Riya
Enter Roll Number: 25IT102
...
✅ Student Added Successfully!
```

---

## 📌 Sample Entry Format (CSV)

Each student record is stored like this:

Name, Roll Number, Branch, Year, CGPA  
Riya, 25IT102, IT, 2, 9.2

---

## 💡 Future Enhancements (Ideas)

- Add input validation and error handling
- Sort students by CGPA or name
- Add GUI using Tkinter or Streamlit
- Convert to JSON-based storage
- Create REST API version (using Flask or FastAPI)

---

## 👨‍💻 Author

Hammad Khan  
Aspiring AI Engineer | BTech IT @ NSUT Delhi  
Project 2 of my AI Learning Roadmap
