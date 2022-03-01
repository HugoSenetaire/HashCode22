import numpy as np

def get_best_project(projects_graphs, score_function):
    max_cost = -np.inf
    for project, _ in projects_graphs.groupby(level=0, axis=1):
        cost_tmp = score_function(project) 
        if cost_tmp > max_cost :
            max_cost = cost_tmp
            best_project = project
    
    return best_project 
