from parse_data import compute_skills, parse_data
from paths import PATHS


def cost_function(project, persons):
    return project.score_per_day


def cost_function_with_skills(coef_score, coef_cost, project, persons, projects):
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


if __name__ == "__main__":
    path = PATHS["a"]

    contributors, projects = parse_data(path)
    print("skills:\n", compute_skills(contributors, projects))
    score = cost_function_with_skills(1, 1, projects[1], contributors, projects)
    print(score)
