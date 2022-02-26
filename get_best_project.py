import numpy as np

def get_best_project(dispo_projects, score_function):
    max_cost = -np.inf
    max_ind=0
    for i,project in enumerate(dispo_projects) :
        cost_tmp = score_function(project) 
        if cost_tmp > max_cost :
            max_ind=i
            max_cost = cost_tmp
            best_project = project 
    return max_ind,best_project 
