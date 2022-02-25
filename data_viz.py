from parse_data import compute_skills, parse_data
from paths import PATHS
import matplotlib.pyplot as plt


def plot_projects_wrt_contribs(projects, contributors):
    skills_distrib = compute_skills(contributors, projects).T[
        ["nb_projects", "nb_contribs"]
    ]
    plt.scatter(
        skills_distrib["nb_contribs"].values, skills_distrib["nb_projects"].values
    )
    plt.show()


if __name__ == "__main__":
    path = PATHS["a"]
    contributors, projects = parse_data(path)
    skills_distrib = compute_skills(contributors, projects).T

    print(skills_distrib.sort_values("nb_projects", ascending=False))
    # plot_projects_wrt_contribs(projects, contributors)
