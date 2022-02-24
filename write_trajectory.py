def write_trajectory(trajectory, best_project, best_contributor):
    trajectory += f"{best_project.name}"
    for contrib in best_contributor:
        trajectory += f" {contrib.name}"

    trajectory+= "\n"

    return trajectory
