import pandas as pd
from dataclasses import dataclass

from parse_data import parse_data
from paths import PATHS


def update_t(t, contributors, projects):
    for person in contributors:
        if person.available_in > 0:
            person.available_in -= 1

    for project in projects:
        if (t + project.length) > project.best_before:
            if project.score_per_day > 0:
                project.score_per_day -= 1 / project.length


def update_choose(contributors, projects, chosen_project, chosen_persons):
    for worker in chosen_persons:
        for person in contributors:
            if person.name == worker.name:
                person.available_in = chosen_project.length

    for i, project in enumerate(projects):
        if project.name == chosen_project.name:
            del projects[i]


if __name__ == "__main__":
    path = PATHS["a"]
    contributors, projects = parse_data(path)

    print(projects)
    update_t(5, contributors, projects)
    update_choose(
        contributors, projects, projects[1], [contributors[1], contributors[2]]
    )

    print(projects)
