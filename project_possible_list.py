def project_possible_list(remaining_projects, persons_list):
    available_projects = remaining_projects;
    for project in remaining_projects:
        avaible_persons = persons_list
        feasible_project = False 
        for role in project.roles :
            feasible_role = False
            for person in persons_list : 
                for skill in person.skills.keys() : 
                    if skill == role : 
                        feasible_role = True 
                        avaible_persons.remove(person)
                        break
                if feasible_role : 
                     break
            if not feasible_role : 
                available_projects.remove(project)
                break
    return available_projects
