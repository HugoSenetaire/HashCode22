def list_projets_possible(leaving_projects, persons_list):
    available_projects = leaving_projects; 
    for project in leaving_projects:
        feasible_project = false 
        for role in project.roles :
            feasible_role = false
            for person in persons_list : 
                for key in person.index : 
                    if key == role : 
                        feasible_role = true 
                        persons_list.remove(person)
                        break
                 if feasible_role : 
                     break
             if !feasible_role : 
                 available_projects.remove(project);
                 break
    return available_projects

