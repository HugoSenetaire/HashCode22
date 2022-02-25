from list_all_contributors import get_all_combination_contributor, get_combination_contributor
import pandas as pd 
from scipy.optimize import linear_sum_assignment
from tqdm import tqdm

def project_possible_list(projects, persons_list):
    possible_projects=[]
    for project in projects:
        if is_project_possible(project, persons_list)[0]:
            possible_projects.append(project)
    return possible_projects

# def get_bipartite_graph(projects, persons_list):
    

def is_project_possible(project, persons_list):
    #TODO: compute this offline, list of skills of person then here just check for availability
    #TODO: some persons seem to be assigned to project out of their reach investigate why
    # is it an issue with learning ?
    dicos = []
    persons = []
    for person in persons_list:
        if person.available_in < 1:
            dico = {}
            for skill in person.skills:
                #TODO: optimize this
                for i,role in enumerate(project.roles):
                    if skill == role.skill_name and person.skills[skill]>=role.skill_level:
                        dico[i]=1
            dicos.append(dico)
            persons.append(person)
    data = pd.DataFrame(dicos, columns=[i for i in range(len(project.roles))]).fillna(0).to_numpy()
    if not len(data):
        return False, []
    row_ind, col_ind = linear_sum_assignment((-1)*data)
    assigned_persons = []
    for i in range(len(row_ind)):
        index = col_ind.tolist().index(i)
        assigned_persons.append(persons[row_ind[index]])
    max_couplage = data[row_ind, col_ind].sum()
    return max_couplage == len(project.roles), assigned_persons



# def project_possible_list(projects, persons_list):
#     remaining_projects = copy.deepcopy(projects)
#     available_projects = []
#     while len(remaining_projects)>0:

#         project = remaining_projects.pop()
#         output = get_combination_contributor(project.roles, [], persons_list, return_first= True)
#         if len(output)>0 :
#             available_projects.append(project)
#     return available_projects
