import copy
import tqdm
from list_all_contributors import get_all_combination_contributor, get_combination_contributor
# def project_possible_list(projects, persons_list):
#     remaining_projects = copy.deepcopy(projects)
#     available_projects = remaining_projects
#     for project in remaining_projects:
#         available_persons = persons_list
#         feasible_project = False 
#         for role in project.roles :
#             feasible_role = False
#             for person in persons_list : 
#                 if person.available_in < 1 :
#                     for skill in person.skills.keys() : 
#                         if skill == role : 
#                             feasible_role = True 
#                             available_persons.remove(person)
#                             break
#                     if feasible_role : 
#                         break
#             if not feasible_role : 
#                 available_projects.remove(project)
#                 break
#     return available_projects


def project_possible_list(projects, persons_list):
    remaining_projects = copy.deepcopy(projects)
    available_projects = []
    while len(remaining_projects)>0:

        project = remaining_projects.pop()
        output = get_combination_contributor(project.roles, [], persons_list, return_first= True)
        if len(output)>0 :
            available_projects.append(project)
    return available_projects
