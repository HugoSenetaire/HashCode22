from score_funtion import score_function, score_function_per_day_and_nb_roles
from parse_data import parse_data, compute_skills, PATHS
from roll import *
from time import time


if __name__ == '__main__':
    start_time = time()
    dataset = "e"
    path = PATHS[dataset]

    contributors, projects = parse_data(path)

    current_score_function = score_function_per_day_and_nb_roles

    trajectory = roll_project_list_project_possible(contributors, projects, current_score_function)
    print("trajectory:\n", trajectory)
    with open(f"output_{dataset}.txt", "w") as f:
        f.write(trajectory)
    print(time() - start_time)
