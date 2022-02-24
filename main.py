from cost_funtion import cost_function
from parse_data import parse_data, compute_skills, PATHS
from roll import *


if __name__ == 'main':
    dataset = "a"
    path = PATHS[dataset]

    contributors, projects = parse_data(path)
    print("skills:\n", compute_skills(contributors, projects))


    current_cost_function = cost_function

    trajectory = roll_project_list_project_possible(contributors, projects, current_cost_function, max_iter = 1e5)

    with open(f"output_{dataset}.txt", "w") as f:
        f.write(trajectory)