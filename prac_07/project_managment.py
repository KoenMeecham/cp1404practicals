"""
CP1402
project managment
estimated: 4 hours
actual: 3.75 hours
"""
import datetime
from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    """Main function to run the project management program."""
    projects = load_projects()

    menu = """Menu:
        L - Load projects
        S - Save projects
        D - Display projects
        F - Filter projects by date
        A - Add new project
        U - Update project
        Q - Quit"""
    print(menu)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()
    save_projects(projects)


def load_projects():
    """Load projects from file."""
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    print(projects)
    return projects

def save_projects(projects):
    """Save projects to file."""
    with open(FILENAME, "w") as out_file:
        out_file.write(f'Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n')
        for project in projects:
            out_file.write(f'{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n')

def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete Projects")
    for project in incomplete_projects:
        print(project)
    print("Complete Projects")
    for project in complete_projects:
        print(project)

def add_project(projects):
    """Add a project to the projects list"""
    name = input("Name: ")
    while name != "":
        date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
        start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        priority = input("Priority: ")
        cost = float(input("Cost: "))
        completion_percentage = input("Completion Percentage: ")
        add_project = Project(name, start_date, priority, cost, completion_percentage)
        projects.append(add_project)
        name = input("Name: ")
    return projects

def filter_projects(projects):
    """Sort and filter projects by date."""
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date_filter = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    date_filtered_project = [project for project in projects if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() >= date_filter]
    date_filtered_project.sort()
    print(f"Filtered Projects")
    for project in date_filtered_project:
        print(project)

def update_project(projects):
    """Update a project in the projects list, but only the completion and priotity"""
    project_name = input("Input the name of the project to update: ")
    for project in projects:
        if project_name == project.name:
            new_priority = int(input("Input the new priority: "))
            new_completion_percentage = int(input("Input the new completion percentage: "))
            project.update(new_priority, new_completion_percentage)

if __name__ == "__main__":
    main()