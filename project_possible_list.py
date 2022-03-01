import pandas as pd 
from scipy.optimize import linear_sum_assignment
from tqdm import tqdm

def remove_impossible_projects_graphs(projects_graphs):
    impossible_projects = []
    # TODO: There must be a better way to iterate over projects, but this should work 
    for project, graph in projects_graphs.groupby(level=0, axis=1):
        if not is_project_possible(graph)[0]:
            impossible_projects.append(project)
    
    projects_graphs.drop(columns=impossible_projects, level=0, inplace=True)

def get_projects_bipartite_graph(projects, persons_list):
    """For a given t this needs to be computed only once. Once contributors are  assigned
    to a project, you should remove their matching row in the projects bipartite graph"""
    projects_graphs = {}
    for project in projects:
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
        projects_graphs[project]=pd.DataFrame(dicos, columns=[i for i in range(len(project.roles))], index=persons).fillna(0)

    # let the magic happen
    return pd.concat(projects_graphs.values(), keys=projects_graphs.keys(), axis=1)

def update_bipartite_graph(projects_graphs):
    """Remove rows of matrix where contributors are now not available"""
    projects_graphs.drop(index=[person for person in projects_graphs.index if person.available_in>0], inplace=True)


def is_project_possible(project_graph):
    # Remove rows with only zeros, i.e. persons that cnanot contribute
    # to this project
    temp = project_graph.loc[~(project_graph==0).all(axis=1)]
    # If a column is full of zeroes, that means no person
    # has a required skill for that project, so the project is not possible
    if (temp==0).all(axis=0).any():
        return False, []
    
    # Not enough collaborators to fill all roles in project
    if len(temp) < len(temp.columns):
        return False, []
    data,possible_contributors = temp.to_numpy(), temp.index.tolist()
    if not len(data):
        return False, []
    
    row_ind, col_ind = linear_sum_assignment((-1)*data)
    assigned_persons = []
    for i in range(len(row_ind)):
        index = col_ind.tolist().index(i)
        assigned_persons.append(possible_contributors[row_ind[index]])
    max_couplage = data[row_ind, col_ind].sum()
    return max_couplage == len(project_graph.columns), assigned_persons


