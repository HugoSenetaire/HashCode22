import copy

def get_all_combination_contributor(project, contributors,):
    combinations = get_combination_contributor(project.roles, [], contributors)
    
    return combinations


def get_combination_contributor(roles, combination, contributors, return_first= False):

    liste_combination = []
    if len(roles) == 1 :
        for i, contributor in enumerate(contributors) :
            if contributor.available_in < 1 :
                for skill in contributor.skills.keys() :
                    aux_combination = copy.deepcopy(combination)
                    if skill == roles[0].skill_name and int(contributor.skills[skill]) >= int(roles[0].skill_level) :
                        

                        aux_combination.append(contributor)
                        if return_first :
                            return [aux_combination]
                        liste_combination.append(aux_combination)

        return liste_combination
                      
    else :
        for i, contributor in enumerate(contributors) :
            if contributor.available_in < 1 :
                for skill in contributor.skills.keys():
                    aux_combination = copy.deepcopy(combination)
                    if skill == roles[0].skill_name and int(contributor.skills[skill]) >= int(roles[0].skill_level) :
                        aux_combination.append(contributor) 
                        new_contributors = copy.deepcopy(contributors)
                        del new_contributors[i]
                        next_combinations_list = get_combination_contributor(roles[1:], aux_combination, new_contributors)
                        liste_combination.extend(next_combinations_list)
                        
        return liste_combination
