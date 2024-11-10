"""
CP1402
project managment
estimated: 4 hours
actual:
"""
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

    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        else:
            print("Invalid choice")
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
            out_file.write(f'{project.name}\t{project.start_date}\t{project.priority}\t{project.completion_percentage}\t{project.cost_estimate}\n')

def display_projects(projects):
    print(projects)

if __name__ == "__main__":
    main()