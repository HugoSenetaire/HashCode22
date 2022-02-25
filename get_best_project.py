import numpy as np

def get_best_project(dispo_projects, cost_function):
    min_cost = np.inf
    min_ind=0
    for i,project in enumerate(dispo_projects) :
        cost_tmp = cost_function(project) 
        if cost_tmp < min_cost :
            min_ind=i
            min_cost = cost_tmp
            best_project = project 
    return min_ind,best_project 
