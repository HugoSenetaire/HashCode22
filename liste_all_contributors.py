import copy

def get_all_combination_contributor(project, contributors):
    combinations = get_combination_contributor(project.roles, [], contributors)
    return combinations


def get_combination_contributor(roles, combination, contributors):
    liste_combination = []
    if len(roles) == 1 :
        for i, contributor in enumerate(contributors) :
            aux_combination = copy.deepcopy(combination)
            for skill in contributor.skills.keys() :
                if skill == roles[0].skill_name and contributor.skills[skill] >= roles[0].skill_level -1 :
                    aux_combination.append(contributor)
                    liste_combination.append(combination)

        return liste_combination
                      
    else :
        for i, contributor in enumerate(contributors) :
            aux_combination = copy.deepcopy(combination)

            for skill in contributor.skills.keys():
                if skill == roles[0].skill_name and contributor.skills[skill] >= roles[0].skill_level -1 :
                    aux_combination.append(contributor) 
                    new_contributors = contributors.copy()
                    del new_contributors[i]

                    next_combinations_list = get_combination_contributor(roles[1:], aux_combination, new_contributors)
                    liste_combination.extend(next_combinations_list)
                    
        return liste_combination