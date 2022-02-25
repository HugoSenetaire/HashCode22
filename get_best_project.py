import numpy as np

def get_best_project(dispo_projects, cost_function):
    min_cost = np.inf
    for i,project in enumerate(dispo_projects) :
        cost_tmp = cost_function(project) 
        if cost_tmp < min_cost : 
            min_cost = cost_tmp
            best_project = project 
    return i,best_project 
