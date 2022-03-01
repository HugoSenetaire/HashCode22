from parse_data import compute_skills, parse_data
from paths import PATHS


def score_function(project, persons=None):
    return project.score_per_day

def score_function_per_day_and_nb_roles(project):
    return project.score_per_day/sum([role.skill_level for role in project.roles])


def score_function_with_skills(coef_score, coef_cost, project, persons, projects):
    project_score = project.score_per_day
    skills_demand_offer = compute_skills(persons, projects)
    skill_cost = 0
    for role in project.roles:
        level = role.skill_level
        skill_cost += (
            skills_demand_offer[role.skill_name][f"nb_projects_{level}"]
            / skills_demand_offer[role.skill_name][f"nb_contribs_{level}"]
        )
    return coef_score * project_score - coef_cost * skill_cost
