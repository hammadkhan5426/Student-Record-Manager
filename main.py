from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from student import Students
from student_manager import Manager

console = Console()
manager = Manager("students.csv")

def header():
    console.clear()
    console.print(Panel.fit("[bold cyan]Student Records System[/bold cyan]\n[green]Manage student records quickly and beautifully[/green]",
                            border_style="bright_magenta"))

def menu():
    console.print("\n[bold yellow]Menu[/bold yellow]")
    console.print("[cyan]1.[/cyan] Add Student")
    console.print("[cyan]2.[/cyan] View All Students")
    console.print("[cyan]3.[/cyan] Search Student via Roll Number")
    console.print("[cyan]4.[/cyan] Update Student Record")
    console.print("[cyan]5.[/cyan] Delete Student Record")
    console.print("[cyan]6.[/cyan] Exit")

def add_student():
    console.print("\n[bold green]Add a new student[/bold green]")
    name = Prompt.ask("Student's Name").strip()
    rollno = Prompt.ask("Roll Number").strip()
    branch = Prompt.ask("Branch").strip()
    # validated year
    while True:
        year_str = Prompt.ask("Year (integer)")
        try:
            year = int(year_str)
            break
        except ValueError:
            console.print("[red]Please enter a valid integer for year.[/red]")
    # validated cgpa
    while True:
        cgpa_str = Prompt.ask("CGPA (e.g. 8.5)")
        try:
            cgpa = float(cgpa_str)
            break
        except ValueError:
            console.print("[red]Please enter a valid number for CGPA.[/red]")

    s = Students(name, rollno, branch, year, cgpa)
    manager.addStudent(s)
    console.print(Panel("[bold green]Student added successfully![/bold green]", border_style="green"))

def view_all():
    students = manager.viewAll()
    if not students:
        console.print(Panel("[bold yellow]No students found.[/bold yellow]", border_style="yellow"))
        return

    table = Table(title="All Students", show_lines=True, header_style="bold magenta")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Roll No", style="bold")
    table.add_column("Branch")
    table.add_column("Year", justify="center")
    table.add_column("CGPA", justify="center")

    for s in students:
        table.add_row(s.name, s.rollno, s.branch, str(s.year), str(s.cgpa))

    console.print(table)

def search_student():
    roll = Prompt.ask("Enter Roll Number to search").strip()
    result = manager.Search(roll)
    if result:
        console.print(Panel(f"[bold green]Student found[/bold green]\n\n{result}", border_style="green"))
    else:
        console.print(Panel("[bold red]Student not found[/bold red]", border_style="red"))

def update_student():
    roll = Prompt.ask("Enter Roll Number to update").strip()
    result = manager.Search(roll)
    if not result:
        console.print(Panel("[bold red]Student not found[/bold red]", border_style="red"))
        return
    console.print(Panel(f"[bold blue]Current:[/bold blue]\n{result}", border_style="blue"))
    newname = Prompt.ask("Updated Name", default=result.name).strip()
    newbranch = Prompt.ask("Updated Branch", default=result.branch).strip()

    # year
    while True:
        newyear_str = Prompt.ask("Updated Year", default=str(result.year))
        try:
            newyear = int(newyear_str)
            break
        except ValueError:
            console.print("[red]Year must be integer.[/red]")

    # cgpa
    while True:
        newcgpa_str = Prompt.ask("Updated CGPA", default=str(result.cgpa))
        try:
            newcgpa = float(newcgpa_str)
            break
        except ValueError:
            console.print("[red]CGPA must be numeric.[/red]")

    ok = manager.Update(roll, newname, newbranch, newyear, newcgpa)
    if ok:
        console.print(Panel("[bold green]Record updated successfully.[/bold green]", border_style="green"))
    else:
        console.print(Panel("[bold red]Failed to update record.[/bold red]", border_style="red"))

def delete_student():
    roll = Prompt.ask("Enter Roll Number to delete").strip()
    confirm = Confirm.ask(f"[red]Are you sure you want to delete roll {roll}?[/red]")
    if not confirm:
        console.print(Panel("[yellow]Deletion cancelled.[/yellow]", border_style="yellow"))
        return
    ok = manager.Delete(roll)
    if ok:
        console.print(Panel("[bold green]Record deleted successfully.[/bold green]", border_style="green"))
    else:
        console.print(Panel("[bold red]Student not found.[/bold red]", border_style="red"))

def main():
    while True:
        header()
        menu()
        try:
            choice = int(Prompt.ask("\nEnter your choice (1-6)"))
        except ValueError:
            console.print("[red]Please enter a number between 1 and 6.[/red]")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_all()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            console.print(Panel("[bold cyan]Goodbye![/bold cyan]", border_style="cyan"))
            break
        else:
            console.print("[red]Invalid choice.[/red]")

        console.print("\nPress Enter to continue...", style="dim")
        input()

if __name__ == "__main__":
    main()
