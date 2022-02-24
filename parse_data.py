from collections import defaultdict
from dataclasses import dataclass
import pandas as pd
from paths import PATHS


def parse_data(path):
    contributors_data = []
    projects = []
    skills_data = defaultdict(lambda: defaultdict(int))
    with open(path, "r") as f:
        nb_contributors, nb_projects = f.readline().replace("\n", "").split(" ")
        for i in range(int(nb_contributors)):
            contributors_data.append({})
            contributor = contributors_data[-1]
            contributor["name"], nb_skills = f.readline().replace("\n", "").split(" ")
            for j in range(int(nb_skills)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                contributor[skill_name] = int(skill_level)
                skills_data[skill_name][f"nb_contribs_{int(skill_level)}"] += 1
                skills_data[skill_name]["nb_contribs"] += 1

        for i in range(int(nb_projects)):
            (project_name, project_length, score, best_before, nb_roles,) = (
                f.readline().replace("\n", "").split(" ")
            )
            roles = []
            for j in range(int(nb_roles)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                roles.append(Role(skill_name, skill_level))
                skills_data[skill_name][f"nb_projects_{int(skill_level)}"] += 1
                skills_data[skill_name]["nb_projects"] += 1
            projects.append(
                Project(project_name, project_length, score, best_before, roles)
            )
    contributors = pd.DataFrame(contributors_data).fillna(0)
    skills = pd.DataFrame(skills_data).fillna(0)

    print("contributors: \n", contributors)
    print("projects:\n", projects)
    print("skills:\n", skills)
    return contributors, projects, skills


@dataclass
class Role:
    skill_name: str
    skill_level: int


class Project:
    def __init__(self, name, length, score, best_before, roles):
        self.name = name
        self.length = length
        self.score = score
        self.best_before = best_before
        self.roles = roles

    def __str__(self):
        return (
            f"<Project {self.name} | score: {self.score} | roles : {len(self.roles)}>"
        )

    def __repr__(self) -> str:
        return (
            f"<Project {self.name} | score: {self.score} | roles : {len(self.roles)}>"
        )


if __name__ == "__main__":
    path = PATHS["a"]

    parse_data(path)
