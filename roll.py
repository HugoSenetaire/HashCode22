from update_fonction import update_t, update_choose


def roll_project_list_project_possible(contributors, projects, cost_function, max_iter = 1e5):
  """
  Roll the project list until we fill all projects  
  #Parameters :
  #   contributors : DF of contributors
  #   projects : list of <Project>

  #Return :
  #   trajectory

  """

  trajectory = str("")
  t = 0
  while (not len(projects) > 0) and t<max_iter:
      t +=1
      update_t(projects, contributors, t)
      dispo_projects = project_possible_list(projects, contributors)
      while len(dispo_projects)>0 :
          best_project = get_best_project(dispo_projects, cost_function)
          best_contributor = get_best_contributor(best_project, contributors)          
          update_choose(projects, contributors, best_project, best_contributor)
          trajectory = write_trajectory(trajectory, best_project, best_contributor)

  return trajectory
        



def roll_project_list_project_possible(contributors, projects, cost_function, max_iter = 1e5):
  """
  Roll the project list until we fill all projects. Difference with previous is we treat contributor and project at the same time for value
  #Parameters :
  #   contributors : DF of contributors
  #   projects : list of <Project>
  #   cost_function : function cost that take as input a contributor and a project, returns a float

  #Return :
  #   trajectory

  """

  trajectory = str("")
  t = 0
  while (not len(projects) > 0) and t<max_iter:
      t +=1
      update_t(projects, contributors, t)
      dispo_projects,dispo_contributors = project_contributors_possible_list(projects, contributors)
      while len(dispo_projects)>0 :
          best_project, best_contributor = get_best_project_and_contributors(dispo_projects, contributors, cost_function)
          
          update_choose(projects, contributors, best_project, best_contributor)
          trajectory = write_trajectory(trajectory, best_project, best_contributor)

  return trajectory
        
