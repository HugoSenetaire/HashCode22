from collections import defaultdict
from dataclasses import dataclass
import pandas as pd

from paths import PATHS


def parse_data(path):
    contributors = []
    projects = []

    with open(path, "r") as f:
        nb_contributors, nb_projects = f.readline().replace("\n", "").split(" ")
        for i in range(int(nb_contributors)):
            name, nb_skills = f.readline().replace("\n", "").split(" ")
            skills = {}
            for j in range(int(nb_skills)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                skills[skill_name] = int(skill_level)
            contributors.append(Contributor(name, skills))

        for i in range(int(nb_projects)):
            (project_name, project_length, score, best_before, nb_roles,) = (
                f.readline().replace("\n", "").split(" ")
            )
            roles = []
            for j in range(int(nb_roles)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                roles.append(Role(skill_name, int(skill_level)))

            projects.append(
                Project(
                    project_name,
                    int(project_length),
                    int(score),
                    int(best_before),
                    roles,
                )
            )

    # print("contributors: \n", contributors)
    # print("projects:\n", projects)
    return (contributors, projects)


# TODO: available, available_in
def compute_skills(contributors, projects):
    skills_data = defaultdict(lambda: defaultdict(int))
    for project in projects:
        for role in project.roles:
            skills_data[role.skill_name][f"nb_projects_{int(role.skill_level)}"] += 1
            skills_data[role.skill_name]["nb_projects"] += 1

    for contributor in contributors:
        if contributor.available_in < 1:
            for skill in contributor.skills:
                level = contributor.skills[skill]
                for i in range(1, int(level)+1):
                    skills_data[skill][f"nb_contribs_{i}"] += 1
                skills_data[skill]["nb_contribs"] += 1

    return pd.DataFrame(skills_data).fillna(0)


@dataclass
class Role:
    skill_name: str
    skill_level: int


class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.available_in = 0

    def __repr__(self):
        return f"<Contributor {self.name} | {self.skills}>"


class Project:
    def __init__(self, name, length, score, best_before, roles):
        self.name = name
        self.length = length
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.score_per_day = score / length

    def __str__(self):
        return (
            f"<Project {self.name}>"
        )

    def __repr__(self) -> str:
        return (
            f"<Project {self.name}>"
        )
    
    def __lt__(self, other):
        return self.name < other.name
    


if __name__ == "__main__":
    path = PATHS["b"]

    contributors, projects = parse_data(path)

    print(sum([project.length for project in projects]))
    print(max([project.best_before + project.score for project in projects]))
