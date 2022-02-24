def project_possible_list(remaining_projects, persons_list):
    available_projects = remaining_projects; 
    for project in remaining_projects:
        feasible_project = false 
        for role in project.roles :
            feasible_role = false
            for person in persons_list : 
                for skill in person.skills.keys() : 
                    if skill == role : 
                        feasible_role = true 
                        persons_list.remove(person)
                        break
                 if feasible_role : 
                     break
             if !feasible_role : 
                 available_projects.remove(project);
                 break
    return available_projects
