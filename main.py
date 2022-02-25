from cost_funtion import cost_function
from parse_data import parse_data, compute_skills, PATHS
from roll import *
from time import time


if __name__ == '__main__':
    start_time = time()
    dataset = "b"
    path = PATHS[dataset]

    contributors, projects = parse_data(path)
    print("skills:\n", compute_skills(contributors, projects))
    

    current_cost_function = cost_function

    trajectory = roll_project_list_project_possible(contributors, projects, current_cost_function)
    print("trajectory:\n", trajectory)
    with open(f"output_{dataset}.txt", "w") as f:
        f.write(trajectory)
    print(time() - start_time)
