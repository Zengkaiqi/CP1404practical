from prac_07.project import Project

FILE_NAME = "projects.txt"
COMPLETED_INDEX = 100
def main():
    incomplete_projects = []
    complete_projects = []
    projects,num_project = read_file(FILE_NAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {num_project} projects from {FILE_NAME}")
    user_choice = display_menu()
    while user_choice != "q":
        if user_choice == "l":
            projects, num_project = read_file(FILE_NAME)
        elif user_choice == "s":
            load_project(projects)
        elif user_choice == "d":
            incomplete_projects,complete_projects = display_project(projects)
        elif user_choice == "f":
            filter_date = input("Show projects that start after date (dd/mm/yy):")
            filter_project(incomplete_projects,filter_date)
            filter_project(complete_projects,filter_date)

        elif user_choice == "a":
            print("add a new project")
            project_name = get_valid_data("Project Name: ",str)
            project_start_date = get_valid_data("Project Start Date: ",str)
            project_priority = get_valid_data("Project Priority: ",int)
            project_cost = get_valid_data("Project Estimate: ",float)
            project_completion = get_valid_data("Project Completion: ",float)
            new_project = [project_name, project_start_date, project_priority, project_cost, project_completion]
            projects.append(new_project)
            if project_completion == 100:
                complete_projects.append(Project(project_name,project_start_date,project_priority,project_cost,project_completion))
            else:
                incomplete_projects.append(Project(project_name,project_start_date,project_priority,project_cost,project_completion))

        elif user_choice == "u":
            if len(incomplete_projects) == 0:
                print("No projects to display")
            else:
                for i in range(len(incomplete_projects)):
                    print(i,incomplete_projects[i])
                project_choice = int(input("Project choice: "))
                print(incomplete_projects[project_choice])
                new_complete_rate = int(input("New percentage: "))
                incomplete_projects[project_choice].get_new_completion(new_complete_rate)
                project_index = incomplete_projects.index(incomplete_projects[project_choice])
                projects[project_index][-1] = new_complete_rate
        else:
            print("Invalid input")
        user_choice = display_menu()
    load_index = input("Would you like to save to projects.txt?(y/n)").lower()
    if load_index == "y":
        load_project(projects)
    print("Thank you")


def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    choice = input(">>> ").lower()
    return choice

def read_file(file_name):
    file_details = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        file_contents = in_file.read()
    for line in file_contents.split("\n"):
        file_details.append(line.split("\t"))
    if [""] in file_details:
        file_details.remove([""])
    return file_details,len(file_details)

def display_project(projects):
    incomplete_objects = []
    complete_objects = []
    incomplete_projects = [project for project in projects if int(project[-1]) != COMPLETED_INDEX]
    completed_projects = [project for project in projects if int(project[-1]) == COMPLETED_INDEX]
    print("Incomplete project:")
    for project in incomplete_projects:
        new_project = Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4]))
        incomplete_objects.append(new_project)
        print("\t",new_project)
    print("Completed project:")
    for project in completed_projects:
        new_project = Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4]))
        complete_objects.append(new_project)
        print("\t",new_project)
    return incomplete_objects,complete_objects

def filter_project(projects,filter_date):
    for project in projects:
        if project.date_filter(filter_date):
            print(project)

def get_valid_data(prompt,types):
    while True:
        try:
            user_input = types(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input")


def load_project(projects):
    with open(FILE_NAME, "w") as out_file:
        out_file.writelines("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project[0]}\t{project[1]}\t{project[2]}\t{project[3]}\t{project[4]}\n")


main()