
from list_all_contributors import get_all_combination_contributor

def get_best_combination(best_project, contributors):
    """
    Return the best contributor combination for best project
    """
    best_combination = []
    best_score = 0
    all_combinations = get_all_combination_contributor(best_project, contributors)

    for combination in all_combinations:
        score = 0
        for k, contributor in enumerate(combination):

            score+=contributor.skills[best_project.roles[k].skill_name] -  best_project.roles[k].skill_level
            if score > best_score:
                best_score = score
                best_combination = combination


    return best_combination
