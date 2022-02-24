from dataclasses import dataclass
import pandas as pd


def parse_data(path):
    contributors_data = []
    projects = []
    # contributors = DataFrame()
    with open(path, "r") as f:
        nb_contributors, nb_projects = f.readline().split(" ")
        for i in range(int(nb_contributors)):
            contributors_data.append({})
            contributor = contributors_data[-1]
            contributor["name"], nb_skills = f.readline().split(" ")
            for j in range(int(nb_skills)):
                skill_name, skill_level = f.readline().split(" ")
                contributor[skill_name] = int(skill_level)
        contributors = pd.DataFrame(contributors_data).fillna(0)

        for i in range(int(nb_projects)):
            (
                project_name,
                project_length,
                score,
                best_before,
                nb_roles,
            ) = f.readline().split(" ")
            roles = []
            for j in range(int(nb_roles)):
                skill_name, skill_level = f.readline().split(" ")
                roles.append(Role(skill_name, skill_level))
            projects.append(
                Project(project_name, project_length, score, best_before, roles)
            )

    print("contributors: \n", contributors)
    print("projects:\n", projects)
    return contributors, projects


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
    a = "data/a_an_example.in.txt"
    b = "data/b_better_start_small.in.txt"
    c = "data/c_collaboration.in.txt"
    d = "data/d_dense_schedule.in.txt"
    e = "data/e_exceptional_skills.in.txt"
    f = "data/f_find_great_mentors.in.txt"

    parse_data(a)
